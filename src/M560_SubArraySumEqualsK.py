from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
            count = 0
            sumMap = {0:1}
            sumVal=0
            for i in range(len(nums)):
                sumVal+=nums[i]
                # print(sumVal-k)
                # if sumMap[(sumVal-k)]>0:
                if (sumVal-k) in sumMap.keys():
                    count += sumMap[(sumVal-k)]
                if sumVal in sumMap.keys():
                    sumMap[(sumVal)]+=1
                else:
                    sumMap[sumVal] = 1
            print(sumMap)
            return count