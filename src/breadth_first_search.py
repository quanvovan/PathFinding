# -*- coding: utf-8 -*-
inf = int(1e8)

def new2DArray(X, Y, value = 0):
    return [ [ value for i in range(Y) ] for j in range(X)]

def Visit(A, Xmax, Ymax, point, visit, trace, cost, stack):
    u, v = point
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visit[u][v] = True
    tmp = []
    for i in range(4):
        x = u + dx[i]
        y = v + dy[i]
        if (x < 0 or y < 0 or x > Xmax or y > Ymax): continue
        if (visit[x][y] == False and A[x][y] != '#' and A[x][y] != 'X'): 
            trace[x][y] = tuple((u,v))
            cost[x][y] = cost[u][v] + 1
            stack.append((x, y))
            visit[x][y] = True
    return
             
def tracePath(A, trace, startPoint, endPoint):
    u, v = startPoint
    s, t = endPoint
    tmp = trace[s][t]
    while tmp != (u, v):
        x = tmp[0]
        y = tmp[1]
        A[x][y] = '+'
        tmp = trace[x][y]
    return

def Breadth_First_Search(A, Xmax, Ymax, startPoint, endPoint):
    visit = new2DArray(Xmax + 1, Ymax + 1, False)
    trace = new2DArray(Xmax + 1, Ymax + 1, ())
    cost = new2DArray(Xmax + 1, Ymax + 1, inf)
    stack = []
    u, v = startPoint
    s, t = endPoint
    
    trace[u][v] = ((0, 0))
    cost[u][v] = 0
    stack.append((u,v))
    while len(stack) > 0:
        x, y = stack.pop(0)
        if (x == s and y == t): 
            tracePath(A, trace, (u, v), (s, t))
            break
        Visit(A, Xmax, Ymax, (x, y), visit, trace, cost, stack)
    return A, cost[s][t]

