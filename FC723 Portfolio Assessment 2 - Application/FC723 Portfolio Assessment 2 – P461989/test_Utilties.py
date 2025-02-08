import unittest
import Utilties as Ut

#this will be used in testig the function. 
account = {
        "Username": "Abdulmalik", #  unique username 
        "Password": "12345678",# normal password must be between 8 to 16 characters
        "Balance": "00000000000000000000010100010100",# balance in binary
        "Balance_sign": True,#True is positve false is negative
        "Overdraft_Allowance": 1500,    
        "is_locked_out":False, # is the account locked out or not
        "floats_amount": 0.0 # the change of money like 0.50
    }
#========================================================================================================
#========================================================================================================
def test_is_balance_sufficient():# function checks if the balance is enough to take a specific amount of money from it
    assert Ut.Utility.is_balance_sufficient(account, 1300) == True,"The number must be less than or equal 1300(The Balance of the account) to be TRUE."# check if the function can recognize when the amount of money needed is the same amount at the balance
    assert Ut.Utility.is_balance_sufficient(account, 1000) == True, "The number must be less than or equal 1300(The Balance of the account) to be TRUE." # test if the function can recognize if the balance has more money than the amount wanted
    assert Ut.Utility.is_balance_sufficient(account, 2000) == False, "The number must be Greater than 1300(The Balance of the account) to be FALSE"# test if the function can recognize if the balance is less that the money wanted


def test_twos_complement_to_decimal():# function convert from binary to decimal
    #test if the function can convert from two complements to deciaml after we pass a negative number and a positive number
    assert Ut.Utility.twos_complement_to_decimal("00000000000000000000010100010100") == 1300, "The Binary number passed does not equal the same number provided in deciaml"#test if the function can convert from binary twos complement to decimal(1300) and get the correct valu
    assert Ut.Utility.twos_complement_to_decimal("11111111111111111111101011101100") == -1300, "The Binary number passed does not equal the same number provided in deciaml"# test if the function also get the right value
    

def test_dec_to_2complemnt():#function convert from dec to two complement's value
    #
    assert Ut.Utility.dec_to_2complemnt(1300) == '00000000000000000000010100010100', "The Value passed in decimal does not equal the valu given in binary"#check if the function can convert 1300 (positive number)
    assert Ut.Utility.dec_to_2complemnt(-1300) == '11111111111111111111101011101100', "The Value passed in decimal does not equal the valu given in binary"  #check if the function can convert -1300 (negative value)


def test_Check_username_valid():
    assert Ut.Utility.Check_username_valid("Normal_Name") == True,"The name to be valid need to does not have spaces and not be embty value"# This will test if name valid the function will return True
    assert Ut.Utility.Check_username_valid("Name has_Space") == False,"The name given must be not valid"# this will test if the name has spaces the function will return False
    assert Ut.Utility.Check_username_valid("") == False, "The name to be valid need to does not have spaces and must not be embty value "# this will test if embty value given, the function must return Flase when this is the case


def test_is_input_intger_number():
    assert Ut.Utility.is_input_intger_number("12345") == True,"The Number given must be True"# test if we give the function string number would know that this is a Valid intger number
    assert Ut.Utility.is_input_intger_number("123a45") == False,"The number given must be False"# test if the function will recognize the letter in the number
    assert Ut.Utility.is_input_intger_number("123 45") == False,"The number given must be False"# test if the function will recognize the space in the strin number

def test_Check_if_password_valid():
    assert Ut.Utility.Check_if_password_valid("ValidPass123") == True,"The password given must be Valid"#test if the function will recogonize the valid password given
    assert Ut.Utility.Check_if_password_valid("short12") == False,"The password given is false"# test if the function will recognize if the password short (Valid password is from 8 to 16 characters)
    assert Ut.Utility.Check_if_password_valid("thispasswordiswaytoolong") == False, "The password given is not valid function must return False"# this
    assert Ut.Utility.Check_if_password_valid("pass word") == False,"This password given is too long the function must return False"#test if the function can recognize if too long password given(Valid password is from 8 to 16 characters)
#=====================================================================================================================
#=====================================================================================================================