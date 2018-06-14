# 7. Reverse Integer
# reversed(seq)
# Return a reverse iterator. seq must be an object which has a __reversed__() method or supports the sequence protocol (the __len__() method and the __getitem__() method with integer arguments starting at 0).

# https://leetcode.com/problems/reverse-integer/description/

# ';'.join(['1',"2"]) return '1;2'

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < -2**31 or x >= 2**31:
            return 0
        else: 
            s = str(x)
            if s[0] == '-':
                rs = list(reversed(s[1:]))
                res ='-'+ ''.join(rs)
                num = int(res)
            else:
                rs = list(reversed(s))
                res = ''.join(rs)
                num = int(res)
                
            if num < -2**31 or num >= 2**31:
                return 0
            else:
                return num 

    def reverse2(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        x_ = abs(x)
        print(x_)
        while x_!=0:
            res = 10*res + x_%10
            x_ = x_//10
        if x_ < -2**31 or x_ >= 2**31 or res < -2**31 or res >= 2**31:
            return 0
        else:
            if x > 0:
                return res
            else:
                return -res

if __name__ == '__main__':
    x = 123
    print(Solution().reverse2(x))
