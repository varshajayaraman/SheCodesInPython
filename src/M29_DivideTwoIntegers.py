class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        odividend = dividend
        odivisor = divisor
        if dividend < 0:
            dividend = -dividend
        if divisor < 0:
            divisor = -divisor
        if dividend < divisor:
            return 0

        def func(dividend, divisor):
            count = 1
            tot = 0
            while dividend >= divisor:
                # print(dividend, divisor)
                dividend -= divisor
                tot += count

                if dividend >= (divisor + divisor):
                    divisor += divisor
                    count += count
            return tot, dividend

        gtot = 0

        while dividend >= divisor:
            # print("Sendin:", dividend)
            t, dividend = func(dividend, divisor)
            # print("Rteurns:",dividend, t)
            gtot += t

        # print(odividend, odivisor)
        if (odividend < 0 and odivisor < 0) or (odividend > 0 and odivisor > 0):
            gtot = min(gtot, pow(2, 31) - 1)
            return gtot
        if odividend < 0:
            return -gtot
        gtot = min(gtot, pow(2, 31) - 1)
        return -gtot