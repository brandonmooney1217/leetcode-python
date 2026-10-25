class Solution:
    def numRescueBoats(self, people: list[int], limit: int) -> int:
        """
        given list of people weights
        given limit , which is boat weight limit
        each boar can carry at most 2 people
        have inf boats

        return min num of boats


        """
        people.sort()
        count = 0
        l, r = 0, len(people)-1

        while l <= r:
            if people[l] + people[r] <= limit:
                l+=1
                r-=1
            else:
                r-=1

            count +=1

        return count
