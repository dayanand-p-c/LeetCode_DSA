class Solution(object):
    def containsDuplicate(self, nums):
        real=set()
        for x in nums:
            if x in real:
                return True
            else:
                real.add(x)
        return False
        