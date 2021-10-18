import sys

sys.stdin = open("input.txt", "r")
input = lambda : sys.stdin.readline()

T = int(input())
for test_case in range(1, T + 1):
  N = int(input())
  schedule = [tuple(map(int,input().split())) for _ in range(N)]
  dp = [0]*(N+1)

  for i in reversed(range(N)):
    t, p = schedule[i]
    if N-i < t:
      dp[i] = dp[i+1]
    else:
      dp[i] = max(p + dp[i+t], dp[i+1])

  print(dp[0])
