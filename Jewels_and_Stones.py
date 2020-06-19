class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        if not J or not S:
            return 0
        jwels = list(J)
        counter = 0
        for stone in S:
            if stone in jwels:
                counter += 1
        return counter
        