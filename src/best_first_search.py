inf = int(1e8)


def D(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)


def new2DArray(X, Y, value=0):
    return [[value for i in range(Y)] for j in range(X)]


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
        if (visit[x][y] ==False and A[x][y] != '#' and A[x][y] != 'X'):
            trace[x][y] = (u,v)
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


def Greedy_Best_First_Search(A, Xmax, Ymax, startPoint, endPoint):
    visit = new2DArray(Xmax + 1, Ymax + 1, False)
    h = new2DArray(Xmax + 1, Ymax + 1, 0)
    trace = new2DArray(Xmax + 1, Ymax + 1, ())
    cost = new2DArray(Xmax + 1, Ymax + 1, inf)
    stack = []
    u, v = startPoint
    s, t = endPoint

    for i in range(Xmax + 1):
        for j in range(Ymax + 1):
            h[i][j] = D(i, j, s, t)

    trace[u][v] = ((0, 0))
    cost[u][v] = 0
    stack.append((u, v))

    while len(stack) > 0:
        m = inf
        imin = -1
        for i in range(len(stack)):
            x0, y0 = stack[i]
            if (h[x0][y0] < m):
                m = h[x0][y0]
                imin = i
        x, y = stack.pop(imin)
        if (x == s and y == t):
            tracePath(A, trace, (u, v), (s, t))
            break
        Visit(A, Xmax, Ymax, (x, y), visit, trace, cost, stack)
    return A, cost[s][t]

