from decimal import *
def f(n, nx):
  return n*nx + n*(n+1)/2 - nx*(nx+1)/2

def solution(sn):
  getcontext().prec = 101
  n = int(sn)
  sq2 = Decimal(2).sqrt()
  nx = int((sq2-1)*n)
  res = f(n, nx)
  i = 1
  n = nx
  while (n > 0):
    nx = int((sq2-1)*n)
    res += (-1)**i * f(n, nx)
    n = nx
    i += 1
  return str(int(res))