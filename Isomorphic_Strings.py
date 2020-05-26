class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        dictionary = {}
        reserved = []
        for i in range(len(s)):
                if (s[i] not in dictionary and t[i] in reserved):
                    return False
                if (s[i] not in dictionary):
                    dictionary[s[i]] = t[i]
                    reserved.append(t[i])
                else:
                    if(dictionary[s[i]] != t[i]):
                        return False
                    
        return True
        