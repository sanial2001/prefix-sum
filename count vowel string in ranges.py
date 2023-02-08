class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        n = len(words)
        vowels = {'a', 'e', 'i', 'o', 'u'}
        pre = [0 for _ in range(n)]
        if words[0][0] in vowels and words[0][-1] in vowels:
            pre[0] = 1

        for i in range(1, n):
            if words[i][0] in vowels and words[i][-1] in vowels:
                pre[i] = pre[i - 1] + 1
            else:
                pre[i] = pre[i - 1]
        # print(pre)

        res = []
        for l, r in queries:
            start = 0 if l == 0 else pre[l - 1]
            end = pre[r]
            res.append(end - start)

        return res
