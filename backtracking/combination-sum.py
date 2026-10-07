class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        res = []
        curr = []
        def f(index, sm):
            if sm == 0:
                res.append(curr[:])
                return
            if index == len(candidates):
                return

            for i in range(index, len(candidates)):
                if candidates[i] <= sm:
                    curr.append(candidates[i])
                    f(i, sm-candidates[i])
                    curr.pop()
        f(0, target)

        return res
