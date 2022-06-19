from collections import defaultdict
def zo1(a, b):
  return 1 if ((a == 1 or a ==2) and b == 0) or ((b == 1 or b ==2) and a == 0) else 0
def compute(a, b, n):
  res = 0
  for i in range(n):
    picker = 0b11 << i
    c1 = (a & picker) >> i
    c2 = (b & picker) >> i
    res += zo1(c1, c2) << i
  return res

def searchspace(num, ncol):
  s = set(num)
  ssp = defaultdict(set)
  for i in range(1<<(ncol+1)):
    for j in range(1<<(ncol+1)):
      af = compute(i, j, ncol)
      if af in s:
        ssp[(i, af)].add(j)
  return ssp 

def solution(g):
  g = list(zip(*g)) 
  lcol = len(g[0])
  num = [sum(1<<(lcol-j-1) if e else 0 for j, e in enumerate(i)) for i in g]
  ssp = searchspace(num, lcol)
  hld = {i: 1 for i in range(1<<(lcol+1))}
  for r in num:
    tmp = defaultdict(int)
    for c1 in hld:
      for c2 in ssp[(c1, r)]:
        tmp[c2] += hld[c1]
    hld = tmp
  res = sum(hld.values())
  return res