class Solution:
    def solve(self, stacks):
        if not stacks:
            return 0

        pre, sums = set(), 0
        for i in stacks[0]:
            sums += i
            pre.add(sums)

        for stack in stacks[1:]:
            sums, new_pre = 0, set()
            for i in stack:
                sums += i
                new_pre.add(sums)
            pre = pre.intersection(new_pre)

        # print(pre)
        return max(pre) if pre else 0
