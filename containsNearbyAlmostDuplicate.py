class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        newNums = [[x, i] for i, x in enumerate(nums)]
        newNums.sort()
        while len(newNums) > 1:
            a = newNums.pop()
            b = 1
            while b <= len(newNums) and newNums[-b][0] + t >= a[0]:
                if abs(newNums[-b][1] - a[1]) <= k:
                    return True
                b += 1
        return False