import sys
from itertools import permutations

input = lambda: sys.stdin.readline()

# sys.stdin = open("input.txt", "r")
#
# T = int(input())
# for test_case in range(1, T + 1):
N = int(input())
A = list(map(int, input().split()))
ops = list(map(int, input().split()))
cal = []
cal += list('+'*ops[0]) + list('-'*ops[1]) + list('*'*ops[2]) + list('/'*ops[3])

max_n = float('-inf')
min_n = float('inf')

cal_perm = set(permutations(cal, N-1))


def calculator(x, y, c):
  if c == '+':
    return x + y
  elif c == '-':
    return x - y
  elif c == '*':
    return x * y
  else:
    if x < 0:
      return -((-x) // y)
    return x // y


for sample in cal_perm:
  result = 0
  for j in range(N-1):
    if j == 0:
      result = calculator(A[j], A[j+1], sample[j])
    else:
      result = calculator(result, A[j+1], sample[j])

  if result < min_n:
    min_n = result
  if result > max_n:
    max_n = result


print(max_n)
print(min_n)
