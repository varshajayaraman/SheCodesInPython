from collections import defaultdict


class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bank = defaultdict(int)
        c5, c10, c20 = 0, 0, 0
        for x in bills:

            if x == 5:
                bank[5] += 1
            if x == 10:
                if bank[5] >= 1:
                    bank[5] -= 1
                    bank[10] += 1
                else:
                    print(x, bank)
                    return False
            else:
                if x == 20:
                    if bank[5] >= 1 and bank[10] >= 1:
                        bank[5] -= 1
                        bank[10] -= 1
                        bank[20] += 1
                    elif bank[5] >= 3:
                        bank[5] -= 3
                        bank[20] += 1

                    # elif bank[10]>=2:
                    #     bank[10]-=2
                    else:
                        print(x, bank)
                        return False
        return True
