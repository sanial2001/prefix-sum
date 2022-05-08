class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        sums, even, odd = 0, 0, 0
        ans = 0
        for val in arr:
            sums += val
            ans += 1 if sums % 2 != 0 else 0
            if sums % 2 == 0:
                even += 1
                ans += odd
            else:
                odd += 1
                ans += even
        return ans % (10 ** 9 + 7)
