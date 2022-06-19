from collections import deque
import numpy as np
def bellmanford(graph, start):
  v = len(graph)
  sd = [float('inf')] * v
  sd[start] = 0
  for _ in range(v - 1):
    for i in range(v):
      for j in range(v):
        if sd[i] != float('inf') and sd[i] + graph[i][j] < sd[j]:
          sd[j] = sd[i] + graph[i][j]
  for i in range(v):
    for j in range(v):
      if sd[i] != float('inf') and sd[i] + graph[i][j] < sd[j]:
        raise Exception("Negative Cycles Encountered")
  return sd

def shortestmap(graph):
  v = len(graph)
  smap = []
  for i in range(v):
    smap.append(bellmanford(graph, i))
  return smap

def solution(g, t):
  pos = len(g)
  try: 
    smap = shortestmap(g)
    s = []
    s.append((t, 0, [0]))
    sols = [5] # MAX ID BUNNY+1
    while s:
      # print(s)
      timeleft, curpos, path = s.pop()
      # print(timeleft, curpos, path)
      if curpos == pos-1:
        if timeleft >= 0:
          bunnies = np.array(sorted(path[1:-1])) - 1
          if len(sols) < len(bunnies):
            sols = bunnies
          elif len(sols) == len(bunnies):
            if max(bunnies) < max(sols):
              sols = bunnies
      else:
        for i in range(1, pos):
          if i not in path:
            s.append((timeleft-smap[curpos][i], i, path + [i]))
    if 5 in sols:
      return []
    else:
      return sols
  except:
    return [i for i in range(pos-2)]