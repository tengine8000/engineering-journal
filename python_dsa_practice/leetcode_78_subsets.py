def subsets(nums = []):
    n = len(nums)
    ans, sol = [], []
    
    def backtrack(i, branch):
        # print("->" * i)
        print("=>" * i,f" {branch} of tree, level {i}")
        if i == n:
            ans.append(sol[:])
            return
        # Only 2 children / choices, so need for For loops
        backtrack(i+1, "left")
       
        sol.append(nums[i])
        
        backtrack(i+1, "right")
        sol.pop()
    
    backtrack(0, "root")
    return ans


print(subsets(['A', 'B', 'C']))