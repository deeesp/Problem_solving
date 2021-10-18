import sys
from collections import deque

sys.stdin = open("211014_input_saw.txt", "r")
input = lambda: sys.stdin.readline()

T = int(input())
for test_case in range(1, T + 1):
  # 톱니바퀴 상태 : N극 0, S극 1, 12시부터 시계방향
  saws = [deque(map(int, input().strip())) for _ in range(4)]
  K = int(input())  # 1~100
  # 회전 방법 : (톱니바퀴 번호, 방향), 방향 1 시계, 방향 -1 반시계
  rotates = [tuple(map(int, input().split())) for _ in range(K)]

  def rotation(saw, dir): # 회전 시 맞닿은 톱니의 극이 다른 경우 : 반대방향 회전
    left = saw[-2]
    right = saw[2]
    if dir == 1:
      saw.appendleft(saw.pop())
    else:
      saw.append(saw.popleft())
    return left, right, saw

  def propagation(idx, dir, visited):
    left, right, saw = rotation(saws[idx], dir)
    saws[idx] = saw
    visited[idx] = True

    if idx != 0:
      if left != saws[idx-1][2] and not visited[idx-1]:
        propagation(idx-1, -dir, visited)

    if idx != 3:
      if right != saws[idx+1][-2] and not visited[idx+1]:
        propagation(idx+1, -dir, visited)

  for n, direction in rotates:
    visited = [False]*4
    propagation(n-1, direction, visited)

  answer = 0
  for k in range(4):
    answer += (2**k)*saws[k][0]

  print(answer)


  # for n, dir in rotates:
  #   left, right, saw = rotation(saws[n - 1], dir)
  #   saws[n-1] = saw
  #
  #   if n == 1:
  #     if right != saws[1][-2]:
  #       l2, r2, saw2 = rotation(saws[1], -dir)
  #       saws[1] = saw2
  #       if r2 != saws[2][-2]:
  #         l3, r3, saw3 = rotation(saws[2], dir)
  #         saws[2] = saw3
  #         if r3 != saws[3][-2]:
  #           _, _, saw4 = rotation(saws[3], -dir)
  #           saws[3] = saw4
  #
  #   elif n == 2:
  #     if right != saws[2][-2]:
  #       l3, r3, saw3 = rotation(saws[2], -dir)
  #       saws[2] = saw3
  #       if r3 != saws[3][-2]:
  #         _, _, saw4 = rotation(saws[3], dir)
  #         saws[3] = saw4
  #
  #     if left != saws[0][2]:  # 다른 극일 때 반대 방향
  #       _, _, saw1 = rotation(saws[0], -dir)
  #       saws[0] = saw1
  #
  #   elif n == 3:
  #     if left != saws[1][2]:  # 다른 극일 때 반대 방향
  #       l2, r2, saw2 = rotation(saws[1], -dir)
  #       saws[1] = saw2
  #       if l2 != saws[0][2]:  # 다른 극일 때 반대 방향
  #         _, _, saw1 = rotation(saws[0], dir)
  #         saws[0] = saw1
  #     if right != saws[3][-2]:
  #       _, _, saw4 = rotation(saws[3], -dir)
  #       saws[3] = saw4
  #
  #   elif n == 4:
  #     if left != saws[2][2]:  # 다른 극일 때 반대 방향
  #       l3, r3, saw3 = rotation(saws[2], -dir)
  #       saws[2] = saw3
  #       if l3 != saws[1][2]:  # 다른 극일 때 반대 방향
  #         l2, r2, saw2 = rotation(saws[1], dir)
  #         saws[1] = saw2
  #         if l2 != saws[0][2]:  # 다른 극일 때 반대 방향
  #           _, _, saw1 = rotation(saws[0], -dir)
  #           saws[0] = saw1