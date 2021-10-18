import sys
from copy import deepcopy

# sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline()

# T = int(input())
# for test_case in range(1, T + 1):
N = int(input())  # 1~20
curves = [list(map(int, input().split())) for _ in range(N)] # x,y,d,g
# x, y : 시작점 0~100, d : 시작 방향 0~3, g : 세대 0~10
# K세대 : K-1세대 드래곤 커브 90도 시계빵향 회전, 끝에 붙임

visited = [[False] * 101 for _ in range(101)]
direction = [(0,1), (-1,0), (0,-1), (1,0)]
max_gen = max(max([curve[-1] for curve in curves]), 1)

generation = {0: [0],
             1: [0, 1]}

# 그냥 구현하자
def gen_gen(k):
  k_gen = deepcopy(generation[k-1])
  front, back = k_gen[:len(k_gen)//2], k_gen[len(k_gen)//2:]
  k_gen.extend([(x+2)%4 for x in front])
  k_gen.extend(back)
  generation[k] = k_gen

if max_gen>1:
  for k in range(2, max_gen+1):
    gen_gen(k)

def move(x,y,d,g):
  n_y, n_x, dir_idx = y, x, d
  visited[n_y][n_x] = True
  for dir in generation[g]:
    dir_idx = (dir+d)%4  #방향 컨트롤
    dy, dx = direction[dir_idx]
    n_y, n_x = n_y+dy, n_x+dx
    visited[n_y][n_x] = True
  return n_y, n_x, dir_idx

# 드래곤커브 지나간곳 체크
for x, y, d, g in curves:
  n_x, n_y, n_d = move(x, y, d, g)

answer = 0
for i in range(100):
  for j in range(100):
    if visited[i][j] and visited[i][j + 1] and visited[i + 1][j] and visited[i + 1][j + 1]:
      answer += 1

print(answer)
