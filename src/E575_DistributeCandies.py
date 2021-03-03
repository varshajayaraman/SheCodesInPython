class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        c = set(candyType)
        maxEat = len(candyType)//2
        var = len(c)
        if var<=maxEat:
            return var
        return maxEat