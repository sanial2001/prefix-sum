class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        n = len(nums)
        even, odd = [], []
        evensum, oddsum = 0, 0

        for i, num in enumerate(nums):
            if i % 2 == 0:
                evensum += num
            else:
                oddsum += num
            even.append(evensum)
            odd.append(oddsum)

        # print(even,odd)

        ans = 0
        for i in range(n):
            if i == 0:
                evensum = odd[n - 1] - odd[i]
                oddsum = even[n - 1] - even[i]
                ans += 1 if evensum == oddsum else 0
            else:
                evensum = even[i - 1] + (odd[n - 1] - odd[i])
                oddsum = odd[i - 1] + (even[n - 1] - even[i])
                ans += 1 if evensum == oddsum else 0

        return ans
