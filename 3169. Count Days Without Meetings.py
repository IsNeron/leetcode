from typing import List


class Solution:
    def countDays(self, days: int, meetings: List[List[int]]) -> int:
        free_days = 0
        latest_end = 0

        meetings.sort()

        for start, end in meetings:
            if start > latest_end + 1:
                free_days += start - latest_end - 1
            latest_end = max(latest_end, end)

        free_days += days - latest_end

        return free_days





a = Solution()
print(a.countDays(10, [[5,7],[1,3],[9,10]])) #2
print(a.countDays(5, [[2,4],[1,3]])) #1
print(a.countDays(6,[[1,6]])) #0