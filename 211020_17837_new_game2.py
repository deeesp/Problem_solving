import sys

input = lambda: sys.stdin.readline()

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  N, K = map(int, input().split())  # 4<=N<=12, 4<=K<=10
  chess = []
  for n in range(N + 2):
    if n == 0 or n == N + 1:
      chess.append([2] * (N + 2))
    else:
      tmp = [2]
      tmp.extend(list(map(int, input().split())))
      tmp.append(2)
      chess.append(tmp)
  pieces = {k: list(map(int, input().split())) for k in range(1, K + 1)}
  dirs = {1: (0, 1), 2: (0, -1), 3: (-1, 0), 4: (1, 0)}
  MAX_TURN = 1000

  state = [[[] for _ in range(N+1)] for _ in range(N + 1)]
  for key in pieces.keys():
    r, c, _ = pieces[key]
    state[r][c].append(key)


  def each_turn(k):
    r, c, d = pieces[k]
    n_r, n_c, n_d = r + dirs[d][0], c + dirs[d][1], d
    # 맨 밑에를 idx=0으로 하자
    # 이동 전 칸 위에 있는놈들 싸그리 같이 가지고
    idx = state[r][c].index(k)
    move = state[r][c][idx:]

    # 2-1. 이동위치가 흰색
    if chess[n_r][n_c] == 0:
      state[n_r][n_c].extend(move)
      del state[r][c][idx:]

    # 2-2. 빨간색
    elif chess[n_r][n_c] == 1:
      state[n_r][n_c].extend(reversed(move))
      del state[r][c][idx:]

    # 2-3. 파란색 또는 out of index
    elif chess[n_r][n_c] == 2:
      if d in [1, 2]:
        n_d = 2 if d == 1 else 1
      else:
        n_d = 4 if d == 3 else 3
      nn_r, nn_c = r + dirs[n_d][0], c + dirs[n_d][1]

      if chess[nn_r][nn_c] == 2:
        n_r, n_c = r, c
      else:
        n_r, n_c = nn_r, nn_c
        # 이부분 실수 : 옮겨야 할 칸 상태에 따라
        if chess[n_r][n_c] == 0:
          state[n_r][n_c].extend(move)
        else:
          state[n_r][n_c].extend(reversed(move))
        del state[r][c][idx:]

    # 말 상태 업데이트
    for x in move:
      if x == k:
        pieces[x] = [n_r, n_c, n_d]
      else:
        pieces[x][:2] = n_r, n_c

    if len(state[n_r][n_c]) >= 4:
      return True
    else:
      return False


  def game():
    i = 1
    while i <= MAX_TURN:
      for k in range(1, K + 1):
        if each_turn(k):
          print(i)
          return
      i += 1

    print(-1)


  game()