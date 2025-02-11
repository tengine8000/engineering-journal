def fib(n, portion, memo = {}):
    print(f"Visiting Node -> {n} on {portion} of tree..")
    if n == 0 or n == 1:
        print("We hit base case", n)
        return 1
    if n in memo:
        print(f"-> -> Hey! We visited Node -> {n} sometime ago.")
        return memo[n]
    
    left = fib(n-2, "left", memo)
    print("Back to root -> ",n)
    right = fib(n-1, "right", memo)
    memo[n] = left + right
    return memo[n]

# print(fib(10,"root"))

def permutations(arr):
    n = len(arr)
    
    ans, sol = [], []
    
    
    def dfs():
        print(" Current Sol Array -> ", sol)
        if len(sol) == n:
            print(f"Reached Base Case => Current Array -> {sol}")
            ans.append(sol[:])
            return

        for x in arr:
            if x not in sol:
                sol.append(x)
                print("Appending -> ", x," Go down .. ")
                dfs()
                print("Pop out -> ", sol.pop()," Back to root ^^ ")
            
    dfs()
    return ans

print(permutations([1,2,3]))