
def findMedianSortedArrays(nums1, nums2) -> float:
        
       
        list1 = sorted(nums1 + nums2)

        if len(list1) == 1:
            list1.extend(list1 * 3)
        

        if len(list1) % 2 != 0:  
            return list1[int(len(list1) / 2)]
        
        while len(list1) > 2:
            list1.pop(0)
            list1.pop(len(list1) - 1)
            
        return (list1[0] + list1[1]) / 2


print(findMedianSortedArrays([1], []))
