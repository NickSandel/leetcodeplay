# Find the Index of the First Occurrence in a String

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0
        elif needle in haystack:
            return haystack.index(needle)
        else:
            return -1

print(Solution().strStr("hello", "ll"))
print(Solution().strStr("aaaaa", "bba"))