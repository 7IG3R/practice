class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1 = len(nums1)-1
        index2 = len(nums2)-1
        for i in range(index2+1):
            if (nums1[index1] == 0):
                nums1[index1] = nums2[index2]
                index1 -=1
                index2 -=1
        nums1.sort()