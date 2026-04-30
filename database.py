import sqlite3

DB_NAME = "zombie_overflow.db"

def connect():
    return sqlite3.connect(DB_NAME)


def createAccount(username, password, security_answer):
    con = connect()
    cursor = con.cursor()

    try:
        cursor.execute("""
                       INSERT INTO users (username, password, security_answer)
                       values (?, ?, ?)
                       """, (username, password, security_answer))
        
        con.commit()
        return True
    except sqlite3.IntegrityError:
        return False
    
    finally:
        con.close()



def checkLogin(username, password):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   SELECT *FROM users
                   WHERE username = ? AND password = ?
                    """, (username, password))
    user = cursor.fetchone()
    con.close()

    return user



def checkUser(username):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   SELECT *FROM users
                   WHERE username = ?
                    """, (username,))
    result = cursor.fetchone()
    con.close()

    return result is not None



def checkSecurity(username, security_answer):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   SELECT * FROM users
                   WHERE username = ? AND LOWER(security_answer) = LOWER(?)
                   """, (username, security_answer))
    
    user = cursor.fetchone()
    con.close()

    return user



def updatePassword(username, new_password):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   UPDATE users
                   SET password = ?
                   WHERE username = ?
                   """, (new_password, username))
    
    con.commit()
    con.close()



def updateUser(username, new_user):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   UPDATE users
                   SET username = ?
                   WHERE username = ?
                   """, (new_user, username))
    
    con.commit()
    con.close()



def getUser(username):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                    SELECT username From users
                    WHERE username = ?
                    """, (username,))
    
    result = cursor.fetchone()
    con.close()

    return result



def getCoins(username):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   SELECT coins From users
                   WHERE username = ?
                   """, (username,))
    
    result = cursor.fetchone()
    con.close()

    return result



def updateCoins(username, coins):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   UPDATE users
                   SET coins = ?
                   WHERE username = ?
                   """, (coins, username))

    con.commit()
    con.close()



def getInventory(username):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   SELECT items.item_name, inventory.quantity
                   FROM inventory
                   JOIN users ON users.user_id = inventory.user_id
                   JOIN items ON items.item_id = inventory.item_id
                   WHERE users.username = ?
                   """, (username,))
    
    items = cursor.fetchall()
    con.close()

    return items



def addInventory(username, item_name):
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
                   SELECT user_id FROM users
                   WHERE username = ?
                   """, (username,))
    user = cursor.fetchone()

    cursor.execute("""
                   SELECT item_id FROM items
                   WHERE item_name = ?
                   """, (item_name,))
    item = cursor.fetchone()

    if user is None or item is None:
        con.close()
        return False

    user_id = user[0]
    item_id = item[0]

    cursor.execute("""
                   SELECT quantity FROM inventory
                   WHERE user_id = ? AND item_id = ?
                   """, (user_id, item_id))
    existing_item = cursor.fetchone()

    if existing_item:
        cursor.execute("""
                       UPDATE inventory
                       SET quantity = quantity + 1
                       WHERE user_id = ? AND item_id = ?
                       """, (user_id, item_id))
    else:
        cursor.execute("""
                       INSERT INTO inventory (user_id, item_id, quantity)
                       VALUES (?, ?, 1)
                       """, (user_id, item_id))

    con.commit()
    con.close()
    return True



def createTables():
    con = connect()
    cursor = con.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        security_answer TEXT NOT NULL,
        coins INTEGER DEFAULT 0
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS items (
        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
        item_name TEXT UNIQUE NOT NULL,
        price INTEGER NOT NULL,
        description TEXT
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventory (
        inventory_id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        item_id INTEGER NOT NULL,
        quantity INTEGER DEFAULT 1,
        FOREIGN KEY (user_id) REFERENCES users(user_id),
        FOREIGN KEY (item_id) REFERENCES items(item_id)
    )
    """)

    con.commit()
    con.close()