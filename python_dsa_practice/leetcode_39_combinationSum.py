def combinationSum(nums = [], target = 0) -> list[list[int]]:
    res, sol = [], []
    n = len(nums)
    
    def backtrack(i, cur_sum):
        if cur_sum == target:
            res.append(sol[:])
            return
            
        if cur_sum > target or i == n:
            return
        
        backtrack(i+1, cur_sum)
        
        sol.append(nums[i])
        backtrack(i, cur_sum+nums[i])
        sol.pop()
        
    backtrack(0,0)
    return res

for c in combinationSum([2,3,4], 11):
    print(c, sep="\n")
            