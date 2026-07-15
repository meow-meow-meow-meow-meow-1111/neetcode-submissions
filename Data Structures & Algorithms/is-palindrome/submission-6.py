class Solution:
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        isalnum = str.isalnum
        lower = str.lower
        
        while left < right:
            while left < right and not isalnum(s[left]):
                left += 1
            while left < right and not isalnum(s[right]):
                right -= 1
                
            if lower(s[left]) != lower(s[right]):
                return False
                
            left += 1
            right -= 1
            
        return True