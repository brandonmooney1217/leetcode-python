class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for num in nums:
            prefix.append(prefix[-1] + (num % 2 == 1))

        count = 0
        dct = collections.defaultdict(int)

        for num in prefix:
            if num-k in dct:
                count += dct[num-k]
            dct[num] +=1
        return count
