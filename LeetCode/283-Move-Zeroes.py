class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        index = 0
        for i in range(len(nums)):
            if (nums[index] == 0):
                nums.append(0)
                nums.remove(0)
            else:
                index +=1
        print(nums)
            