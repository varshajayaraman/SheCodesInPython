class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        res=[]
        for x in range(len(cost)):
            if x==0 or x==1:
                res.append(0)
            else:
                val = min(res[x-2]+cost[x-2], res[x-1]+cost[x-1])
                res.append(val)
            # print(res)
        leng = len(cost)-1
        ans = min(res[leng-1]+cost[leng-1], res[leng]+cost[leng])
        return ans
