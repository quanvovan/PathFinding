def Connect(A, pList):
    global k
    pList.append(pList[0])
    for i in range(len(pList) - 1):
        s1 = pList[i]
        s2 = pList[i+1]
        dx = s1[0] - s2[0]
        dy = s1[1] - s2[1]
        p = (dx > 0 and dy > 0) or (dx < 0 and dy < 0) #True - If 'dx' and 'dy' have same sign
        if (p == True  and abs(dx) > abs(dy)) or (p == False and abs(dx) < abs(dy)):
            s1, s2 = s2, s1
            
        x, y = s1[0], s1[1]
        A[x][y] = '#'
        while not (x==s2[0] and y==s2[1]):
            flag = 0
            if (x != s2[0]):
                x = x + int((s2[0]-x)/abs(s2[0]-x))
    
            if (y != s2[1]):
                y = y + int((s2[1]-y)/abs(s2[1]-y))
    
            A[x][y] = '#'
    
    for i in range(len(pList) - 1):
        A[pList[i][0]][pList[i][1]] = 'X'
    return A

def readInput(fileName):
    f = open(fileName, 'r')
    Ymax, Xmax = list(map(int, f.readline().split(',')))
    pointList = list(map(int, f.readline().split(',')))
    N = int(f.readline())
    shape = [[] for i in range(N)]
    for i in range(N):
        arr = list(map(int, f.readline().split(',')))
        for j in range(0, len(arr), 2):
            vertex = tuple((arr[j+1], arr[j]))
            shape[i].append(vertex)
    """    
    print('----------INPUT----------');
    print('X-axis limit: ', Xmax)
    print('Y-axis limit: ', Ymax)
    print('Start point: (', pointList[1], ',',pointList[0],')')
    print('End point: (', pointList[3], ',', pointList[2],')')
    print('Number of shapes: ', N)
    for i in range(N):
        print(' ', shape[i])
    """
    v, u = pointList[:2]    
    t, s = pointList[2:4]   
    
    startPoint = (u,v)  # S(u,v)
    endPoint = (s,t)    # G(s,t)
    
    pickupPoints = []
    for i in range(4, len(pointList), 2):
        pickupPoints.append(tuple((pointList[i+1], pointList[i])))
    
    A = [ [ '.' for i in range(Ymax + 1) ] for j in range(Xmax + 1) ]
    
    for i in range(len(pickupPoints)):
        p = pickupPoints[i]
        A[p[0]][p[1]] = '*'
    
    for i in range(Xmax+1): 
        A[i][0] = A[i][Ymax] = '#'
        
    A[0] = A[Xmax] = ['#' for i in range(Ymax + 1)]
    A[u][v] = 'S'
    A[s][t] = 'G'
    
    for i in range(N):
        A = Connect(A, shape[i]) 
    return A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape