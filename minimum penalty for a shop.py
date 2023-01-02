class Solution:
    def bestClosingTime(self, s: str) -> int:
        n = len(s)
        pre, suff = [0] * n, [0] * n

        sums = 0
        for i in range(n - 1, -1, -1):
            if s[i] == 'Y':
                sums += 1
            suff[i] = sums

        sums = 0
        for i in range(n):
            if s[i] == 'N':
                sums += 1
            pre[i] = sums

        pre = [0] + pre
        suff = suff + [0]
        res, mn = 0, float("inf")
        for i in range(n + 1):
            if suff[i] + pre[i] < mn:
                mn = suff[i] + pre[i]
                res = i

        # print(res)
        return res
