
import Utilties as Ut


#this will be used in the tests
Accounts =[ 
    {
        "Username": "Abdulmalik", #  unique username 
        "Password": "12345678",# normal password must be between 8 to 16 characters
        "Balance": "00000000000000000000010100010100",# balance in binary
        
        "Overdraft_Allowance": 1500,   #this is the overdraft limit 
        "is_locked_out":False # is the account locked out or not
        
    },
    {
        "Username": "Sam112233",
        "Password": "123456789",
        "Balance": "00000000000000000000010100010100",
        
        "Overdraft_Allowance": 1500,
        "is_locked_out":True
           
    },
    {
        "Username": "mono133",
        "Password": "1q2w3e4r5t",
        "Balance": "0",
        
        "Overdraft_Allowance": 1500,
        "is_locked_out":False
        
    },
    { 
        "Username": "Hydro1233", 
        "Password": "12345678",
        "Balance": "00000000000000000000010100010100",
        
        "Overdraft_Allowance": 1500,   
        "is_locked_out":False
    }
      ]




#===============================================  Banking app utilities functions  ================================================================

def Display_balance(Username):# to display the balance
    for account in Accounts:#loop through the account
        if Username == account["Username"]:# check if accont names are the same. to display the right account balance
            balanceinbinary= account["Balance"]# get the balance in binary stored in the data
            decbalance=Ut.Utility.twos_complement_to_decimal(balanceinbinary)#convert the balance in binary to decimal
            Overdraft=account["Overdraft_Allowance"]
            print(f"Your Overdraft Alowance:\n{Overdraft} GBP\n====================\nYou Balance is:\n{decbalance} GBP\n====================")# display the balance
            return decbalance

def Display_balance_overdraft(Username):# to display the overdraft limit ### this is new fuction just for the tests
    for account in Accounts:#loop through the account
        if Username == account["Username"]:# check if accont names are the same. to display the right account overdraft limit
            balanceinbinary= account["Balance"]# get the balance in binary stored in the data
            decbalance=Ut.Utility.twos_complement_to_decimal(balanceinbinary)#convert the balance in binary to decimal
            Overdraft=account["Overdraft_Allowance"]
            print(f"Your Overdraft Alowance:\n{Overdraft} GBP\n====================\nYou Balance is:\n{decbalance} GBP\n====================")# display the balance
            return Overdraft # overdraft limit

def add_New_accounts_to_data(Username,Password,money_deposited):# this function is to add a new account to the data
##The line above have been changed from the orginal function. I Just removed self parameter

    template={"Username": Username, "Password": Password,"Balance": "0","Balance_sign": True,"Overdraft_Allowance": 1500,"is_locked_out":False,"floats_amount": 0.0}# this is template to fill the data for the new account. this will be added to the accounts lists
    balance=Ut.Utility.twos_complement_to_decimal(template["Balance"])# to convert the balance from binary to decimal
    new_balance=balance+money_deposited #after prompt the user to deposit money this line to add the deposited money to the balance
    finalbalance=Ut.Utility.dec_to_2complemnt(new_balance) # convert the final balance to binary
    template["Balance"]=finalbalance # set the final balance in the data
    

    Accounts.append(template)# add the new account to the data
    ##The line above have been changed from the orginal function insead of loop through self. account I put accounts in this file to be in the same file


def Is_account_locked(Username):# this function check if the account locked or not. to make sure that you can log in to it or transfer to it
#The line above have been changed from the orginal function. I removed self parameter
    for i in Accounts:
    ##The line above have been changed from the orginal function. changed from self.Account to Account.
    
        if i["Username"]==Username:# after looping through the accounts and find the right account 
            if i["is_locked_out"] ==True:# check if the account locked or not
                return True# if the account locked it will return true
    return False# if the account is not locked it will return False




def Check_username_availability(Username):# this to check if username avialible when creating a new username
#the line above have been changed from the orginal function. I removed self Parameter
    for account in Accounts :# loop through the accounts
    #the line above have been changed from the orginal function. instead of self.Accounts I putted Account
        if account["Username"] == Username: #check if name exist
            return False# if yes return flase
    return True # if the username availible return true
    

def Password_Checker(Username,Password):
    #the line above have been changed from the orginal function. I removed self Parameter
    for i in Accounts:
        #the line above have been changed from the orginal function. I removed self.Account and put Account
        if i["Username"]==Username:
            if i["Password"]==Password:
                return True
    return False



#==============================================   Functions require user inputs   ===========================================================


### those functions have been changed to set values in the function parameters.



def Deposit(Username,inn):# this function is to deposit money in the account
    
    
    if Ut.Utility.is_input_intger_number(inn)==False:
        return "not valid input"
    depositamount = int(inn)# convert the input from string number to intger class number
    for account in Accounts:
        if Username == account["Username"]:#after looping through account check if names are the same to deposit to the right account
            balance_in_binary=account["Balance"]#convert balance to decimlal
            balance_dec=Ut.Utility.twos_complement_to_decimal(balance_in_binary)#
            final_amount=balance_dec+depositamount
            newbalance=Ut.Utility.dec_to_2complemnt(final_amount)
            account["Balance"]=newbalance


def Withdrawl(Username,inn):# funtion to withdrawl money including overdraft withdrawl   
     for i in Accounts:# loop through accounts
         if i["Username"] == Username:# check if the usernames are the same to withdrawl from the right user
             balance=Ut.Utility.twos_complement_to_decimal(i["Balance"])# get the balance in decimal
             
             if inn =="1":# option is 1 means user want to withdrawl 500
                 amount="500"
             if inn =="2":# option is 2 means user want to withdrawl 100
                 amount="100"
             if inn=="3":# option is 3 means user want to withdrawl 20
                 amount="20"
             if inn=="4":#option is 4 means user want to withdrawl 10
                 amount="10"
             if inn=="5":#option is 5 means user want to withdrawl custom amount

                     amount="1170"# just a new option was added to simulate user input possibilities
                     
             if inn=="6":#just a new option was added to simulate user input possibilities
                 amount="-1000"
                 
             if inn=="7":
                amount="123d"
             
             if Ut.Utility.is_input_intger_number(amount)==False:#check if user input is not int number
                 return "User input is not valid"# 
             

             amount=int(amount)#make the amount intger after taking it from the user from the first time
             if Ut.Utility.is_balance_sufficient(i, amount)== True:# check if balance is sufficient 
                 balance-=amount# subtract the amount from the balance to get the new balance
                 i["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# set the balance back to 2'complemnts
                 print(f"withdrawal of {amount} GBP have been successful")#success message
                 return
             if Ut.Utility.is_balance_sufficient(i, amount)== False:# check balance is sufficient if not
                 print("insufficient balance")# will print a message to say that                
                 questtion="1" 
                 if questtion=="2":# if answer is no
                        return
                 if questtion=="1":# if answer is yes
                        if balance+i["Overdraft_Allowance"] == amount:# check if balance and overdraft together equal the amount wanted if yes balance and oerdraft limit will be set to 0

                           i["Balance"]= Ut.Utility.dec_to_2complemnt(0)# set the balance to zero
                           #balance=0# balance will be zero
                           i["Overdraft_Allowance"]=0# over draft limit will be zero
                           print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")# show message of success
                           return
                           
                        if i["Overdraft_Allowance"] < amount and balance < amount and i["Overdraft_Allowance"]+balance >= amount :# if the overdraftamount wantned greater than overdraft limit and balance, but they can achieve the amount wanted together   
                            balance-=amount# first we will take all the money from the balance then we get the rest from the overdraft limit
                            i["Overdraft_Allowance"]=i["Overdraft_Allowance"]+balance# then we take the rest of amount from the over draft limit. notice the balance will be negative here so it subtracting operation
                            i["Balance"]= Ut.Utility.dec_to_2complemnt(0)# set the balance to zero
                            print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")# show a success message
                            return
                            
                            
                        if i["Overdraft_Allowance"] >= amount:# if the amount is less or equal to the amount wanted. this will happen when the balance is not enough so we want to take from the overdraft but first we have to take all what is inside the account then suptract the rest from the overdraft allowance
                            restOfmoney=amount-balance# we get the rest of money after subtracting the amount from the balance
                            i["Overdraft_Allowance"]= i["Overdraft_Allowance"]- restOfmoney# suptract the rest from the overdraft limit
                            i["Balance"]= Ut.Utility.dec_to_2complemnt(0)#set balance to zero
                            print(f"withdrawal of {amount} GBP from overdraft Allowance have been successful")# message
                            return

                        if i["Overdraft_Allowance"] < amount:# if the amount is greater than the balance and the overdraft limit together
                            print("Overdraft limit exceded, or the amount you asked for is greater than the balance and overdraft together")#message
                            return





def Transfer(Username,receiver,amount):# this is transfer function to transfer money from account to another by using usernames which are unique
 
    if Is_account_locked(receiver)== True:# if the receiver account is locked you can not transfer to it
        print("==========\nthis account is locked out you can not transfer money to it\n==========")# message tells that the receiver account is locked
        return "Receiver account is locked out"# get the user back to the main iterface
        
        
    while Check_username_availability(receiver)== True: # while the username of the receiver is not avilible thats mean the account does not exist 
        return "This account does not exist"# message and take the input again
        
    if Ut.Utility.is_input_intger_number(amount)==False:
        return "number is not valid"
    
       
    amount=int(amount)# convert the string number to intger
    
    
    for i in Accounts:
        if i["Username"]==Username:
            if Ut.Utility.is_balance_sufficient(i, amount)==False:
                print("Balance is not sufficient")
                return "Not sufficient"
    
    
    for rec in Accounts:# loop throgh accounts to find the receiver 
        if rec["Username"]==receiver:# check usernames are the same
            balance=rec["Balance"]# take the balance of the receiver
            balance=Ut.Utility.twos_complement_to_decimal(balance)# convert it to decimal
            balance=balance+amount# add the money to the reciver balance 
            rec["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# ger the balance back to 2'complements

    
    for Useraccount in Accounts:# for user that transfer the money
        if Useraccount["Username"]==Username: #check if usernames are the same
            balance=Useraccount["Balance"]# get the balance of the user
            balance=Ut.Utility.twos_complement_to_decimal(balance)# convert the balance to decimal
            balance-=amount# subtract the amount from the abalance
            Useraccount["Balance"]=Ut.Utility.dec_to_2complemnt(balance)# convert it back to 2'complements
            print(f"===============\n{amount} GBP Transfer from your account to {receiver} have been successful\n===============")# print success message
            return 
            
         




#========================   Testing add_New_accounts_to_data   ==============================================================================================
def Help_to_test_add_New_accounts_to_data(Username,Password,Balance):# this function will check if the account already added if yes will return True## this is a new function for the tests.
    for o in Accounts:#loop through the accounts
        if o["Username"]== Username:#check if usernames are the same
            if o["Password"]==Password:#chheck if passwords are the same
                if o["Balance"]=="00000000000000000000001111101000":#check if balances are the same
                    if o["is_locked_out"]==False:#check if that its not locked out which is putted as default
                        if o["Overdraft_Allowance"]==1500:# check if the overdraft limit is the same . its 1500 by default
                            return True# mean the account added and exist
                        

    return False# means the account does not exist

def test_add_New_accounts_to_data(): # test the function that add new account to the data(list of accounts(dictionaries))
    add_New_accounts_to_data("Hydro", "123123123", 1000)# just using the function to add the account
    assert Help_to_test_add_New_accounts_to_data("Hydro","123123123",1000)==True,"If the account added output will be True" # test if the function did add the account to the list of accounts added or not
    assert Help_to_test_add_New_accounts_to_data("Username", "Password123", 500)==False, "This account does not exist must return False"# test if the function will recognize account that doess not exist



#=================================  Testing Is_account_locked  =========================================================================================
def test_Is_account_locked():# test the function that checks if the account locked out or not      
    assert Is_account_locked("Sam112233")== True,"The account is locked out, output must be False"# check if the function will recognize that the account is locked
    assert Is_account_locked("mono133")== False,"The account is not locked out the output must be False"#this will test  if the function will recognize the account added recentlly and will knows that its not locked out

    
    
#===========  Testing Check_username_availability  =================

def test_Check_username_availability():#this will test the usernames availbility function
    assert Check_username_availability("Abdulmalik")==False,"The account Username is not availible the output must be False"#this will test if the function recognize that the account username is not availible
    assert Check_username_availability("Hydro")==False,"The account Username is not availible, the account is added recently the output must be False "# this will test if the function can recognize that the account username is not availible because its added recently in the code above
    assert Check_username_availability("CheeseeMori") == True,"this username is avilible the output must be True"# this will test if the function can recognize if the name given is availible
    
#============= Testing Password_Checker   ========================
def test_Password_Checker():#this will test the function that check if username and password mathces the same account
    assert Password_Checker("Abdulmalik", "12345678")==True,"This account password is for this Username the function must return True"# this check if the function will recognize that the username and password are for the same account
    assert Password_Checker("Hydro", "123123123")==True, "this account added recently and the password and username match function must return True"# check if the function can check the password and username for account that is added recently
    assert Password_Checker("mono133", "Password123")==False,"This account username does not matches the account password output must be False"#check if the function can recognize if the password annd username does not match


#=================================  Testing Display Balance  =========================================================================================

def test_Display_balance():#this will check if the balance are the same as what display balance function says
    assert Display_balance("Abdulmalik")==1300,"User has 1300"#check if function can recognize the correct  balance
    assert Display_balance_overdraft("mono133")==1500, "User overdaft limit is 1500" #check if function can recognizze overdraft



   
            
            
#=================================  Testing Deposit function  =========================================================================================

def test_Deposit():
    Deposit("mono133","500")
    assert Display_balance("mono133")==500
    assert Deposit("mono133", "-100")=="not valid input"
    assert Deposit("mono133", "1d00")=="not valid input"


#=================================  Testing Withdrawl function  =========================================================================================


def test_Withdrawl():
    
    Withdrawl("mono133","1")  #withdraw 500 from account "mono133"
    #check if the balance after withdrawal is 0
    assert Display_balance("mono133") == 0, "the account has 0 after withdrawing 500"
    Withdrawl("Abdulmalik", "2")  ## withdraw 100 from abdulmalik's account
    #verify if the balance is now 1200 ( 1300 - 100)
    assert Display_balance("Abdulmalik") == 1200  
    Withdrawl("Abdulmalik", "3")  #withdraw 20
    assert Display_balance("Abdulmalik") == 1180  # check balance
    Withdrawl("Abdulmalik", "4")  #withdraw another 10
    assert Display_balance("Abdulmalik") == 1170  # verify balance
    Withdrawl("Abdulmalik", "5")  # withdraw remaining balance
    assert Display_balance("Abdulmalik") == 0  # account should be empty
    Withdrawl("Abdulmalik", "1")  #attempt withdrawal when balance is 0
    #check overdraft balance, should be 1000 after using overdraft
    assert Display_balance_overdraft("Abdulmalik") == 1000  
    Deposit("Abdulmalik", "1000")  #deposit 1000 into abdulmalik's account
    # check that the balance is now 1000
    assert Display_balance("Abdulmalik") == 1000  
    # overdraft balance should remain at 1000
    assert Display_balance_overdraft("Abdulmalik") == 1000  
    Withdrawl("Abdulmalik", "5")  #withdraw entire balance(1000)
    # balance should now be 0
    assert Display_balance("Abdulmalik") == 0  
    #overdraft balance should be 830 after withdrawal
    assert Display_balance_overdraft("Abdulmalik") == 830  
    Withdrawl("Abdulmalik", "1")  # withdraw 500 more using overdraft
    # balance remains 0 since only overdraft is being used
    assert Display_balance("Abdulmalik") == 0  
    ##overdraft balance should now be 330 after withdrawal
    assert Display_balance_overdraft("Abdulmalik") == 330  

    assert Withdrawl("Hydro1233", "6")=="User input is not valid"#check if the function will recognize that the input is invalid
    assert Withdrawl("Hydro1233", "7")=="User input is not valid"#check if the function will recognize that the input is invalid



#=================================  Testing Transfer function  =========================================================================================

def test_Transfer():
    # check if transfer fails due to insufficient funds
    assert Transfer("Abdulmalik", "mono133", "330") == "Not sufficient"  
    
    # deposit 2000 into mono133's account
    Deposit("mono133", "2000")  
    
    # check if transfer fails because the receiver's account is locked
    assert Transfer("mono133", "Sam112233", "100") == "Receiver account is locked out"  
    
    # check if transfer fails due to invalid negative amount
    assert Transfer("mono133", "Abdulmalik", "-100") == "number is not valid"  
    
    # check if transfer fails due to non-numeric input
    assert Transfer("mono133", "Abdulmalik", "81h8") == "number is not valid"  
    
    # perform a valid transfer of 1100 from mono133 to abdulmalik
    Transfer("mono133", "Abdulmalik", "1100")  
    
    # check if abdulmalik's balance is updated correctly
    assert Display_balance("Abdulmalik") == 1100  
    
    # check if mono133's balance is updated correctly after transfer
    assert Display_balance("mono133") == 900  

    # check if transfer fails due to a non-existent account
    assert Transfer("mono133", "mooo123", "100") == "This account does not exist"
