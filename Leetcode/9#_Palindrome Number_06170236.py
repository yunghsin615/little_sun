class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 :
            return False
        a = str(abs(x))
        b = a[::-1]
        if a == b:
            return True
        else:
            return False
