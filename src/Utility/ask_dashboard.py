
def ask_for_dashboard():
    while True:
        print('\n1 BACK TO  DASHBOARD')
        print('2 LOGOUT')
        choise = input('please choose a option : ')
        if(choise == '1'):
            return True 
        elif(choise == '2'):
            return False

        else:
            print('please choose a correct option.')
            continue