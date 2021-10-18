import sys
sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline()

def slope(row, N, L):
  if len(set(row))==1:
    return 1

  flag_slope = [0] * N  # 경사로 설치 유무
  i = 0

  while i < N - 1:
    diff = row[i + 1] - row[i]

    if abs(diff) >= 2:  # 인접 높이 차이 2 이상
      return 0

    elif diff == 0:  # 인접 높이 같으면 slope 설치 x
      i += 1
      continue

    elif diff == -1:  # 2. 현재가 우측보다 1만큼 더 높음
      target = row[i + 1]  # 우측에 경사로, target height
      for k in range(L):
        if i + k + 1 >= N:  # 좌표 바깥 길 x
          return 0
        if flag_slope[i + k + 1]:  # 경사로가 이미 있으면 길 x
          return 0
        if target != row[i + k + 1]:  # 연속된 target 높이 개수가 L만큼 안되면 길 x
          return 0
      flag_slope[i + 1:i + L + 1] = [1] * L  # L개 구역에 경사로 설치 체크
      i += L

    elif diff == 1:  # 2. 우측이 현재보다 1만큼 더 높음
      target = row[i]
      i -= L - 1
      if i < 0: # 좌표 바깥 길 x
        return 0
      for k in range(L):
        if flag_slope[i+k]:  # 경사로 이미 있으면 길 x
          return 0
        if target != row[i+k]:
          return 0
      flag_slope[i:i+L] = [1] * L
      i += L

  return 1

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
  N, L = map(int, input().split())  # input : 2<=N<=100, 1<=L<=N
  grid = [list(map(int, input().split())) for _ in range(N)]  # NxN grid, 1 <= elements <= 10
  grid.extend(list(map(list, zip(*grid))))
  cnt = 0
  for row in grid:  # row roads
    cnt += slope(row, N, L)
  print(cnt)
