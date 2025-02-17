class Solution:
    def dfs(self, tile_counter: dict) -> int:
        combinations_count = 0
        for tile, count in tile_counter.items():
            if count > 0:
                combinations_count += 1

                tile_counter[tile] -= 1
                combinations_count += self.dfs(tile_counter)
                tile_counter[tile] += 1

        return combinations_count


    def make_counter(self, tiles: str):
        counter = {}
        for letter in tiles:
            if letter in counter:
                counter[letter] +=1
            else:
                counter[letter] = 1
        
        return counter


    def numTilePossibilities(self, tiles: str) -> int:
        counter = self.make_counter(tiles)
        return self.dfs(counter)
    


a = Solution()
print(a.numTilePossibilities('AAB')) #8
print(a.numTilePossibilities('AAABBC')) #188
print(a.numTilePossibilities('V')) #1