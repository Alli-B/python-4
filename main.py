import ast
from random import randint

def Account_num(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

print("Hello! Welcome to SNH bank please select an option")
print("select 1 for Login")
print('Select 2 to Exit')
choice = input('')
while True:
    try:
        if choice == "1":
            print("Please enter your details to log in")
            username1 = input("Please enter your username: ")
            password1 = input("Please enter your password: ")
            f=open("staff.txt", "r")
            lines=f.readlines()
            jack = lines[1]
            dictionary = ast.literal_eval(jack)
            f.close()
            correct_username = dictionary['username']
            correct_password = dictionary['password']
            if username1 == correct_username and password1 == correct_password:
                print("Log-in successful")
                while True:
                    try:
                        
                        print("select 1 to Create new bank account")
                        print('Select 2 to Check account Details')
                        print('Select 3 to Logout')
                        login_choice = input('')        
                        if login_choice == "1":
                            acct = input("Please enter your Account name: ")
                            Balance = input("Please enter your Opening Balance: ")
                            Type = input("Please enter your Account type: ")
                            Mail = input("Please enter your Email: ")
                            customer = {}
                            customer['Account_name'] = acct
                            customer['Account_Balance'] = Balance
                            customer['Account_Type'] = Type
                            customer['Account_mail'] = Mail
                            customer['Account_number'] = Account_num(10)

                            f = open("customers.txt","a")
                            f.write( str(customer) )
                            f.close()
                            print("\nThank you for a succeful registration \nYour account number is")
                            print(customer['Account_number'])
                            break
                        elif login_choice == "2":
                            User_input = int(input("Please enter your Account number: "))
                            User_accountNumber = int(User_input)
                            z=open("customers.txt", "r")
                            lines=z.readlines()
                            june = lines[0]
                            details = ast.literal_eval(june)
                            print(details['Account_number'])
                            if User_accountNumber == details['Account_number']:
                                print("Your account name is: ")
                                print(details['Account_name'])
                                print("Your account balance is: ")
                                print(details['Account_Balance'])
                                print("Your account type is: ")
                                print(details['Account_Type'])
                                print("Your account mail is: ")
                                print(details['Account_mail'])
                                print("Your account number is is: ")
                                print(details['Account_number'])
                            else:
                                print("Wrong details")
                            f.close()
                            break
                        elif login_choice == "3":
                            print("Thank you for banking with us ")
                            exit()
                        print("Invalid selection \nTry again \n")
                    except Exception as e:
                        print(e)
            break
        elif choice == "2":
            print("Thank you for banking with us")
            exit()
        print("Invalid selection \nTry again \n")
    except Exception as e:
        print(e)
