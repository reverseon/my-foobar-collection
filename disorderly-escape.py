from collections import Counter
gcdgl = []
facgl = []
def gcddp(n):
    res = [[0 for x in range(n)] for y in range(n)]
    for i in range(n):
        for j in range(i,n):
            if i == 0 or j == 0:
                res[i][j] = 1
                res[j][i] = 1
            elif i == j:
                res[i][j] = i+1
            else:
                res[i][j] = res[i][j-i-1]
                res[j][i] = res[i][j-i-1]
    global gcdgl 
    gcdgl = res

def facdp(n):
  res = [1 for _ in range(n)]
  for i in range(1,n):
    res[i] = res[i-1]*(i+1)
  global facgl
  facgl = res

def gcd(x, y):
  return gcdgl[x-1][y-1]

def fac(n):
  return facgl[n-1]

def cc(c, n):
  res = fac(n)
  for i, cn in Counter(c).items():
    res//=(i**cn)*fac(cn)
  return res

def pcc(n):
  a = [0 for i in range(n + 1)]
  k = 1
  y = n - 1
  res = []
  while k != 0:
    x = a[k - 1] + 1
    k -= 1
    while 2 * x <= y:
        a[k] = x
        y -= x
        k += 1
    l = k + 1
    while x <= y:
        a[k] = x
        a[l] = y
        pt = a[:k+2]
        res.append((pt, cc(pt,n)))
        x += 1
        y -= 1
    a[k] = x + y
    y = x + y - 1
    pt = a[:k+1]
    res.append((pt, cc(pt,n)))
  return res

def solution(w, h, s):
  n = max(w, h)
  gcddp(n)
  facdp(n)
  ts = 0
  for i in pcc(w):
    for j in pcc(h):
      t = i[1]*j[1]
      ts += t*(s**sum([sum([gcd(k, l) for k in i[0]]) for l in j[0]]))
  return str(ts//(fac(w)*fac(h)))