import login
import database

def profileMenu():
    value = 0
    while(True):
        try:
            print('')
            print('\033[1m' + "*** PROFILE MENU ***" + '\033[0m')
            print("1. Account Information")
            print("2. Change Username")
            print("3. Change Password")
            print("4. Exit to Main Menu ")


            if(value != 0):
                print('')
                login.print_equals()
                print('')
            choice = int(input("Please enter the numbered option: "))
            value = 1
            
            if(choice > 4 or choice < 1):
                raise ValueError
            else:
                return choice
            

        except ValueError:
            print('')
            print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-4 ***" + '\033[0m')
            value = 0

def accountInfo():
    value = 0
    try:
        
        print('')
        print('\033[1m' + "*** Account Info MENU ***" + '\033[0m')
        print("1. Display All Information")
        print("2. Display Username")
        print("3. Display Coins")
        print("4. Display Inventory")
        print("5. Exit to Profile Menu")


        if(value != 0):
            print('')
            login.print_equals()
            print('')
        choice = int(input("Please enter the numbered option: "))
        value = 1
        
        if(choice > 5 or choice < 1):
            raise ValueError
        else:
            return choice
            

    except ValueError:
        print('')
        print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
        value = 0

    if(choice == 1):
        
        print(displayUser())
        print(displayCoins())
        print(displayInventory())
    elif(choice == 2):
        print("")
        print(displayUser())
    elif(choice == 3):
        print("")
        print(displayCoins())
    elif(choice == 4):
        print("")
        print("INVENTORY")
        print(displayInventory())
    elif(choice == 5):
        return
    else:
        print("Please enter the numbered option: ")



def displayCoins():
    coins = database.getCoins(login.getUser())

    if coins:
        print(f"Coins: {coins[0]}")



def displayInventory():

    inventory = database.getInventory(login.getUser())

    if len(inventory) == 0:
        print("Your inventory is empty.")
    else:
        for item in inventory:
            print(item)



def displayUser():
    print(f"Username: {login.getUser()}")



def changeUser():
    print('')
    login.print_equals()
    print('')
    print('\033[1m' + "*** PASSWORD FORGOTTEN PAGE ***" + '\033[0m')
    print("If you'd like to exit at any time please type '1'")
    
    while(True):
        security_answer = input("What city were you born in: ")

        if(security_answer == "1"):
            print("Exiting changing password page")
            return
        
        user = database.checkSecurity(user, security_answer)
        if(user):
            break
        else:
            print("Answer was incorrect.")

        while(True):
            new_user = input("Please enter your new password: ")

            if(user == "1"):
                print("Exiting gchanging password page")
                return

            if(database.checkUser):
                database.updateUser(user, new_user)
                print(f"Username successfully changed to was successfully changed")
                break
            else:
                print("Username was already taken. Please try again")

    

    

def changePassword():
    print('')
    login.print_equals()
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
            break
        print("Passwords did not match. Please try again")
    


print('')
login.print_equals()
print('')


while(True):
    choice = profileMenu()

    if(choice == 1):
        accountInfo()
    elif(choice == 2):
        changeUser()
    elif(choice == 3):
        changePassword()
    elif(choice == 4):
        break

        
