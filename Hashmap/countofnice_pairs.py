class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(num):
            return int(str(num)[::-1])

        mod = 10**9 + 7
        freq_map = {}
        count = 0

        for num in nums:
            transformed = num - rev(num)

            if transformed in freq_map:
                count = (count + freq_map[transformed]) % mod
                freq_map[transformed] += 1
            else:
                freq_map[transformed] = 1

        return count
