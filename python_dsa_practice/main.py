import pprint
from collections import defaultdict
from collections import deque



def printHello():
    name = input("What is your name? ")
    print(f"Hello {name}")


# printHello()

n = 8
A = [[0,1], [1,2], [0,3], [3,4], [3,6], [3,7], [4,2], [4,5], [5,2]]
# print("Edge List of A: ", A)
# print("Length of Edge list A: ", len(A))

#Convert to Adjancy Matrix

M = [[0 for i in range(len(A))] for j in range(len(A))]

# print(M)

for r, c in A:
    M[r][c] = 1 
    M[c][r] = 1 # uncomment for undirected graphs
    
# pprint.pprint(M)


# Convert to Adjacency List -- better 
D = defaultdict(list)

for u, v in A:
    D[u].append(v)
    # D[v].append(u) # uncomment for undirected graphs

# pprint.pp(D)

def dfs_recursive(node):
    print(node)
    for nei_node in D[node]:
        if nei_node not in visited:
            visited.add(nei_node)
            dfs_recursive(nei_node)
        
    

def bfs(node):
    q = deque([node])
    
    while q:
        node = q.popleft()
        print(node)
        for nei_node in D[node]:
            if nei_node not in visited:
                visited.add(nei_node)
                q.append(nei_node)
source = 0
visited = set()
# visited.add(source)
# print("BFS Traversal")
# bfs(source)
visited.clear()
# print("DFS Traversal: ") 
# dfs_recursive(source)


def backtrack_solution(arr):
    n = len(arr)
    res, sol = [], []
    
    def backtrack(i):
        # Base case, return result
        if i == n:
            res.append(sol[:])
            return
        
        # Decision 1 branch: Do not pick arr[i] move forward
        backtrack(i+1)
        
        # Decision 2 branch: Pick arr[i] and move forward
        sol.append(arr[i])
        backtrack(i+1)
        
        # Reset temporary solution
        sol.pop()
    
    backtrack(0)
    return res


print(backtrack_solution([1,2,3,4]))

    