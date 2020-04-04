class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        def check(flowerbed):

            if len(flowerbed) == 1:
                return True
            for i in range(len(flowerbed) - 1):

                if flowerbed[i] == 1 and flowerbed[i + 1] == 1:
                    return False

            return True

        if n == 0:
            return True
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0:
                if i == 0:
                    if len(flowerbed) > 1 and flowerbed[1] == 0:
                        flowerbed[0] = 1
                        n -= 1
                    elif len(flowerbed) == 1:
                        flowerbed[i] = 1
                        n -= 1
                else:
                    if i == len(flowerbed) - 1:
                        if flowerbed[i - 1] == 0:
                            flowerbed[i] = 1
                            n -= 1
                    elif flowerbed[i - 1] == 0 and flowerbed[i + 1] == 0:
                        flowerbed[i] = 1
                        n -= 1

            # print(flowerbed, n)
            if n == 0:
                return True
        # print(flowerbed)
        return False