import Utilties as Ut
class Banking_app:
    def __init__(self,Accounts):
        self.Accounts=Accounts



    def initial_Menu(self):# the first menu appear to ask for log on or sign in
        option=input("Enter 1 for Sign in\n===========\nEnter 2 for log in\n")
        if option =="1":
             New_Username=input("Enter New Username:\n ")
             while self.Check_username_availability(New_Username)== False or Ut.Utility.Check_username_valid(New_Username)==False:
                 print("\nUsername is not availbile or contain space\s. Write new one")
                 New_Username=input("Enter New Username:\n  ")
                 
             New_password=input("Write a password:\n ")
             while Ut.Utility.Check_if_password_valid(New_password)== False : # while the password is not valid the app will continue to take passwords from the user until one of them is valid
                     print("The password should be from 8 to 16 characters, and does not contain spaces")#message for the user if the password is not valid
                     New_password=input("Write a password ")# to write the password again
                     
             print("\nYou have to deposit money in your new account")
             
             try:
                 moneyfordeposit=int(input("Enter the ammount of money\n"))
             
             except:
                 print("Please enter The amount in numbers")
                 moneyfordeposit=int(input("Enter the ammount of money\n"))
                 
             self.add_New_accounts_to_data(New_Username, New_password, moneyfordeposit)
             print(self.Accounts)
             self.App_main_interface()










    def App_main_interface(self):
        option=input("1-Withdrawl\n===========\n2-Deposit\n===========\n3-Display Balance\n===========\n4-Transfer money")
        
        


    def add_New_accounts_to_data(self,Username,Password,moneydeposited):
        template={"Username": Username, "Password": Password,
        "Balance": "0","Balance_sign": True,"Overdraft_Allowance": 1500,"is_locked_out":False}
        balance=Ut.Utility.twos_complement_to_decimal(template["Balance"])
        new_balance=balance+moneydeposited
        las=Ut.Utility.dec_to_2complemnt(new_balance)
        template["Balance"]=las
        self.Accounts.append(template)
            
        
    def Check_username_availability(self,Username):
        for account in self.Accounts :
            if account["Username"] == Username:
                return False
        return True

































    
dd=Banking_app(Ut.data.Accounts)
dd.initial_Menu()