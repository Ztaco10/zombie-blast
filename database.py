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
                   """, (username, new_password))
    
    con.commit()
    con.close()



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