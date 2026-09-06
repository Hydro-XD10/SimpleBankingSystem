import Utilties as Ut # self-made module
class Banking_app:
    def __init__(self,Accounts):# constructor method
        self.Accounts=Accounts# accounts is list of accounts and accounts are in dictionarries. we could scale this app to bigger one by creating a new class and inhert this one eg. Special banking app for and pass a list of special accounts.


#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\    Intial Menu code    /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\   


    def initial_Menu(self):# the first menu appear to ask for log on or sign in
        option=input("Enter service number\n\n1- for Sign in\n===========\n2- for log in\n===========\nEnter- Exit App\n")# this is the menu
        if option ==" ":
            return# if option is space which is close the app
       
        if option =="2":# to log into existing account
            
            
            
            Username=input("To go back Enter space\nEnter Username: ")#take user name for log in
            if Username==" ":# to go back
                return self.initial_Menu()# to go back
            while self.Check_username_availability(Username)==True:#check if the name exist and if the input is valid
               Username=input("\nTo go back Enter space\nThe Username is wrong: ")# if not input valid or the username is does not exist it will keep taking input
               if Username==" ":#to go back
                   self.initial_Menu()#to go back
            if self.Is_account_locked(Username)==True:#after taking the username we want to check if its locked out first
                print("This account is locked contact the bank")# instructing message
                self.initial_Menu()# get it back to the sign in page after finding out if the accoubnt locked or not 
#==================================================================================================
            for i in self.Accounts:
                if i["Username"] == Username:
                    counter = i["Password_attempts"]
                    Password = input("\nEnter space to go back\nIf password is incorrect after three attempts, the account will be locked out\nEnter Password: ")  # take the password
        
                    if Password == " ":  # to go back
                        for i in self.Accounts:
                            if i["Username"] == Username:
                               i["Password_attempts"] = counter    
                        self.initial_Menu()  # to go back

                    while Ut.Utility.Check_if_password_valid(Password) == False or self.Password_Checker(Username, Password) == False:  # while password is invalid (not between 8-16 characters or incorrect)
                        if counter == 1:  # If counter reaches 0 (third failed attempt)
                            for i in self.Accounts:  # loop through the accounts
                                if i["Username"] == Username:  # finding the username of the account
                                    i["is_locked_out"] = True  # lock out the account
                                    print("==========\nThe account has been locked out. Contact the bank please.\n==========")  # message for the user
                                    return self.initial_Menu()  # take it back to the sign-in menu
                        counter -= 1  # decrease the password attempts counter
                        Password = input(f"\nEnter space to go back\nPassword is not valid, enter password again or incorrect:\n{counter} attempt\s left\n\n ")  # asks again for the password
            
                        if Password == " ":  # to go back
                            for i in self.Accounts:
                                if i["Username"] == Username:
                                    i["Password_attempts"] = counter
                            self.initial_Menu()  # to go back
            
            if counter == 0:  # If counter reaches 0 (third failed attempt)
                for i in self.Accounts:  # loop through the accounts
                    if i["Username"] == Username:  # finding the username of the account
                        i["is_locked_out"] = True  # lock out the account
                        print("==========\nThe account has been locked out. Contact the bank please.\n==========")  # message for the user
                        return self.initial_Menu()  # take it back to the sign-in menu
            
            i["Password_attempts"]==3# if user pass the correct the password the aattempts will back to 3
            self.App_main_interface(Username)  # let the user enter the app interface to perform operations, always passing Username as a reference
                    
            
            
            
        if option =="1":# to sign in (create new account)
             New_Username=input("To go back Enter space\nCreate New Username:\n ")# take the username
             if New_Username== " ":#to go back
                 self.initial_Menu()#to go back
             while self.Check_username_availability(New_Username)== False or Ut.Utility.Check_username_valid(New_Username)==False:# while and username is not valid (has spaces or empty input)  and the username is not availible because username is the unique part of the account
                 print("\nUsername is not availbile or contain space\s. Write new one")# message for the user
                 New_Username=input("To go back Enter space\nCreate New Username:\n  ")#take the username again
                 if New_Username==" ":#to go back
                     self.initial_Menu()#to go back
                 
             New_password=input("To go back Enter space\nCreate a password:\n ")# create new password
             if New_password==" ":#to go back
                 self.initial_Menu()#to go back
             while Ut.Utility.Check_if_password_valid(New_password)== False : # while the password is not valid the app will continue to take passwords from the user until one of them is valid
                     print("\nThe password should be from 8 to 16 characters, and does not contain spaces")#message for the user if the password is not valid
                     New_password=input("To go back Enter space\nWrite a new password ")# to write the password again
                     if New_password==" ":#to go back
                         self.initial_Menu()#to go back
                     
             print("\nYou have to deposit money in your new account")#instructing message
             moneyfordeposit=input("Enter the ammount of money\n")# the amount want to be diposited
             while Ut.Utility.is_input_intger_number(moneyfordeposit)== False:# while the input is not valid (intger ) it will keep asking for valid input and show error message
                 print("Please make sure you enter a valid number")
                 moneyfordeposit=input("To go back Enter space\nEnter the ammount of money\n")
                 if moneyfordeposit== " ":#to go back
                     self.initial_Menu()#to go back
             intgeramount= int(moneyfordeposit)# convert it from string number to intger
             self.add_New_accounts_to_data(New_Username, New_password, intgeramount)# add it to the data stucture
             self.App_main_interface(New_Username)#get access to the app interface with the username as reference(New_Username)
#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_ The end of Intial Menu code  \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/






#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\     The app main interface code   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\
    def App_main_interface(self,Username):# this is the app interface that has withdrawl,transfer, deposit, display balance, exit app and log out
        #this is to take the service number vvvv
        option=input("Please Enter the service number\n1-Withdrawl\n===========\n2-Deposit\n===========\n3-Display Balance\n===========\n4-Transfer money\n===========\n5-Exit App\n===========\n6-Log out\n")
        num_Services=["1","2","3","4","5","6"]
        while option not in num_Services :
            option=input("Please Enter the service number\n1-Withdrawl\n===========\n2-Deposit\n===========\n3-Display Balance\n===========\n4-Transfer money\n===========\n5-Exit App\n===========\n6-Log out\n")
        
        if option == "5":# exit app
            return
        if option =="6":
            self.initial_Menu() # log out
        
        if option =="3": #show balance
            self.Display_balance(Username)
        
        if option == "2":# deposit money
            self.Deposit(Username)
            
        if option == "1":#withdrawl
            self.Withdrawl(Username)
        if option =="4":# transfer
            self.Transfer(Username)
#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/     the end of main interface code   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/







#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\     Utilities Functions   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\

    #Those Utilities functions need parameter self to work thats why there are in the same file as the main code of the banking app
    



    def add_New_accounts_to_data(self,Username,Password,money_deposited):# this function is to add a new account to the data
        template={"Username": Username, "Password": Password,"Balance": "0","Password_attempts":3,"Overdraft_Allowance": 1500,"is_locked_out":False}# this is template to fill the data for the new account. this will be added to the accounts lists
        balance=Ut.Utility.twos_complement_to_decimal(template["Balance"])# to convert the balance from binary to decimal
        new_balance=balance+money_deposited #after prompt the user to deposit money this line to add the deposited money to the balance
        finalbalance=Ut.Utility.dec_to_2complemnt(new_balance) # convert the final balance to binary
        template["Balance"]=finalbalance # set the final balance in the data
        self.Accounts.append(template)# add the new account to the data
            

    def Is_account_locked(self,Username):# this function check if the account locked or not. to make sure that you can log in to it or transfer to it
        for i in self.Accounts:
            if i["Username"]==Username:# after looping through the accounts and find the right account 
                if i["is_locked_out"] ==True:# check if the account locked or not
                    return True# if the account locked it will return true
        return False# if the account is not locked it will return False




    def Check_username_availability(self,Username):# this to check if username avialible when creating a new username
        for account in self.Accounts :# loop through the accounts
            if account["Username"] == Username: #check if name exist
                return False# if yes return flase
        return True # if the username availible return true
        

    def Password_Checker(self,Username,Password):#this function checks if the password and username are for the same account
        for i in self.Accounts:#loop through accounts
            if i["Username"]==Username:# check if usernames are the same
                if i["Password"]==Password:# check password for the same account match
                    return True # if the password and the username for the same account match the function will return true
        return False # otherwise it will return false
#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/     the end of Utilities function code code   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/






#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\     display balance function   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\


    def Display_balance(self,Username):# to display the balance
        for account in self.Accounts:#loop through the account
            if Username == account["Username"]:# check if accont names are the same. to display the right account balance
                balanceinbinary= account["Balance"]# get the balance in binary stored in the data
                decbalance=Ut.Utility.twos_complement_to_decimal(balanceinbinary)#convert the balance in binary to decimal
                Overdraft=account["Overdraft_Allowance"]
                print(f"Your Overdraft Alowance:\n{Overdraft} GBP\n====================\nYou Balance is:\n{decbalance} GBP\n====================")# display the balance
                self.App_main_interface(Username)# run the interface again

#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/     The end of display balance function code   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/



#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\     Deposit function   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\


    def Deposit(self,Username):# this function is to deposit money in the account
        inn=input("To go back Enter space\nEnter a amount of money ")#take the input of the amount of money
        if inn==" ":#to go back 
            self.App_main_interface(Username)#to go back
        while Ut.Utility.is_input_intger_number(inn) == False:# check if iniput valid intger number
            print("Please make sure you enter a valid number ")#instructing message if the condtion above is true
            inn=input("To go back Enter space\nEnter a amount of money ")# if invaild number given this will repated until valid input given
            if inn==" ":# to go back
                self.App_main_interface(Username)#to go back
        depositamount = int(inn)# convert the input from string number to intger class number
        
        for account in self.Accounts:
            if Username == account["Username"]:#after looping through account check if names are the same to deposit to the right account
                balance_in_binary=account["Balance"]#convert balance to decimlal
                balance_dec=Ut.Utility.twos_complement_to_decimal(balance_in_binary)#
                final_amount=balance_dec+depositamount
                newbalance=Ut.Utility.dec_to_2complemnt(final_amount)
                account["Balance"]=newbalance

                print(f"{depositamount} GBP is deposited successfully")
                self.App_main_interface(Username)# run the interface again
                

#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\    End of The Deposit function code    /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\


#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\    Withdral function   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\


    def Withdrawl(self,Username):# funtion to withdrawl money including overdraft withdrawl
        print("\nEnter service number:")# intructing message
        inn=input("\n1-500 GBP\n2-100 GBP\n3-20 GBP\n4-10 GBP\n5-Custom amount\n6-Go back\n")# take service number
        services=["1","2","3","4","5","6"]#the services numbers 
        while inn not in services : #if the service number not in the services list or a random string it will asks again for an input
            print("Plese enter service number")# intructing message
            inn=input("\n1-500 GBP\n2-100 GBP\n3-20 GBP\n4-10 GBP\n5-Custom amount\n6-Go back\n")#take the input again

        if inn=="6":# if user want to go back to the main interface
            self.App_main_interface(Username)
        
        
        for i in self.Accounts:# loop through accounts
            if i["Username"] == Username:# check if the usernames are the same to withdrawl from the right user
                balance=Ut.Utility.twos_complement_to_decimal(i["Balance"])# get the balance in decimal
                
                if inn =="1":# option is 1 means user want to withdrawl 500
                    amount=500
                if inn =="2":# option is 2 means user want to withdrawl 100
                    amount=100
                if inn=="3":# option is 3 means user want to withdrawl 20
                    amount=20
                if inn=="4":#option is 4 means user want to withdrawl 10
                    amount=10
                if inn=="5":#option is 5 means user want to withdrawl custom amount
                    amount=input("To go back Enter space\nEnter amount:\n")# input of how much money user want to withdrawl 
                    if amount==" ":#to go back
                        self.Withdrawl(Username)#to go back
                    while Ut.Utility.is_input_intger_number(amount) == False:# while amount is not valid like letters etc.
                        amount=input("To go back Enter space\nPlease Enter a Valid Number:\n")# enter the number again
                        if amount==" ":#to go back
                            self.Withdrawl(Username)#to go back
                        amount=int(amount)#make the amount intger after taking it from the user after 2 or more times
                    amount=int(amount)#make the amount intger after taking it from the user from the first time
                    
                
                    
                    
                    
                if Ut.Utility.is_balance_sufficient(i, amount)== True:# check if balance is sufficient 
                    balance-=amount# subtract the amount from the balance to get the new balance
                    i["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# set the balance back to 2'complemnts
                    print(f"withdrawal of {amount} GBP have been successful")#success message
                    self.App_main_interface(Username)#back to the main app interface
                
                if Ut.Utility.is_balance_sufficient(i, amount)== False:# check balance is sufficient if not
                    print("insufficient balance")# will print a message to say that
                    
                    
                    questtion=input("Do you want to use overdraft alowance?\n1-Yes\n2-No\n")# question if user want to use his overdraft alowance
                    servicesnum=["1","2"]# number of services 1 means yes 2 means no
                    while questtion not in servicesnum:#check if user put the service number
                        questtion=input("Please Enter a number\nDo you want to use overdraft alowance?\n1-Yes\n2-No\n")# asks again until user put 1 or 2 
                        
                        
                    if questtion=="2":# if answer is no
                           self.App_main_interface(Username)#get back to the interface
                           
                    if questtion=="1":# if answer is yes
                           if balance+i["Overdraft_Allowance"] == amount:# check if balance and overdraft together equal the amount wanted if yes balance and oerdraft limit will be set to 0
                              
                              i["Balance"]= Ut.Utility.dec_to_2complemnt(0)# set the balance to zero
                              #balance=0# balance will be zero
                              i["Overdraft_Allowance"]=0# over draft limit will be zero
                              print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")# show message of success
                              self.App_main_interface(Username)#get back to the main interface
                              
                           if i["Overdraft_Allowance"] < amount and balance < amount and i["Overdraft_Allowance"]+balance >= amount :# if the overdraftamount wantned greater than overdraft limit and balance, but they can achieve the amount wanted together   
                               balance-=amount# first we will take all the money from the balance then we get the rest from the overdraft limit
                               i["Overdraft_Allowance"]=i["Overdraft_Allowance"]+balance# then we take the rest of amount from the over draft limit. notice the balance will be negative here so it subtracting operation
                               i["Balance"]= Ut.Utility.dec_to_2complemnt(0)# set the balance to zero
                               print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")# show a success message
                               self.App_main_interface(Username)# get the user back to the main interface
                               
                               
                           if i["Overdraft_Allowance"] >= amount:# if the amount is less or equal to the amount wanted. this will happen when the balance is not enough so we want to take from the overdraft but first we have to take all what is inside the account then suptract the rest from the overdraft allowance
                               restOfmoney=amount-balance# we get the rest of money after subtracting the amount from the balance
                               i["Overdraft_Allowance"]= i["Overdraft_Allowance"]- restOfmoney# suptract the rest from the overdraft limit
                               i["Balance"]= Ut.Utility.dec_to_2complemnt(0)#set balance to zero
                               print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")# message
                               self.App_main_interface(Username)# get the user back to the main interface

                           if i["Overdraft_Allowance"] < amount:# if the amount is greater than the balance and the overdraft limit together
                               print("Overdraft limit exceded, or the amount you asked for is greater than the balance and overdraft together")#message
                               self.App_main_interface(Username)#get the user back to the app main interface
                        


#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_ The end of Withdrawl function code  \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/









                        
#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\    Transfer function   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\

    def Transfer(self,Username):# this is transfer function to transfer money from account to another by using usernames which are unique
        
                
            
        

        receiver=input("To go back Enter space\nEnter the Username of the receiver ")# the username of the reciver
        if receiver==" ":
            self.App_main_interface(Username)
        if self.Is_account_locked(receiver)== True:# if the receiver account is locked you can not transfer to it
            print("==========\nthis account is locked out you can not transfer money to it\n==========")# message tells that the receiver account is locked
            self.App_main_interface(Username)# get the user back to the main iterface
        while self.Check_username_availability(receiver)== True: # while the username of the receiver is not avilible thats mean the account does not exist 
            receiver=input("To go back Enter space\nUsername of the receiver is not Correct or does not exist\nEnter the name again ")# message and take the input again
            if receiver==" ":
                self.App_main_interface(Username)
        amount=input("To go back Enter space\nThe amount of money ")# take the amoun that wanted to be transfer
        if amount==" ":
            self.App_main_interface(Username)
        while Ut.Utility.is_input_intger_number(amount)== False:# while the number is wrong not string number 
            amount=input("To go back Enter space\nPlease Enter the amount in numbers ")# will keep take input from it
            if amount==" ":
                self.App_main_interface(Username)
        amount=int(amount)# convert the string number to intger
        
        
        for i in self.Accounts:
            if i["Username"]==Username:
                if Ut.Utility.is_balance_sufficient(i, amount)==False:
                    print("Balance is not sufficient")
                    self.App_main_interface(Username)
        
        
        for rec in self.Accounts:# loop throgh accounts to find the receiver 
            if rec["Username"]==receiver:# check usernames are the same
                balance=rec["Balance"]# take the balance of the receiver
                balance=Ut.Utility.twos_complement_to_decimal(balance)# convert it to decimal
                balance=balance+amount# add the money to the reciver balance 
                rec["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# ger the balance back to 2'complements

        
        for Useraccount in self.Accounts:# for user that transfer the money
            if Useraccount["Username"]==Username: #check if usernames are the same
                balance=Useraccount["Balance"]# get the balance of the user
                balance=Ut.Utility.twos_complement_to_decimal(balance)# convert the balance to decimal
                balance-=amount# subtract the amount from the abalance
                Useraccount["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# convert it back to 2'complements
                print(f"===============\n{amount} GBP Transfer from your account to {receiver} have been successful\n===============")# print success message
                self.App_main_interface(Username)# get the user back the main interface


#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_ The end of transfer function code  \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/




    
dd=Banking_app(Ut.data.Accounts)# create an instance.      and pass list of accounts
Username=dd.initial_Menu()# run the app