import Utilties as Ut
class Banking_app:
    def __init__(self,Accounts):
        self.Accounts=Accounts



    def initial_Menu():# the first menu appear to ask for log on or sign in
        option=input("Enter 1 for Sign in \nEnter 2 for log in ")
        if option =="1":
             New_Username=input("Enter New Username ")
             while Ut.Utility.Check_username_availability(New_Username) == False:
                 print("\nUsername is not availbile. Write new one")
                 New_Username=input("Enter New Username\n  ")
                 
                 New_password=input("Write a password")
                 while Ut.Utility.Check_if_password_valid(New_password)== False : # while the password is not valid the app will continue to take passwords from the user until one of them is valid
                     print("The password should be from 8 to 16 characters, and does not contain spaces")#message for the user if the password is not valid
                     New_password=input("Write a password ")# to write the password again
        if option == "2":
                






































    
Banking_app.initial_Menu()