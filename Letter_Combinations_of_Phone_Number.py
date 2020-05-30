class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        result = []
        if digits == None or len(digits)== 0 :
            return result
        dictionary = {"2":["a","b","c"],
                     "3":["d","e","f"],
                     "4":["g","h","i"],
                     "5":["j","k","l"],
                     "6":["m","n","o"],
                     "7":["p","q","r","s"],
                     "8":["t","u","v"],
                     "9":["w", "x","y","z"]}        
        
        currentString = ""
        # call the recursive function 
        self.letterCombinationsRecursive(result, currentString, 0 , digits, dictionary)
        return result
        
    def letterCombinationsRecursive(self, result: List[str], currentString: str, index: int, digits: str, dictionary ):
        if index == len(digits):
            result.append(currentString)
            return

        digit =  digits[index]     
        for letter in dictionary[digit]:
                self.letterCombinationsRecursive(result,currentString +letter , index +1, digits , dictionary )
                    
            
        