import login

def total_currency():
    return currency

def total_items():
    return items

def userInfo():
    return info

print('')
login.print_equals()
print('')

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
        choice = int(input("Please choose a number from"))
        value = 1
        
        if(choice > 5 or choice < 1):
            raise ValueError

    except ValueError:
        print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
        value = 0
#blank
