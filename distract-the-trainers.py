def gcd(x, y):
   while y:
       x, y = y, x % y
   return x

def isInfinite(x,y):
    ck = (x+y)//gcd(x,y)
    return False if (ck & (ck - 1) == 0) else True
    
def adjdict(blist):
    l = len(blist)
    dictg = {i: [] for i in range(l)}
    for i in range(l):
        for j in range(i, l):
            if i != j and isInfinite(blist[i], blist[j]):
                dictg[i].append(j)
                dictg[j].append(i)
    return dictg
def maxBPM(graph):
    res = 0
    maxNode = len(graph[max(graph, key=lambda a: len(graph[a]))])
    while len(graph) > 1 and maxNode >= 1:
        minNode = min(graph, key=lambda a: len(graph[a]))
        if len(graph[minNode]) == 0:
            del graph[minNode]
        else:
            secondMinNode = 1
            secondMinLen = len(graph[graph[minNode][0]])+1
            for i in graph[minNode]:
                if len(graph[i]) < secondMinLen:
                    secondMinNode, secondMinLen = i, len(graph[i])
                for j in range(len(graph[i])):
                    if graph[i][j] == minNode:
                        del graph[i][j]
                        break
            for i in graph[secondMinNode]:
                for j in range(len(graph[i])):
                    if graph[i][j] == secondMinNode:
                        del graph[i][j]
                        break
            del graph[minNode]
            del graph[secondMinNode]
            res += 2
        if len(graph) > 1:
            maxNode = len(graph[max(graph, key=lambda a: len(graph[a]))])
    return res

def solution(l):
    return len(l) - maxBPM(adjdict(l))