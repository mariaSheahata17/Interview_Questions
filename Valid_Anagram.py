class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        charList = []
        for char in s:
            charList.append(char)
        for char in t:
            if(char not in charList or len(charList) == 0 ):
                return False
            else:
                charList.remove(char)
        if (len(charList) == 0):
            return True
        return False
        