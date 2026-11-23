class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        
        list =[]
        for i in range(n):
            count =0
            for j in range(n):
                if nums[i]>nums[j]:
                    count+=1
            list.append(count)
        return list
