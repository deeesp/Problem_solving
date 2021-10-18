import sys

input = lambda: sys.stdin.readline()
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  N, M, K = map(int, input().split())
  A = [list(map(int, input().split())) for _ in range(N)]  # NxN 매년 추가 양분 정보
  land = [[5] * N for _ in range(N)]

  trees = [[[] for _ in range(N)] for _ in range(N)]  # M개 나무 정보 (x,y), age
  for _ in range(M):
    x, y, z = map(int, input().split())
    trees[x - 1][y - 1].append(z)
  dead = []
  direction = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
  old = []

  def spring():
    global trees
    for r in range(N):
      for c in range(N):
        if trees[r][c]:
          trees[r][c].sort()
          tmp = []
          for age in trees[r][c]:
            if age <= land[r][c]:  # 나이만큼 양분먹고 나이 1 증가
              land[r][c] -= age
              tmp.append(age+1)
              if age % 5 == 4:
                old.append((age+1, r, c))
            else:  # 양분 < 나이 : 나무 사망
              dead.append((age, r, c))
          trees[r][c] = tmp

  def summer():
    while dead:
      age, r, c, = dead.pop()
      land[r][c] += age // 2

  def fall():
    while old:
      age, r, c = old.pop()
      for dr, dc in direction:
        n_r, n_c = r+dr, c+dc
        if 0 <= n_r < N and 0 <= n_c < N:
          trees[n_r][n_c].append(1)

  def winter():
    for i in range(N):
      for j in range(N):
        land[i][j] += A[i][j]


  for k in range(K):
    spring()
    summer()
    if not trees:
      print(0)
      break
    fall()
    winter()

  answer = 0
  # 살아있는 나무 개수 출력
  for i in range(N):
    for j in range(N):
      answer += len(trees[i][j])
  print(answer)