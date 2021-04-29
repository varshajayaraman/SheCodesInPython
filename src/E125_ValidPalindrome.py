class Solution:
    def isPalindrome(self, s: str) -> bool:
        i = 0
        j = len(s) - 1
        while i < j:

            while i < j and (s[i] == ' ' or s[i].isalnum() is False):
                i += 1
            while i < j and (s[j] == ' ' or s[j].isalnum() is False):
                j -= 1
            print(i, j)

            if i > j or s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True