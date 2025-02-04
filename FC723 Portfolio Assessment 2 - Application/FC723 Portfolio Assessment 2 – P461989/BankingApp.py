import Utilties as Ut
class Banking_app:
    def __init__(self,Accounts):
        self.Accounts=Accounts


#========================================================================================================     Intial Menu code   =====================================================================================================


    def initial_Menu(self):# the first menu appear to ask for log on or sign in
        option=input("Enter service number\n\n1- for Sign in\n===========\n2- for log in\n===========\n3- Exit\n")# this is the menu
        if option =="3":
            return
        
        if option =="1":
             New_Username=input("Enter New Username:\n ")
             while self.Check_username_availability(New_Username)== False or Ut.Utility.Check_username_valid(New_Username)==False:
                 #print("\nUsername is not availbile or contain space\s. Write new one")
                 New_Username=input("Enter New Username:\n  ")
                 
             New_password=input("Write a password:\n ")
             while Ut.Utility.Check_if_password_valid(New_password)== False : # while the password is not valid the app will continue to take passwords from the user until one of them is valid
                     print("The password should be from 8 to 16 characters, and does not contain spaces")#message for the user if the password is not valid
                     New_password=input("Write a password ")# to write the password again
                     
             print("\nYou have to deposit money in your new account")
             moneyfordeposit=input("Enter the ammount of money\n")
             while Ut.Utility.is_input_float(moneyfordeposit)== False:
                 print("Please make sure you enter a valid number")
                 moneyfordeposit=input("Enter the ammount of money\n")
             floatmoneydeposit=float(moneyfordeposit)
             floatamount= floatmoneydeposit- int(floatmoneydeposit)
             intgeramount= int(floatmoneydeposit)
             self.add_New_accounts_to_data(New_Username, New_password, intgeramount,floatamount)
             print(self.Accounts)
             self.App_main_interface(New_Username)



#=========================================================================================================  Intial Menu code end  ===================================================================================================================






#=====================================================================================================     The app main interface code   =====================================================================================================
    def App_main_interface(self,Username):
        option=input("\nPlease Enter the service number\n1-Withdrawl\n===========\n2-Deposit\n===========\n3-Display Balance\n===========\n4-Transfer money\n===========\n5-Exit account\n")
        if option =="3":
            self.Display_balance(Username)
        


    def add_New_accounts_to_data(self,Username,Password,money_deposited,Money_Float_Amount):# this function is to add a new account to the data
        template={"Username": Username, "Password": Password,"Balance": "0","Balance_sign": True,"Overdraft_Allowance": 1500,"is_locked_out":False,"floats_amount": 0.0}# this is template to fill the data for the new account. this will be added to the accounts lists
        balance=Ut.Utility.twos_complement_to_decimal(template["Balance"])# to convert the balance from binary to decimal
        new_balance=balance+money_deposited #after prompt the user to deposit money this line to add the deposited money to the balance
        finalbalance=Ut.Utility.dec_to_2complemnt(new_balance) # convert the final balance to binary
        template["Balance"]=finalbalance # set the final balance in the data
        template["floats_amount"]=Money_Float_Amount # set the amount of float money in to the floats_amount in the data. floats amount the change of money like 0.50
        self.Accounts.append(template)# add the new account to the data
            
        
    def Check_username_availability(self,Username):# this to check if username avialible when creating a new username
        for account in self.Accounts :# loop through the accounts
            if account["Username"] == Username: #check if name exist
                return False# if yes return flase
        return True # if the username availible return true



    def Display_balance(self,Username):# to display the balance
        for account in self.Accounts:#loop through the account
            if Username == account["Username"]:# check if accont names are the same. to display the right account balance
                balanceinbinary= account["Balance"]# get the balance in binary stored in the data
                decbalance=Ut.Utility.twos_complement_to_decimal(balanceinbinary)#convert the balance in binary to decimal
                flt=account["floats_amount"] # get the float amount stored in the account because its part of the balance 
                displayamount=flt+decbalance #add the float and balance together
                print(f"You Balance is:\n{displayamount}")# display the balance
                print(self.Accounts)


##=====================================================================================================     The app main interface the end of the code   =====================================================================================================



























    
dd=Banking_app(Ut.data.Accounts)
Username=dd.initial_Menu()
