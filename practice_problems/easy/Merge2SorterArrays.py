# LeetCode 88. Merge Sorted Array
# Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The arrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        midx = m-1
        nidx = n-1
        ridx = len(nums1)-1
        while nidx > -1 :
            if nums1[midx] < nums2[nidx] and midx > -1:
                nums1[ridx] = nums2[nidx]
                ridx -= 1
                nidx -= 1
            elif nums1[midx] > nums2[nidx] and midx > -1:
                nums1[ridx] = nums1[midx]
                midx -= 1
                ridx -= 1
            else:
                nums1[ridx] = nums2[nidx]
                ridx -= 1
                nidx -= 1
