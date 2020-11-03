class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        
            avg = sum(A)//3
            if sum(A)%3!=0:
                return False
            sumval=0
            count=0
            for i in A:
                sumval += i
                if sumval==avg:
                    count +=1
                    sumval=0
            print(count)
            return count>=3