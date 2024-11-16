from Src.Utility.color import Colors
def ask_for_dashboard():
    while True:
        print(f'\n{Colors.BRIGHT_MAGENTA}1 BACK TO  DASHBOARD')
        print(f'2 LOGOUT{Colors.RESET}')
        choise = input('please choose a option : ')
        if(choise == '1'):
            return True 
        elif(choise == '2'):
            return False

        else:
            print('please choose a correct option.')
            continue