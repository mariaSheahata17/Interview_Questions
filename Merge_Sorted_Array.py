"""
fix infinit loop problem in my solution
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        j = 0
        nums1_Size = len(nums1)
        print(nums1_Size)
        for i in range(nums1_Size):
            while j < n :
                if (nums1[i] >= nums2[i]):
                    self.pushBackward(i, nums1, m)
                    nums1[i] = nums2[j]
                    m +=1
                    j +=1
        
     # pushes back all elements by one position starting from index i   
    def pushBackward(self, i : int, array: List[int], size: int) -> None:            
            index = size-1
            while index >= i:
                array[index + 1] = array[index]
                index -=1
            
"""
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        while m > 0 and n > 0:
            if (nums1[m-1] > nums2[n-1]):
                nums1[m+n-1] = nums1[m-1]
                m-=1
            else:
                nums1[m+n-1] = nums2[n-1]
                n-=1
            
        if n > 0:
            nums1[:n] = nums2[:n]
        
