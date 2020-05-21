class Solution:
def isValid(self, s: str) -> bool:
    stack = []
    if (len(s) % 2 != 0):
        return False
    for string in s:
        if (string == "(" or string == "[" or string == "{") :
            stack.append(string)
        else:
            if (len(stack) != 0):
                openBracket = stack.pop()
                if ((openBracket  == "(" and string != ")") or
                   (openBracket  == "[" and string != "]") or
                   (openBracket  == "{" and string != "}")):
                    return False
    if (len(stack) != 0):
        return False
    return True
               
                
            
         
