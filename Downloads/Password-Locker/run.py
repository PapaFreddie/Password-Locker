from user import User

def main():

    if True:
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
        print(f'Congratulations {created_username}!')
        print('\n')
        print("Continue to login")
        print("Username")
        entered_username = input()
        print("Your Password")
        entered_password = input()

    while entered_username != created_username or entered_password != created_user_password:
        print("Invalid username or password!")
        print("Username")
        entered_username = input()
        print("Enter your password")
        entered_password = input()


        
    else:
        print(f" Welcome {entered_username} to your account!")
        print('\n')






    