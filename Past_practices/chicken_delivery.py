import sys
from itertools import combinations
input = sys.stdin.readline

N, M = map(int, input().split())
city = [list(map(int,input().split())) for _ in range(N)]
ans = 1e9

# 최대 M개 치킨집 골라야 함
# 그럼 각 집과 치킨집 사이 최단거리

home, chicken, v = [], [], []

def init(): # 치킨집 2, 집 1
    for i in range(N):
        for j in range(N):
            if city[i][j] == 1:
                home.append((i+1, j+1))
            elif city[i][j] == 2:
                chicken.append((i+1, j+1))
'''
def solve(idx, depth):
    global ans

    if idx > len(chicken):
        return

    if depth == M: # M개 치킨집 선
        s = 0
        for hx, hy in home:
            d = 1e9
            for j in v:
                cx, cy = chicken[j]
                d = min(d, abs(hx-cx)+abs(hy-cy))
            s += d
        ans = min(ans, s)
        return

    v.append(idx)
    solve(idx+1, depth+1)
    v.pop()
    solve(idx+1, depth)
'''

def combi():
    global ans

    for k in combinations (chicken, M):
        s = 0
        for hx, hy in home:
            d = 1e9
            for j in v:
                cx, cy = k
                d = min(d, abs(hx-cx)+abs(hy-cy))
            s += d
        ans = min(ans, s)


init()
combi()
#solve(0,0)
print(ans)