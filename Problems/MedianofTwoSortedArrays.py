class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        

        arry=nums1+nums2
        arry.sort()


        if (len(arry)%2==0):
            s= int (len(arry)/2)
            med=(arry[s]+arry[s-1])/2

        else:
            s= int ((len(arry))/2)
            med=arry[s]
         
        return float(med)

        