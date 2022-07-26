class Solution:
    # Simple
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     for i in range(len(nums)):
    #         for j in range(i+1,len(nums)):
    #             if(nums[i]+nums[j] == target):
    #                 return i,j
    # Ordered Map
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     omap = {}
    #     for i in range(len(nums)):
    #         omap[i] = nums[i]
    #     mapKeys = list(omap.keys())
    #     mapValues = list(omap.values())
    #     nums.sort()
    #     left = 0
    #     right = len(nums)-1
    #     while(left < right):
    #         if (nums[left] + nums[right] > target):
    #             right -= 1
    #         if (nums[left] + nums[right]< target):
    #             left += 1
    #         if(nums[left] + nums[right] == target):
    #             i = mapKeys[mapValues.index(nums[left])]
    #             j = mapKeys[mapValues.index(nums[right])]
    #             return i,j
    # Unordered Map
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        umap = {}
        for i in range(len(nums)):
            x = target-nums[i]
            try:
                return i,umap[x]
            except:
                umap[nums[i]] = i
            