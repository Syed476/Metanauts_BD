class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) < 3:
            return []
        nums.sort()
        ret_val = []
        for i in range(len(nums) - 2):
             if i - 1 >= 0 and nums[i - 1] == nums[i]:
				continue
            j = i + 1
            k = len(nums) - 1
            # This is our target sum
            target = -nums[i]            
            while j < k:
                if j - 1 != i and nums[j - 1] == nums[j]:
                    while nums[j - 1] == nums[j] and j < k:
                        j += 1
                elif k + 1 != len(nums) and nums[k + 1] == nums[k]:
                    while nums[k + 1] == nums[k] and j < k:
                        k -= 1
                else:
                    if nums[j] + nums[k] == target:
                        ret_val.append([nums[i], nums[j], nums[k]])
                        j += 1
                        k -= 1
                    elif nums[j] + nums[k] < target:
                        j += 1
                    else:
                        k -= 1
        return ret_val