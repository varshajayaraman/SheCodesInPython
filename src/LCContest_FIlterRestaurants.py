class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> \
    List[int]:

        filtered = []
        # print(restaurants[0][1])
        for h in restaurants:
            # print(h)
            if veganFriendly == 1:
                if h[2] == veganFriendly and h[3] <= maxPrice and h[4] <= maxDistance:
                    filtered.append(h)
            else:
                if h[3] <= maxPrice and h[4] <= maxDistance:
                    filtered.append(h)

        print(filtered)
        sorter = lambda x: (x[1], x[0])
        filtered = sorted(filtered, key=sorter, reverse=True)
        res = []
        for x in filtered:
            res.append(x[0])
        return res