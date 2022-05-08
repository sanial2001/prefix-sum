class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        n = len(nums)
        k = sum(nums) - x
        if sum(nums) == x:
            return len(nums)

        d = {0: -1}
        ans, sums = 0, 0
        for i in range(n):
            sums += nums[i]
            if sums - k in d:
                ans = max(ans, i - d[sums - k])
            d[sums] = i

        return -1 if ans == 0 else n - ans
