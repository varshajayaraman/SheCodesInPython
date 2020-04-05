class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        num = numerator
        den = denominator

        ans = []
        ind = 0
        if num < 0 and den < 0:
            num = -num
            den = -den

        elif num < 0 or den < 0:
            if num < 0:
                num = -num
            else:
                den = -den
            ans.append('-')
            ind += 1
        if num == 0 or den == 0:
            return "0"

        ans.append(str(int(num / den)))
        if num < 0:
            num = -num
        rem = num % den
        if rem == 0:
            return "".join(ans)
        hmap = {}
        ans.append('.')
        ind += 2
        while rem != 0 and hmap.get(rem) is None:
            hmap[rem] = ind
            ind += 1
            rem *= 10
            q = int(rem / den)
            ans.append(str(q))
            rem = rem % den

        if rem == 0:
            return "".join(ans)
        ans.append(")")
        ans.insert(hmap[rem], "(")
        return "".join(ans)


