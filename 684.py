class Solution:
    def findRedundantConnection(self, edges):
        
        arr = [i for i in range(len(edges) + 1)]
        
        def find(x):
            if x != arr[x]: 
                arr[x] = find(arr[x])
            return arr[x]
        
        def union(x, y):
            arr[find(y)] = find(x)
        
        for a,b in edges:
            if find(a) == find(b): 
                return [a,b]
            else: 
                union(a,b)
        