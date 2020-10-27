class Solution:
    def numTeams(self, rating: List[int]) -> int:
        count = 0
        lesser=0
        higher=0
        for i in range(1,len(rating)):
            lesser=0
            higher=0
            lesser_reverse=0
            higher_reverse=0
            for j in range(i):
                if rating[j]<rating[i]:
                    lesser +=1 
                elif rating[j]>rating[i]:
                    higher_reverse += 1
            for j in range(i+1, len(rating)):
                if rating[j]>rating[i]:
                    higher += 1
                elif rating[j]<rating[i]:
                    lesser_reverse += 1
            count += (lesser*higher)
            count += (lesser_reverse*higher_reverse)
            # print(lesser, higher, lesser_reverse, higher_reverse)
        return count