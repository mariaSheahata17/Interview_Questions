class Solution:
    def isPalindrome(self, s: str) -> bool:
        charList = []
        for char in s:
            if(char.isalnum()):
                charList.append(char.lower())
        size = len(charList) -1
        print(charList)
        for i in range(len(charList)//2):
            if(charList[i] != charList[size -i]):
                return False
        return True
        