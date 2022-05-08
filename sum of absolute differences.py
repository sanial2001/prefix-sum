class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        prefix, suffix = [0 for _ in range(n)], [0 for _ in range(n)]
        prefix[0], suffix[n - 1] = nums[0], nums[n - 1]
        for i in range(1, n):
            prefix[i] = prefix[i - 1] + nums[i]
        for i in range(n - 2, -1, -1):
            suffix[i] = suffix[i + 1] + nums[i]
        # print(prefix, suffix)

        ans = []
        for i in range(n):
            left = 0 if i == 0 else (i) * nums[i] - prefix[i - 1]
            right = 0 if i == n - 1 else suffix[i + 1] - (n - 1 - i) * nums[i]
            ans.append(right + left)

        return ans
