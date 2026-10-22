class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        A A A B A B B B B
        k = 1

        answer = 6
        """
        res = 0
        tmp = [0] * 26
        l = 0

        for r in range(len(s)):
            curr_char = s[r]
            curr_char_index = ord(curr_char) - ord("A")
            tmp[curr_char_index] +=1

            mx = max(tmp)

            while (r-l+1) > mx + k:
                left_index = ord(s[l])-ord("A")
                tmp[left_index]-=1
                l+=1
                mx = max(tmp)
            res = max(res, r-l+1)

        return res
