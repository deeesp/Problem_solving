class itertool():

    def __init__(self,arr,k):
        super(itertool, self).__init__()
        self.arr = sorted(arr)
        self.n = len(self.arr)
        self.k = k

    def nPk(self):
        used = [False]*len(self.arr)
        ans = []

        def dfs(depth, used, curr):
            if depth == self.k:  # end condition
                ans.append(curr[::]) # use deepcopy because curr is tracking all partial solution, it eventually become []
                return

            for i in range(self.n):
                if not used[i]:
                    curr.append(self.arr[i]) # generate the next solution from curr
                    used[i] = True
                    dfs(depth + 1, used, curr) # move to the next solution
                    used[i] = False
                    curr.pop()  # backtrack to previous partial state
            return

        dfs(0, used, [])

        return ans

    def nCk(self):
        ans = []

        def dfs(depth, start, curr):
            if depth == self.k:
                ans.append(curr[::])
                return

            for i in range(start, self.n):
                curr.append(self.arr[i]) # generate the next solution from curr
                dfs(depth + 1, i + 1, curr) # move to the next solution
                curr.pop()  # backtrack to previous partial state
            return

        dfs(0, 0, [])
        return ans


arr = [1,2,3,4,5]
k = 3
I = itertool(arr,k)

print("permutation")
print(I.nPk())
print("combination")
print(I.nCk())
