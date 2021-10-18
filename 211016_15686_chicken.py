import sys
from itertools import combinations

sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline()

T = int(input())
for test_case in range(1, T + 1):
  n, m = map(int, input().split())
  city = [list(map(int, input().split())) for _ in range(n)]
  home = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 1]
  chicken = [(i, j) for i in range(n) for j in range(n) if city[i][j] == 2]
  ans = 99999  ## 무한대 값 설정

  for c in combinations(chicken, m):  # 치킨집 조합
    s = 0
    for hx, hy in home:
      d = 99999
      for cx, cy in c:
        d = min(d, abs(hx - cx) + abs(hy - cy))
      s += d
    ans = min(ans, s)

  print(ans)