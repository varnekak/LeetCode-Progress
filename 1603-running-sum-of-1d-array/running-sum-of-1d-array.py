class Solution(object):
    def runningSum(self, nums):
        list =[]
        total = 0
        for i in nums:
            total+= i
            list.append(total)
        return list