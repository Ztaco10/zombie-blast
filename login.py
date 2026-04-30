import shutil
import database

def print_dashes():
    dash = '-'

    try:
        column = shutil.get_terminal_size().columns

        print(dash * column)
    except OSError:
        print(dash * 97)



def print_equals():
    equal = '='

    try:
        column = shutil.get_terminal_size().columns

        print(equal * column)
    except OSError:
        print(equal * 97)



def main_menu():
    print('\033[1m' + "*** MAIN MENU ***" + '\033[0m')
    print("1. Login")
    print("2. Create and Account")
    print("3. Forgot Password")
    print("4. About the Game")
    print("5. Exit Game")
    choice = int(input("Please enter the corresponding number to where you'd like to go: "))
    return choice



def login():
    while(True):
        print('')
        print_equals()
        print('')
        print('\033[1m' + "*** LOGIN PAGE ***" + '\033[0m')

        print("If you'd like to exit then please type '1' as username")
        
        username = input("Enter your username: ")

        if(username == "1"):
            print("Exiting login page")
            return
        
        password = input("Enter your password: ")

        user = database.checkLogin(username, password)
        if(user):
            print("Login Successful")
            return username
        else:
            print("Incorrect User or Password was entered")
        



def account_create():
    print('')
    print_equals()
    print('')
    print('\033[1m' + "*** ACCOUNT CREATION PAGE ***" + '\033[0m')
    print("If you'd like to exit then please type '1' as username")
    while(True):
        username = input("Please enter a valid username: ")
        #check if the username already exists
        if(username == "1"):
            print("Exiting account creation page")
            return
        elif(username == ""):
            print("Username cannot be empty")
        elif (database.checkUser(username)):
            print("Username already exists")
        else:
            break

    while(True):
        password = input("Enter password: ")
        if(password == 1):
            return
        elif(password == ""):
            print("Password cannot be empty")
        else:
            break

    while(True):
        security_answer = input("What city were you born in: ")
        if(security_answer == 1):
            return
        elif(security_answer == ""):
            print("Security question answer cannot be empty")
        else:
            break

    success = database.createAccount(username, password, security_answer)
    
    if success:
        print("Account successfully created")
        return username
    else:
        print("Account creation failed")



def password_change():

    print('')
    print_equals()
    print('')
    print('\033[1m' + "*** PASSWORD FORGOTTEN PAGE ***" + '\033[0m')
    print("If you'd like to exit at any time please type '1'")
    
    while(True):
        count = 0
        username = input("Please enter a valid username: ")

        if(username == "1"):
            print("Exiting changing password page")
            return
        
        if not database.checkUser(username):
            print("The username you have entered does not exist.")
            print('')
        else:
            break

    while(True):
        security_answer = input("What city were you born in: ")

        if(security_answer == "1"):
            print("Exiting changing password page")
            return
        
        user = database.checkSecurity(username, security_answer)
        if(user):
            break
        else:
            print("Answer was incorrect.")

    while(True):
        password = input("Please enter a new password: ")

        if(password == "1"):
            print("Exiting gchanging password page")
            return

        rePassword = input("Please reenter your password: ")
        if (password == rePassword):
            database.updatePassword(username, password)
            print("Password was successfully changed")
            return username
        print("Passwords did not match. Please try again")
    


def game_summary():
    print('')
    print_equals()
    print('')
    print("This is a math zombie game where you use math problems to defeat evil zombies! As you play you can earn currency and buy power-ups to better help you to defeat the zombies.")
    exit = input("Press enter to continue\n")    



def getUser():
    return currentUser



def startMenu():
    print('')
    print("_____________________________________")
    print('\033[1m' + "| HELLO WELCOME TO ZOMBIE OVERFLOW! |" + '\033[0m')
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    choice = 0
    value = 0
    global currentUser
    currentUser = None
    

    database.createTables()
    while(True):
        try:
            if(value != 0):
                print('')
                print_equals()
                print('')

            value = 1
            choice = main_menu()
            
            if(choice > 5 or choice < 1):
                raise ValueError

        except ValueError:
            print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
            value = 0

        if(choice == 1):
            currentUser = login()

            if(currentUser):
                return currentUser
            
        elif(choice == 2):
            currentUser = account_create()

            if(currentUser):
                return currentUser
            
        elif(choice == 3):
            currentUser = password_change()

            if(currentUser):
                return currentUser
            
        elif(choice == 4):
            game_summary()
        elif(choice == 5):
            break


        
