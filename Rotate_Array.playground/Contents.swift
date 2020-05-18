/*

1.use temp variable for swapping
2. swap i with j , if i == nums.count , then i = 0
*/
class Solution {
    func rotate(_ nums: inout [Int], _ k: Int) {
        for l in 0..<k{
            for i in 0..<nums.count {
                var firstNum = nums.count - 1
                var secondNum = i
            // checking if index out of bounce
                if firstNum == nums.count {
                        firstNum = 0
                }

                if secondNum == nums.count {
                    secondNum = 0

                }

                //print("firstNum", firstNum, "secondNum", secondNum)
                var temp = nums[secondNum]
                nums[secondNum] = nums[firstNum]
                nums[firstNum] = temp
                firstNum += 1
            }
        }
    }
}
