from typing import List


class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        n = len(queries)
        result = []
        color_map = {}
        ball_map = {}

        for i in range(n):
            ball, color = queries[i]

            if ball in ball_map:
                prev_color = ball_map[ball]
                color_map[prev_color] -= 1

                if color_map[prev_color] == 0:
                    del color_map[prev_color]

            ball_map[ball] = color

            color_map[color] = color_map.get(color, 0) + 1

            result.append(len(color_map))

        return result




a = Solution()
print(a.queryResults(4, [[1,4],[2,5],[1,3],[3,4]])) #[1,2,2,3]
print(a.queryResults(4, [[0,1],[1,2],[2,2],[3,4],[4,5]])) #[1,2,2,3,4]