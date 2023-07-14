class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = nums1 + nums2
        merged.sort()
        print(merged)
        if len(merged) % 2 == 1:
            return float(merged[len(merged)/2])
        else:
            return (float((merged[len(merged)/2 - 1]) + float(merged[len(merged)/2]))/2)
