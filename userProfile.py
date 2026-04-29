import login

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
        print(displayUser())
    elif(choice == 3):
        print(displayCoins())
    elif(choice == 4):
        print(displayInventory())
    elif(choice == 5):
        return
    else:
        print("Please enter the numbered option: ")


def displayCoins():
    return None

def displayInventory():
    return None

def displayUser():
    return None

def changeUser():
    return

def changePassword():
    return


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

        
