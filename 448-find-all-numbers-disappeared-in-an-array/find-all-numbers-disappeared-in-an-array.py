class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        list = []
        n = len(nums)
        seen = set(nums)
        for i in range(1,n+1):
            if i not in seen:
                list.append(i)
       
        return list