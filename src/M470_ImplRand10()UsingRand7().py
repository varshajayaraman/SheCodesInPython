# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        idx = 100
        while idx > 40:
            row = rand7()
            col = rand7()

            idx = (row - 1) * 7 + col  # 5,6

        return (idx % 10) + 1