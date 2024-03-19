#Task 1 loop over N time (N provided by user) Create N objects put it in a list
#Task 2 take username and password from user check which object it belongs to
#Task 3 display all information of that user
#Task 4 take username of person who you want to send money
#Task 5 find the object with that username amd deposit required amount
#Task 6 withdraw amount from your object and deposit ti target object

class Bank_Account:
    def __init__(self,user_name,name,pass_word,balance):
        # pass
        self.user_name = user_name
        self.name = name
        self.password = pass_word
        self.balance = balance
    
    def withdraw(self,amt):
        self.balance -= amt
        # pass

    def deposit(self,amt):
        self.balance += amt
        
    def show(self):
        print('Name: ',self.name)
        print('Username: ',self.user_name)
        print('Balance: ',self.balance)

import getpass
total_accounts = []  #For adding usernames in the list

while True:
    print("WELCOME TO KHWOPA BANKING SYSTEM")
    switcher = int(input("1: Add Users\n2: Login\n3: Exit\n"))
    match switcher:
        case 1:
            #Task 1 - User input for creating N number of usernames and adding to list
            user_num = int(input("\nHow many users to add?\n"))

            for i in range(user_num):         
                a = True
                while a == True:  # Loop for checking username already exists
                    username_exist = False       #Used for checking if username already exists
                    user_name = input(f'\nEnter Username for {i+1}:     ')
                    
                    for users in total_accounts:
                        if user_name == users.user_name:
                            print("Username already exists. Please use another username")
                            username_exist = True   
                            break
                    
                    if username_exist == False:
                        a = False
                        
                    """Comphrehension Code that didnt work 
                    # if user_name == [username_check.user_name for username_check in total_accounts]:
                    #     print("Username already exists. Please use another username")
                    """
                
                name = input("Enter your name:     ")
                password = getpass.getpass('Enter password:     ')
                balance = float(input('Enter bank balance:     '))
                total_accounts.append(Bank_Account(user_name,name,password,balance)) # Appending to list
                user_exist = True
                print(len(total_accounts))
        
        case 2:
            #Task 2 Take username and pw and check which object it belongs to
                print("\nLOGIN PANEL\n")
                login_check = False
                count = 0
                while login_check == False:
                                
                    username = input("Enter login username: ")
                    user_pw = input("Enter password to login: ")
                    
                    for sender in total_accounts:
                        if sender.user_name == username and sender.password == user_pw:
                            #Task 3 Display all information of that user
                            see = input("Would your like to see your Account details? yes/no")
                            if see.lower() == 'yes': sender.show()
                            
                            login_check = True
                            break
                        
                    if login_check == False:
                        print("\nInvalid username or password")
                        print("Try again")
                        count+=1
                    if count >3:
                        print("\nToo many attempts!!")
                        break

                username_check = False
                while username_check== False:    
                    receiver_username = input("\nWho do you want to send money to?(Write username of receiver)\n")
                    user_exist = False    #Checking if the receiver exists
                    # if receiver_username == [receiver.user_name for receiver in total_accounts]: 
                        # Can use while loop here to check if there is enough money in senders account to send the money
                    while user_exist == False:
                        for receiver in total_accounts:
                            if receiver_username == receiver.user_name:
                                amount = int(input("Enter how much money would you like to send?\n"))
                                sender.withdraw(amount)
                                receiver.deposit(amount)
                                user_exist = True # Exiting loop condition
                                username_check = True
                        if user_exist == False:
                            print("Username doesn't exist. Please write the correct username")

                #Printing Updated Account information
                print("\nUPDATED Sender Account Information:\n")
                sender.show()
                print("\nUPDATED Receiver Account Information:\n")
                receiver.show()
                print("\n")
        case 3:
            exit()        
    
