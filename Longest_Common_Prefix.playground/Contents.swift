/*

1. store the first word in var commonPrefix
2. keep comparing the letters of commomPrefix to each letter in the coming words
3. update commonPrefix based on the common letters with the other words
4. if at any time the commonPrefix became "" return commonPrefix
 
 
 
 class Solution {
     func longestCommonPrefix(_ strs: [String]) -> String {
         var result = ""
         
         guard let firstWord = strs.first, let shortestWordCount = strs.map({$0.count}).min(), shortestWordCount > 0 else {
             return result
             
         }
         
         for (index, char) in firstWord.enumerated() {
             let matchedWords = strs.filter({$0[$0.index($0.startIndex, offsetBy: index)] == char})
             if matchedWords.count == strs.count {
                 result.append(char)
             } else {
                 return result
             }
             if index == shortestWordCount - 1 { return result }
         }
         
         return result
     }
 }

*/
class Solution {
    func longestCommonPrefix(_ strs: [String]) -> String {
        var commomPrefix = strs[0]
        for (wordIndex ,word) in strs.enumerated() {
            for wordLetter in word.enumerated(){
                for (Prefixindex ,prefixLetter) in commomPrefix.enumerated(){
                    if commomPrefix == ""{
                        return commomPrefix
                    }
                    if prefixLetter != wordLetter {
                        if let index = word.index(of: prefixLetter) {
                            let distance = word.distance(from: word.startIndex, to: index)
                            commomPrefix.remove(at: commomPrefix.index(before: distance))
                        }
                        
                    }
                    
                }
            }
        }
        return commomPrefix
    }
        
}
