class Solution:
    #calculate the biggest area
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        start = 0 
        end = len(height) -1 
        prev_start = 0
        prev_end = 0
        while start != end:
                
            maxArea = max( min( height[start], height[end]) * (end - start) , maxArea )
            if(height[start] < height[end]):
                prev_start = height[start]
                start +=1
            else:
                prev_end = height[end]
                end -=1
        return maxArea
 