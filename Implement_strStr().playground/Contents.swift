
    /*
    
    1.check if needle is empty, and declar var firstIndex=0
    2. check the index of each char  to the first index in the needle
    3. if they match, update firstIndex, and repeat step 2 untill the end of the needle
    
     
     for (index, char) in str.enumerated() {
         print("index = \(index), character = \(char)")
     }
     
    */
   
    
    func strStr(_ haystack: String, _ needle: String) -> Int {
        var firstIndex = 0
        if needle == ""{
            return firstIndex
        }
        if needle.count > haystack.count{
            firstIndex = -1
            return firstIndex
        }
        for (index1, char1) in haystack.enumerated() {
            for (index2 , char2) in needle.enumerated() {
                if char1 != char2 {
                    break
                }
                if index2 == 0 && char1 == char2{
                    firstIndex = index1
                }
                if index2 == needle.count - 1 && char1 == char2{
                    return firstIndex
                }
            }
            
        }
        firstIndex = -1
        return firstIndex
    }

    

