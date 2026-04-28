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
            
            if(choice > 5 or choice < 1):
                raise ValueError
            else:
                return choice
            

        except ValueError:
            print('\033[1m' + "*** PLEASE ENTER A NUMBER 1-5 ***" + '\033[0m')
            value = 0

def total_currency():
    return None

def total_items():
    return None

def userInfo():
    return None

print('')
login.print_equals()
print('')


while(True):
    number = 10000
    number = profileMenu()
    print(number)
    break
        
