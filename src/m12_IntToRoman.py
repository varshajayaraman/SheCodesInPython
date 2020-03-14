class Solution:
    def intToRoman(self, num: int) -> str:
        roman = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]
        decimal = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]

        res = ""
        for r, d in zip(roman, decimal):
            q = num // d
            res += q * r
            num %= d

        return res