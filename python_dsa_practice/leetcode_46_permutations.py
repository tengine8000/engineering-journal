def permutations(nums = []):
    n = len(nums)
    ans, sol = [], []
    
    def backtrack():
        if len(sol) == n:
            ans.append(sol[:])
            print("sol -> ", sol)
            return
        
        for num in nums:
            if num not in sol:
                print('current sol before append', sol)
                sol.append(num)
                backtrack()
                sol.pop()
    
    backtrack()
    return ans

for p in permutations([1,2,3,4]):
    print(p, sep="\n")