# 5 Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/description/
# https://www.youtube.com/watch?v=bSNhTqzgCq4
# https://www.youtube.com/watch?v=Fi5INvcmDos

# odd string aba
# even string abba
# look for the center of palindro to test odd or even

# dp methond: start and end define substring. look up 2-d table to see if 
# if aba is palendrom, for cabac, just look at A[1][3] and test one befor and after

class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = (0,None)
        dp = [[0]* len(s)]*len(s)   # initialize dp table as all substring not palindrome
        # print(dp)
        # find odd palindrome
        for i in range(len(s)):
            # print('a')
            print(dp[i][i])
            dp[i][i]= 1 
            
            print(dp)
            if 1>res[0]:           # every element is palindrome
                res = (1,s[0])        # if this loop run, we know not empty and res at least 1
            iter = 0
            while i-iter >= 1 and i+iter <= len(s)-1 -1:
                if dp[i-iter][i+iter] == 1 and s[i-iter-1] == s[i+iter+1]:
                    dp[i-iter-1][i+iter+1] = 1
                    iter += 1
                else:
                    if 2*iter+1 > res[0]:
                        # print(i-iter,i+iter)
                        res = (2*iter+1, s[i-iter:i+iter+1])
                    
                    break
               
        # find odd palindrome
        
        for start in range(len(s)-1):
            if s[start] == s[start+1]:
                dp[start][start+1] = 1
                if 2>res[0]:
                    
                    res = (2,s[start:start+1 +1])
            iter = 0
            while start-iter >= 1 and (start+1)+iter <= (len(s)-1) -1:
                if dp[start-iter][(start+1)+iter] == 1 and s[start-iter-1] == s[(start+1)+iter+1]:
                    dp[start-iter-1][(start+1)+iter+1] =1
                    iter += 1
                else:
                    if 2*iter+2 > res[0]:
                      
                        res = (2*iter+2,s[start-iter : (start+1)+iter +1])
                
                    break
                    # res = max(res, 2*iter+2)
           
        # print(dp)
        return res

# or use len = 1 and 2 as base case first      
if __name__ == '__main__':
    s = "abc"
    print(Solution().longestPalindrome(s))
        