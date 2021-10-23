import sys
from collections import Counter

input = lambda: sys.stdin.readline()

sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
  r, c, k = map(int, input().split()) # 1~100
  A = [list(map(int,input().split())) for _ in range(3)]

  def op_R(arr2d): # 모든 행에 대해 정렬
    max_col = 0
    tmp = []
    for a in arr2d:
      row = []
      for v, k in sorted([[v, k] for k, v in Counter(a).items() if k!=0]):
        row.extend([k, v])
      max_col = max(max_col, len(row))
      tmp.append(row)

    for i in range(len(tmp)):
      if len(tmp[i]) < max_col:
        tmp[i].extend([0] * (max_col - len(tmp[i])))
        tmp[i] = tmp[i][:100]
    return tmp

  def op_C(arr2d): # 모든 열에 대해 정렬
    tr_A = op_R(list(zip(*arr2d))) # 로직은 똑같으니 transposed 해서 넘기기
    return list(zip(*tr_A))

  def result():
    global A
    if r<=len(A) and c<=len(A[0]):
      if A[r-1][c-1] == k:
        print(0)
        return

    for i in range(1, 101):
      len_r, len_c = len(A), len(A[0])
      if len_r >= len_c: # 행의 개수 >= 열의 개수인 경우
        A = op_R(A)
      else: # 행의 개수 < 열의 개수인 경우
        A = op_C(A)

      if r<=len(A) and c<=len(A[0]):  # 인덱스 1부터, out of index 조심
        if A[r-1][c-1] == k:  # A[r][c] == k 가 되기 위한 최소 연산시간
          print(i)
          return

    print(-1) # 100초가 지나도 안되면 -1

  result()