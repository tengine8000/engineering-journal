def combinations(n, k):
    nums = [ i for i in range(1, n+1)]
    print("nums -> ", nums)
    ans, sol, = [], []
    
    def backtrack(x):
        if len(sol) == k:
            ans.append(sol[:])
            return
        
        left = x
        still_need = k - len(sol)
        
        if left > still_need:
            backtrack(x-1)
            
        
        sol.append(x)
        backtrack(x-1)
        sol.pop()
        
        
    backtrack(n)
    return ans

print(combinations(4, 2))
        
        