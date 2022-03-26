"""
Given an integer x, return true if x is palindrome integer.
An integer is a palindrome when it reads the same backward as forward.
For example, 121 is a palindrome while 123 is not.
"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        
        int2str = str(x) 
        
        for i in range  (len(int2str)) :
            if ( int2str[i] != int2str[len(int2str) - i-1]):
                return False 
        return True 