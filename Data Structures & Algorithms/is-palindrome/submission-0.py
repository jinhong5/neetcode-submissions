class Solution:
    def isPalindrome(self, s: str) -> bool:

        chars = []

        for c in s:
            if c.isalnum():
                chars.append(c.lower())

        s = ''.join(chars)
            
        left = 0
        right = len(s) - 1

        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True
