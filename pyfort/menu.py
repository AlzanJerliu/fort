import os

from colorama import init
from termcolor import colored, cprint
from pyfort.secret.secret_json import * 
from pyfort.secret.secret_sqlite import delete_table 


# use Colorama to make Termcolor work on Windows too
init()

# Main menu
def show_menu():
    while True: 
        print('\n[Login / Signup / Erase / Ctrl+C] \nLogin:Already created account / Signup:Create new account / Erase:Delete account!!!')
        choice = input('>')
        # To login into account
        if choice.lower() == 'login':
            user_name = input(' Enter user name:')
            user_pwd = getpass.getpass(f' Enter password for {user_name}:')
            login(user_name, user_pwd)
            del(user_pwd)
            del(user_name)
                
        # To signup for new user    
        elif choice.lower() == 'signup':
            try:
                print('>Creating new user')
                user_name = input(' Enter user name:')
                loc = f'{PATH}/{user_name}.json'
                # Check if user name is available
                if os.path.exists(loc):
                    print(' User already exist')
                    print(' Try another name')
                else:
                    userpwd = getpass.getpass(f' Enter password for {user_name}:')
                    signup(user_name, userpwd)
                    print(colored('Account created', 'green'))
                    print(colored('Database created', 'green'))
            except Exception as Error:
                print(colored('>Something went wrong','red'))
                print(Error)
                
        # To delete all user related files and data
        elif choice.lower() == 'erase':
            flag = False
            user_name = input('Enter user name:')
            userpwd = input(f'Enter password for {user_name}:')
            loc = f'{PATH}/{user_name}.json'
            # Check if user exist
            if os.path.exists(loc):
                print(f'>File {user_name}.json exist')
                print('>Verifying password')
                flag = verify_password(user_name, userpwd, loc)
                if flag:
                    print('!!password verified')
                    confirm = input('>>Confirm want to delete account [Y/n]:')
                    confirm1 = input('  >>Sure want to delete data [Y/n]:')
                    if confirm == 'Y' and confirm1 == 'Y':
                        delete_table(user_name)
                        os.remove(loc)
                        print('!!User file and data deleted!!')
                else:
                    print('!!password incorrect')
            else:
                print('No such file found')
                            