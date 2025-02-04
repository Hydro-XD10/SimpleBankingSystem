class Utility:    
    def Check_username_valid(Username):
        for i in Username:
            if i == " ":
                return False
            
        return True
        
    
    def check_if_input_is_numbers(INPUT): # to check any input if its numbers or not. this is for inputs that requires numbers
        list_of_numbers=[1,2,3,4,5,6,7,8,9,0]
        for i in INPUT:
            if i :
    
    
    
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
            "Username": "Abdulmalik", #
            "Password": 12345678,
            "Balance": "0",
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,
            "is_locked_out":False # is the account locked out or not
        },
        {
            "Username": "Sam112233",
            "Password": 123456789,
            "Balance": "0",
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,
            "is_locked_out":False# is the account locked out or not
        },
        {
            "Username": "mono133",
            "Password": "1q2w3e4r5t",
            "Balance": "0",
            "Balance_sign": True,#True is positve false is negative
            "Overdraft_Allowance": 1500,
            "is_locked_out":False# is the account locked out or not
        }
        ]
    






