class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k=0
        for n in nums:
            if k==0 or n!=nums[k-1]: nums[k],k=n,k+1
        return k
