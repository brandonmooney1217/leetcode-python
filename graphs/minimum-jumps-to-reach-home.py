class Solution:
    def minimumJumps(self, forbidden: list[int], a: int, b: int, x: int) -> int:
        """
        problem
            start at pos 0
            home is at index x
            can move right a
            can move left b, but cannot do this 2x in a row

            cannot move to forbidden pos

        impl
            - recursive approach with state (index, moveBack?)
            - need to keep track of seen to avoid cycles in graph and inf loop
            - put forbidden in set for constant time look ups
            - base case is index == x
            - can alway move right
                if we are past home, then dont move right
            - cant move left twice in a row, also cannot go negative


        """
        tmp = set(forbidden)
        seen = set()

        def f(index, back):
            if index == x:
                return 0

            if (index,back) in seen:
                return float('inf')

            res = float('inf')
            seen.add((index, back))

            # cannot go to forbidden index
            if index not in tmp:
                if index + a <= 6000:
                    res = min(res, f(index + a, False) + 1)

                # move left if index >= 0 (cant go neg) and
                if (index - b) >= 0 and not back:
                    res = min(res, f(index-b, True) + 1)

            return res

        t = f(0, False)
        return t if t!= float('inf') else -1
