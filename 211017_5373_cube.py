import sys

input = lambda: sys.stdin.readline()
sys.stdin = open("input.txt", "r")

TC = int(input())
for test_case in range(1, TC + 1):
  def rotate(side):
    # U : 위, D : 아래, F : 앞, B : 뒤, L : 왼, R : 오른
    # + : 시계, - : 반시계
    if side == 'U':
      T, X, Y, Z, W = U, L, F, R, B
    if side == 'L':
      T, X, Y, Z, W = L, F, U, B, D
    if side == 'F':
      T, X, Y, Z, W = F, U, L, D, R
    if side == 'R':
      T, X, Y, Z, W = R, D, B, U, F
    if side == 'B':
      T, X, Y, Z, W = B, R, D, L, U
    if side == 'D':
      T, X, Y, Z, W = D, B, R, F, L

    T[0][2], T[1][2], T[2][2], T[2][1], T[2][0], T[1][0], T[0][0], T[0][1] =\
      T[0][0], T[0][1], T[0][2], T[1][2], T[2][2], T[2][1], T[2][0], T[1][0]

    X[2][2], X[2][1], X[2][0], Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2] = \
      Y[2][0], Y[1][0], Y[0][0], Z[0][2], Z[1][2], Z[2][2], W[0][0], W[0][1], W[0][2], X[2][2], X[2][1], X[2][0]

  n = int(input())
  U = [['w'] * 3 for _ in range(3)]
  D = [['y'] * 3 for _ in range(3)]
  F = [['r'] * 3 for _ in range(3)]
  B = [['o'] * 3 for _ in range(3)]
  L = [['g'] * 3 for _ in range(3)]
  R = [['b'] * 3 for _ in range(3)]

  for side, direction in input().split():
    rotate(side)  # 90 degree
    if direction == '-':  # + 180 degree
      rotate(side)
      rotate(side)

  for k in range(3):  # Print out answer
    print("".join(U[k]))
