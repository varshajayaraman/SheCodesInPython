class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        p1=0
        p2=0
        l1 = len(nums1)
        l2 = len(nums2)
        l=l1+l2
        mid = (l1+l2)//2
        c = 0
        ele1 = 0
        ele2 = 0
        while c<mid+1 and (p1<l1 or p2<l2):
            if p1<l1 and p2<l2:
                if nums1[p1]<nums2[p2]:
                    if c+1==mid and l%2==0:
                        ele1=nums1[p1]
                    if c==mid:
                        ele2=nums1[p1]
                    p1+=1
                else:
                    if c+1==mid and l%2==0:
                        ele1=nums2[p2]
                    if c==mid:
                        ele2=nums2[p2]
                    p2+=1
            elif p1<l1:
                if c+1==mid and l%2==0:
                    ele1=nums1[p1]
                if c==mid:
                    ele2=nums1[p1]
                p1+=1
            else:
                if c+1==mid and l%2==0:
                    ele1=nums2[p2]
                if c==mid:
                        ele2=nums2[p2]
                p2+=1
            c+=1
        print(ele1, ele2)
        # if mid==0:
        #     return ele2
        if l%2==0:
            return (ele1+ele2)/2
        return ele2