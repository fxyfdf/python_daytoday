
# hash 思想求两个数之和

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        Hash_dict = {}
        for i in range(len(nums)):
        	Hash_dict[nums[i]] = i
        for i in range(len(nums)):
        	temp = target - nums[i]
        	if temp in Hash_dict & i != Hash_dict[temp]:
        		return [i,Hash_dict[temp]]


