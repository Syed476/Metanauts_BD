class MedianFinder:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        output_list = []
        while(nums1 and nums2):
            if nums1[0] <= nums2[0]:
                output_list.append(nums1.pop(0))
            else:
                output_list.append(nums2.pop(0))
        while nums1:
            output_list.append(nums1.pop(0))
        while nums2:
            output_list.append(nums2.pop(0))
        mid = len(output_list)//2
        if len(output_list)%2 != 0:
            return(output_list[mid])
        return(float(output_list[mid] + output_list[mid-1])/2)