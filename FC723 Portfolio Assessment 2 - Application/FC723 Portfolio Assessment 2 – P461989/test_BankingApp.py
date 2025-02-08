
import Utilties as Ut


#this will be used in the tests
Accounts =[ 
    {
        "Username": "Abdulmalik", #  unique username 
        "Password": "12345678",# normal password must be between 8 to 16 characters
        "Balance": "00000000000000000000010100010100",# balance in binary
        
        "Overdraft_Allowance": 1500,   #this is the overdraft limit 
        "is_locked_out":True # is the account locked out or not
        
    },
    {
        "Username": "Sam112233",
        "Password": "123456789",
        "Balance": "0",
        
        "Overdraft_Allowance": 1500,
        "is_locked_out":False
           
    },
    {
        "Username": "mono133",
        "Password": "1q2w3e4r5t",
        "Balance": "0",
        
        "Overdraft_Allowance": 1500,
        "is_locked_out":False
        
    }
    ]




#===============================================================================================================

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

#========================   Testing add_New_accounts_to_data   ==============================================================================================
def Help_to_test_add_New_accounts_to_data(Username,Password,Balance):# this function will check if the account already added if yes will return True
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
    assert Is_account_locked("Abdulmalik")== True,"The account is locked out, output must be False"# check if the function will recognize that the account is locked
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

    





































    
    
    
    
    
    
    
    
    