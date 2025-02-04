class Utility:    
    def Check_username_valid(Username):# check if username valid 
        if Username == "": # check if the input is embty
            print("You have to write username\n")# instructing message
            return False # meanns not availible
        for i in Username: # loop through username characters
            if i == " ": #check if there is a space
                print("Username must not contain space/s\n")# instucting message 
                return False # Thats means username not availible
            
        return True # after checking all the condtions return true
    

    def is_input_float(INPUT): # to check any string input if its float or int. this is for inputs that requires numbers
        lis=["1","2","3","4","5","6","7","8","9","0","."] # list of numbers and dot. this used to check if they values in the input if yes that means they are float
        dotsCounter=0 # count how dots   
        
        for i in INPUT:# loop through characters 
            if dotsCounter==2: # check if the dots counter already 2
                return False #if dots counter is 2 means not valid input
            if i == ".":# if the character is dot
                dotsCounter+=1 # increase the dots counter
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
        
    def twos_complement_to_decimal(binary_str):
        return int(binary_str, 2)

    def dec_to_2complemnt(number): 
        output=bin(number)
        return(output[2:])
    
class data:
    
    Accounts =[ 
        {
            "Username": "Abdulmalik", #  unique username 
            "Password": 12345678,# normal password must be between 8 to 16 characters
            "Balance": "0",# balance in binary
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,    
            "is_locked_out":False, # is the account locked out or not
            "floats_amount": 0.0 # the change of money like 0.50
        },
        {
            "Username": "Sam112233",
            "Password": 123456789,
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
    





