class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(integer) for integer in digits] # Change int to str in list
        s_digits = "".join(s) # Add the list to a full str
        int_digits = int(s_digits) # change type str to int
        int_digits += 1 # sum one 
        return [int(num) for num in str(int_digits)] # return list of int 
        
        
            