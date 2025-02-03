class Utility:


    def twos_complement_to_decimal(binary_str):
        return int(binary_str, 2)

    def dec_to_2complemnt(number): 
        output=bin(number)
        return(output[2:])