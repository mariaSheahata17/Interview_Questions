class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {"I":1 , "V":5 , "X":10 , "L":50 , "C":100 , "D":500 , "M":1000}
        result = 0
        prev_char = ""
        current_Char = ""
        for char in s:
            prev_char = current_Char
            current_Char = char
            if ((prev_char == "I" and (current_Char == "V" or current_Char == "X")) or 
               (prev_char == "X" and (current_Char == "L" or current_Char == "C")) or 
               (prev_char == "C" and (current_Char == "D"  or current_Char == "M"))) :
                result -= dic[prev_char]
                result += (dic[current_Char] - dic[prev_char])
            else:
                result +=  dic[current_Char]

        return result
