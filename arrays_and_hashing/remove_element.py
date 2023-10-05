class Solution:
    def removeElement(self, nums: list, val: int) -> int:
        k = 0
        for i in range(len(nums)-1):
            if nums[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
print(Solution().removeElement([3,2,2,3,2,3], 3))