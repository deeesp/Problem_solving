import sys
from itertools import combinations, permutations

#sys.stdin = open("input.txt", "r")
input = lambda: sys.stdin.readline()

#T = int(input())
#for test_case in range(1, T + 1):
  N = int(input())
  S = [list(map(int, input().split())) for _ in range(N)]
  comb = list(combinations(range(N), N // 2))
  comb_pair = [(comb[i], comb.pop()) for i in range(len(comb) // 2)]

  MIN = 999999

  for start, link in comb_pair:
    start_sum = sum([S[chemi[0]][chemi[1]] for chemi in permutations(start, 2)])
    link_sum = sum([S[chemi[0]][chemi[1]] for chemi in permutations(link, 2)])
    diff = abs(start_sum - link_sum)
    if diff < MIN:
      MIN = diff
  print(MIN)
