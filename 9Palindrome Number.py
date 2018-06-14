#Palindrome Number
# https://leetcode.com/problems/palindrome-number/description/

# soltion: https://www.youtube.com/watch?v=Yyk3f0lH7VM
class Solution:
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        s = str(x)
        revs = list(reversed(s))
        for i in range(len(s)):
            if s[i] != revs[i]:
                return False
        return True

    def isPalindrome2(self, x):
        """
        :type x: int
        :rtype: bool
        """
        rev=0
        absx = abs(x)
        while absx != 0:
            rev = 10*rev + absx%10
            absx = absx//10
        return rev == x
       
        