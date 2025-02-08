class Utility:  
    
    def is_balance_sufficient(account,amount_of_money):# function that checks if the user got enough balance
        balance=Utility.twos_complement_to_decimal(account["Balance"])#get the balance in decimal
        
        if balance >= amount_of_money: # if balance greater that the amount of money wanted to withdrawl or transfer
            return True#return true which means enough money is in the account
        if balance < amount_of_money:# if there is less money in the balance than the amount wanted to withdrawl or transfer
            return False#will return false which  means there is no enough money in the balance
        
                
            
        
    def twos_complement_to_decimal(binarynum):# function that convert from 2'complemnts to decimal
        bits = len(binarynum)# check how many bits in the binarynum
        value = int(binarynum, 2)  #convert from binary to integer
        if binarynum[0] == '1':  #if the sign bit is 1, its negative
            value -= (1 << bits)  #convert again using two complement formula
        return value
    
    def dec_to_2complemnt(n, bits=32):
        if n < 0:
            n = (1 << bits) + n#Compute two's complement for negative numbers
        return format(n, f'0{bits}b')# Format as binary with leading zeros
    
    
    def Check_username_valid(Username):# check if username valid 

        if Username == "": # check if the input is embty
            print("You have to write username\n")# instructing message
            return False # meanns not valid
        for i in Username: # loop through username characters
            if i == " ": #check if there is a space
                print("Username must not contain space/s\n")# instucting message 
                return False # Thats means username not valid
            
        return True # after checking all the condtions return true means no condtion achieved
    

    def is_input_intger_number(INPUT): # to check any string input if its float or int. this is for inputs that requires numbers
        lis=["1","2","3","4","5","6","7","8","9","0"] # list of numbers and dot. this used to check if they values in the input if yes that means they are float
        
        for i in INPUT:# loop through characters 
            if i not in lis:# if the character is not in the list
                return False# reuturn false because its means that it could be letters
    
        return True# if nothing is passed as false it will be true which means valid float
    
        
    
    
    def Check_if_password_valid(Password):# This function to check if password valid
        passed=0 # this will increase if the condtion is for valid password condition 
        error=0  # this will increase if the condtion is for non valid password condition
        number_of_digits=len(Password)
        if  number_of_digits <= 16 and number_of_digits >= 8: #check if password between 8 and 16 including  8 and 16
            passed+=1
        
        for i in Password:
            if i == " ":
                error+=1
        if passed == 1 and error == 0: # thats means passed the valid password conditions
            return True
        else: # did not passed the valid password test
            return False
        

    
class data:
    
    Accounts =[ 
        {
            "Username": "Abdulmalik", #  unique username 
            "Password": "12345678",# normal password must be between 8 to 16 characters
            "Balance": "00000000000000000000010100010100",# balance in binary
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,    
            "is_locked_out":False, # is the account locked out or not
            "floats_amount": 0.0 # the change of money like 0.50
        },
        {
            "Username": "Sam112233",
            "Password": "123456789",
            "Balance": "0",
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,
            "is_locked_out":False,# is the account locked out or not
            "floats_amount": 0.0      
        },
        {
            "Username": "mono133",
            "Password": "1q2w3e4r5t",
            "Balance": "0",
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,
            "is_locked_out":False,# is the account locked out or not
            "floats_amount": 0.0
        }
        ]
    

a=Utility.dec_to_2complemnt(1300)
print(a)

