class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic = {}
        for num in nums:
            if (num not in dic):
                dic[num] = 1
            else:
                dic[num] +=1
            if (dic[num] > len(nums)/2):
                return num
        sorted_Dictionary = sorted(dic.items(), key = lambda x: x[1] , reverse = True)
        return list(dic.keys())[0]
            
