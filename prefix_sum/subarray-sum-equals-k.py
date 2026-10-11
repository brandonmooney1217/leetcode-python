class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]

        for num in nums:
            prefix.append(num + prefix[-1])

        dct = {0:1}
        res = 0
        for i in range(1, len(prefix)):
            num = prefix[i]
            if (num-k) in dct:
                res += dct[num-k]
            if num not in dct:
                dct[num] = 0
            dct[num] +=1
        return res


        """
        -2, 2, 0, 4, -4 k = 0

        -2 0 0 4 0

        seen = {0, -2, }

        (-2, 2) (-2, 2, 0)
        (0)
        (0, 4, -4)
        (4, -4)

        k = 0
        """
