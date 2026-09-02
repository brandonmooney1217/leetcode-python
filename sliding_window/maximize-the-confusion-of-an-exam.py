class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        """

        T T F F F,  k = 1
        """
        res = 0
        t_count, f_count = 0, 0
        left = 0

        for i in range(len(answerKey)):
            char = answerKey[i]
            if char == "T":
                t_count +=1
            else:
                f_count +=1

            max_char = max(t_count, f_count)
            while (i-left+1) > max_char + k:
                left_char = answerKey[left]
                if left_char == "T":
                    t_count -=1
                else:
                    f_count -=1
                max_char = max(t_count, f_count)
                left +=1
            res = max(res, (i-left+1))
            print(i, res)
        return res


        """
        T T F T T T T T F T k = 1
        """
