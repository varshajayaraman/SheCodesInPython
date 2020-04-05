class Solution:
    def mySqrt(self, x: int) -> int:

        def sq(x, l, h, up):
            print(l, h)
            if l < h:
                m = (l + h) // 2
                print(m)
                val = m * m
                if val == x or m == up:
                    return int(m)
                if val < x:
                    if val > (up * up):
                        up = m
                    return sq(x, m, h, up)
                else:
                    return sq(x, l, m, up)
            return int(up)

        if x == 0 or x == 1:
            return x
        return sq(x, 0, x, 0)