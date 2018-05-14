# coding:utf-8

"""
Given an array of n Intergers, are there elements a, b, c in S such that
a + b + c =0? Find all unique triplets in the array which gives the sum of zero.


Note:
Elements in a triplet (a,b,c) must be in non-descending order. (ie, a ≤ b ≤ c)
The solution set must not contain duplicate triplets.
	For example, given array S = {-1 0 1 2 -1 -4},

	A solution set is:
	(-1, 0, 1)
	(-1, -1, 2)
"""


class Solution(object):
	def threeSum(self, nums):
		"""
        :type nums: List[int]
        :rtype: List[List[int]]
        """
		res = []
		nums.sort()
		for i in range(len(nums) -2):
			if i == 0 or i > 0 and nums[i -1] != nums[i]:
				left = i + 1
				right = len(nums) - 1
				while left < right:
					sum = nums[i] + nums[left] + nums[right]
					if sum == 0:
						res.append([nums[i], nums[left], nums[right]])
						left += 1
						right -= 1
						while left < right and nums[left] == nums[left - 1]:
							left += 1
						while left < right and nums[right] == nums[right + 1]:
							right -= 1
					elif sum  < 0:
						left += 1
					else:
						right -= 1
		return res


