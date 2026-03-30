# Two sum
# Difficulty: Easy
# https://neetcode.io/problems/two-integer-sum/question?list=neetcode150

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Hash map for storing differences and indexes
        # Keys: difference values, Values: indexes in nums
        # Time: O(n)  Space: O(n)
        hash_map = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in hash_map:
                return [hash_map[diff], i]
            else:
                hash_map[nums[i]] = i

        return []
