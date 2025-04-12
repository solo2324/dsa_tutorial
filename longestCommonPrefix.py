class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        shortest = strs[0]
        for word in strs:
            if len(word) < len(shortest):
                shortest = word
        res=""
        for i in range(len(shortest)):
            for word in strs:
                if ( i == len(word)) or (word[i] != strs[0][i]):
                    return res
            
            res += word[i]    
        return res
