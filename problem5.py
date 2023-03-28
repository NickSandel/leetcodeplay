class Solution:
    def is_palindrome(self, value):
        if str(value) == str(value)[::-1]:
            return True
        else:
            return False

    def longestPalindrome(self, s: str) -> str:
        # Deal with simplest edge cases first
        if s is None:
            return None
        elif s == "":
            return s
        elif self.is_palindrome(s):
            return s
        else:
            # Now get into the guts of this, iterating through possible combinations starting with longest
            s_length = len(s)
            print(s_length)
            while s_length > 0:
                s_length -= 1
                for r in range(0,len(s)-s_length+1):
                    s_test = s[r:r + s_length]
                    print(s_test)
                    # if self.is_palindrome(s_test):
                    #     return s_test
                    
print(Solution().longestPalindrome("babad"))