import UIKit

func binarySearch(in arr : [Int], for value : Int)-> Int? {
    var left = 0
    var right = arr.count - 1
    while left <= right {
        let mid = Int(floor(Double(left + right) / 2.0))
        if arr[mid] < value {
            left = mid + 1
        }else if arr[mid] > value {
            right = mid - 1
        }else {
            return mid
        }
    }
    return nil


}

func findNumber(arr: [Int], k: Int) -> String {
    // Write your code here
    var array = arr
    array.sort()
    var returnedNum = binarySearch( in : array, for : k )
    if k != returnedNum {return "NO"}
    return "YES"


}

var num_list : [Int] = []
print("Enter values")
var userInput = readLine()!
var numLines : Int = Int(userInput)!
var num : Int
for _ in 0..<numLines {
    userInput = readLine()!
    num = Int(userInput)!
    num_list.append(num)
}

userInput = readLine()!
num = Int(userInput)!


print(findNumber(arr : num_list, k : num))
