class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq = [(-1, 0)]
        sums, res = 0, float("inf")
        for i, val in enumerate(nums):
            sums += val
            while dq and sums - dq[0][1] >= k:
                res = min(res, i - dq[0][0])
                dq.pop(0)
            while dq and sums < dq[-1][1]:
                dq.pop()
            dq.append((i, sums))
        return -1 if res == float("inf") else res
