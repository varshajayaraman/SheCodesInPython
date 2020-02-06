class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        hmap = {}
        count = 0

        for t in time:
            curr_t = (t % 60)
            # print(hmap, curr_t)
            if curr_t in hmap:
                count += hmap[curr_t]
                # hmap[curr_t] +=1

            curr_r = (60 - t % 60) % 60

            if curr_r in hmap:
                hmap[curr_r] += 1
            else:
                hmap[curr_r] = 1
        return count