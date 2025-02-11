class Solution:
    def lexicographicallySmallestArray(self, nums: list[int], limit: int) -> list[int]:
        n = len(nums)

        # Create a copy of key, value of nums into an array of tuples
        t_nums = sorted((num, i) for i, num in enumerate(nums))

        new_positions = []
        curr_positions = []
        prev = float('-inf')

        for num, idx in t_nums:
            if num > prev + limit:
                new_positions.extend(sorted(curr_positions))
                curr_positions = [idx]
            else:
                curr_positions.append(idx)
            prev = num
        
        new_positions.extend(sorted(curr_positions))

        res = [0] * n
        for i, nidx in enumerate(new_positions):
            res[nidx] = t_nums[i][0]
        
        return res
    

algo = Solution()
# answer = algo.lexicographicallySmallestArray([1,5,3,9,8], 2)
# print(answer)

answer = algo.lexicographicallySmallestArray([1,7,6,18,2,1], 3)
print(answer)