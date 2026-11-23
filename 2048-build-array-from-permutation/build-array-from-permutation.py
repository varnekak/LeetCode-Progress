class Solution(object):
    def buildArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list =[]
        n = len(nums)
        for i in range (n):   
            list.append(nums[nums[i]])
        return list