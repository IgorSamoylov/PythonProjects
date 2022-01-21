import statistics

def findMedianSortedArrays(nums1, nums2) -> float:
        
       
        list1 = nums1 + nums2

        list1.sort()

        return statistics.median(list1)

print(findMedianSortedArrays([1], []))



def findMedianSortedArraysShort(nums1, nums2) -> float:
        
        return statistics.median(nums1 + nums2)

print(findMedianSortedArraysShort([1,2,3,4,5], [6,7,8,9,10]))


