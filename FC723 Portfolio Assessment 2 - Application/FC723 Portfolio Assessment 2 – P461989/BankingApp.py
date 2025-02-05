import Utilties as Ut
class Banking_app:
    def __init__(self,Accounts):
        self.Accounts=Accounts


#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\    Intial Menu code    /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\   


    def initial_Menu(self):# the first menu appear to ask for log on or sign in
        option=input("Enter service number\n\n1- for Sign in\n===========\n2- for log in\n===========\n3- Exit App\n")# this is the menu
        if option =="3":
            return
        
        if option =="1":
             New_Username=input("Create New Username:\n ")
             while self.Check_username_availability(New_Username)== False or Ut.Utility.Check_username_valid(New_Username)==False:
                 #print("\nUsername is not availbile or contain space\s. Write new one")
                 New_Username=input("Create New Username:\n  ")
                 
             New_password=input("Create a password:\n ")
             while Ut.Utility.Check_if_password_valid(New_password)== False : # while the password is not valid the app will continue to take passwords from the user until one of them is valid
                     print("\nThe password should be from 8 to 16 characters, and does not contain spaces")#message for the user if the password is not valid
                     New_password=input("Write a new password ")# to write the password again
                     
             print("\nYou have to deposit money in your new account")
             moneyfordeposit=input("Enter the ammount of money\n")
             while Ut.Utility.is_input_intger_number(moneyfordeposit)== False:
                 print("Please make sure you enter a valid number")
                 moneyfordeposit=input("Enter the ammount of money\n")
             intgeramount= int(moneyfordeposit)
             self.add_New_accounts_to_data(New_Username, New_password, intgeramount)
             self.App_main_interface(New_Username)



#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_ The end of Intial Menu code  \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/






#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\     The app main interface code   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\
    def App_main_interface(self,Username):
        option=input("Please Enter the service number\n1-Withdrawl\n===========\n2-Deposit\n===========\n3-Display Balance\n===========\n4-Transfer money\n===========\n5-Exit App\n===========\n6-Log out\n")
        if option == "5":
            return
        if option =="6":
            self.initial_Menu()
        
        if option =="3":
            self.Display_balance(Username)
        
        if option == "2":
            self.Deposit(Username)
            
        if option == "1":
            self.Withdrawl(Username)


    def add_New_accounts_to_data(self,Username,Password,money_deposited):# this function is to add a new account to the data
        template={"Username": Username, "Password": Password,"Balance": "0","Balance_sign": True,"Overdraft_Allowance": 1500,"is_locked_out":False,"floats_amount": 0.0}# this is template to fill the data for the new account. this will be added to the accounts lists
        balance=Ut.Utility.twos_complement_to_decimal(template["Balance"])# to convert the balance from binary to decimal
        new_balance=balance+money_deposited #after prompt the user to deposit money this line to add the deposited money to the balance
        finalbalance=Ut.Utility.dec_to_2complemnt(new_balance) # convert the final balance to binary
        template["Balance"]=finalbalance # set the final balance in the data
        self.Accounts.append(template)# add the new account to the data
            
        
    def Check_username_availability(self,Username):# this to check if username avialible when creating a new username
        for account in self.Accounts :# loop through the accounts
            if account["Username"] == Username: #check if name exist
                return False# if yes return flase
        return True # if the username availible return true
        


    


#\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/     the end of main interface code   \_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/\_/





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


    def Deposit(self,Username):
        inn=input("Enter a amount of money ")
        while Ut.Utility.is_input_intger_number(inn) == False:
            print("Please make sure you enter a valid number ")
            inn=input("Enter a amount of money ")
        depositamount = int(inn)
        
        for account in self.Accounts:
            if Username == account["Username"]:
                balance_in_binary=account["Balance"]
                balance_dec=Ut.Utility.twos_complement_to_decimal(balance_in_binary)
                final_amount=balance_dec+depositamount
                newbalance=Ut.Utility.dec_to_2complemnt(final_amount)
                account["Balance"]=newbalance

                #print(account)
                self.App_main_interface(Username)# run the interface again
                
                
#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\     The Deposit function code   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\


#/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\    Withdral function   /-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\/-\


    def Withdrawl(self,Username):# funtion to withdrawl money including overdraft withdrawl
        print("\nEnter service number:")# intructing message
        inn=input("\n1-500 GBP\n2-100 GBP\n3-20 GBP\n4-10 GBP\n5-Custom amount\n6-Go back\n")# take service number
        services=["1","2","3","4","5","6"]#the services numbers 
        while inn not in services : #if the service number not in the services list or a random string it will asks again for an input
            print("Plese enter service number")# intructing message
            inn=input("\n1-500 GBP\n2-100 GBP\n3-20 GBP\n4-10 GBP\n5-Custom amount\n6-Go back\n")#take the input again

        if inn=="6":# if user want togo back to the main interface
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
                    amount=input("Enter amount:\n")# input of how much money user want to withdrawl 
                    while Ut.Utility.is_input_intger_number(amount) == False:# while amount is not valid like letters etc.
                        amount=input("Please Enter a Valid Number:\n")# enter the number again
                        amount=int(amount)#make the amount intger after taking it from the user after 2 or more times
                    amount=int(amount)#make the amount inger after taking it from the user from the first time
                    
                
                    
                    
                    
                if Ut.Utility.is_balance_sufficient(i, amount)== True:# check if balance is sufficient 
                    balance-=amount# subtract the amount from the balance to get the new balance
                    i["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# set 
                    print(f"withdrawal of {amount} GBP have been successful")
                    self.App_main_interface(Username)
                if Ut.Utility.is_balance_sufficient(i, amount)== False:
                    print("insufficient balance")
                    
                    
                    questtion=input("Do you want to use overdraft alowance?\n1-Yes\n2-No\n")
                    servicesnum=["1","2"]
                    while questtion not in servicesnum:
                        questtion=input("Please Enter a number\nDo you want to use overdraft alowance?\n1-Yes\n2-No\n")
                        
                        
                    if questtion=="2":
                           self.App_main_interface(Username)
                           
                    if questtion=="1":
                           if balance+i["Overdraft_Allowance"] == amount:
                              
                              i["Balance"]= Ut.Utility.dec_to_2complemnt(0)
                              balance=0
                              i["Overdraft_Allowance"]=0
                              print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")
                              self.App_main_interface(Username)
                              
                           if i["Overdraft_Allowance"] < amount and balance < amount and i["Overdraft_Allowance"]+balance >= amount :
                               balance-=amount
                               i["Overdraft_Allowance"]=i["Overdraft_Allowance"]+balance
                               i["Balance"]= Ut.Utility.dec_to_2complemnt(0)
                               print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")
                               self.App_main_interface(Username)
                               
                               
                           if i["Overdraft_Allowance"] >= amount:
                               restOfmoney=amount-balance
                               i["Overdraft_Allowance"]= i["Overdraft_Allowance"]- restOfmoney
                               i["Balance"]= Ut.Utility.dec_to_2complemnt(0)
                               print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")
                               self.App_main_interface(Username)

                           if i["Overdraft_Allowance"] < amount:
                               print("Overdraft limit exceded")
                               self.App_main_interface(Username)
                        
                        











    
dd=Banking_app(Ut.data.Accounts)
Username=dd.initial_Menu()