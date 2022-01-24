
from user import User

def main():

    while True:
        print("Welcome to password locker!")
        print('\n')
        print("Select a code to navigate through: to create new user use 'new: to login to your account 'log and 'ex' to exit")
        code = input().lower()
        print('\n')

        if code == 'new':
            print('create username')
            created_username = input()

            print('create password')
            created_user_password = input()
            print('confirm password')
            confirm_password = input()


            while confirm_password != created_user_password:
                print('Passwords do not match!')
                print('Enter valid password to match the previous!')
                created_user_password = input()
                print('Confirm your password')
                confirm_password = input()

            else:
                print(f'Hurray!!! {created_username}, Your account was created successfully!')
                print('\n')
                print("Continue to login")
                print("Username")
                entered_username = input()

                print("Your Password")
                entered_password = input()

            if  entered_username != created_username or entered_password != created_user_password:
                print("Invalid username or password!")
                print("Username")
                entered_username = input()

                print("Enter your password")
                entered_password = input()


        
            else:
                print(f" Welcome {entered_username} to your account!")
                print('\n')

        elif code == 'log':
            print("Welcome!")
            print("Enter Username")
            default_username = input()

            print("Enter your password")
            default_user_password = input()
            print('\n')

            while default_username != 'testuser' or default_user_password != '05121':
                print("Wrong Username or Password. Username 'testuser' Password '05121")
                print("Username")
                default_username = input()

                print("Enter Your Password")
                default_user_password = input()
                print('\n')
            else:
                print("Logged in successfully!")
                print('\n')
                print('\n')

        elif code == 'ex':
            breakpoint
        else:
            print("Enter valid code to proceed!")
            


if __name__ == '__main__':
    main()









    