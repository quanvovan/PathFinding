from best_first_search import *
from astar import *
from path_map import *

def Permute(N):
    X = [i for i in range(N)]
    tmp = []
    tmp.append([i for i in X])
    while (True):
        k = l = -1
        for i in range(N-2, -1, -1): 
            if X[i] < X[i+1]:
                k = i
                break
            
        if k < 0: break
        
        for i in range(N-1, k, -1):
            if X[k] < X[i]:
                l = i
                break
            
        X[k], X[l] = X[l], X[k]
        i = k+1
        j = N-1
        while i < j: 
            X[i], X[j] = X[j], X[i]
            i += 1
            j -= 1
            
        tmp.append([i for i in X])
    return tmp

def Pickup(A, Xmax, Ymax, startPoint, endPoint, pickupPoints):  
    minCost = inf
    A_res = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
    permutations = Permute(len(pickupPoints))
    for p in permutations:
        A_tmp = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
        totalCost = 0
        flag = 0
        lastPoint = startPoint
        for i in p:
            A_tmp, cost = A_Star(A_tmp, Xmax, Ymax, lastPoint, pickupPoints[i])
            if cost < inf:
                lastPoint = pickupPoints[i]
                totalCost += cost
            else:
                flag = 1
                break
        
        if flag == 1:
            break
        
        A_tmp, cost = A_Star(A_tmp, Xmax, Ymax, lastPoint, endPoint)
        if cost < inf:
            totalCost += cost
        else: break
        
        if totalCost < minCost:
            minCost = totalCost
            A_res = [[A_tmp[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
    
    if minCost == inf:
        minCost = 0
    
    showMap(A_res, Xmax, Ymax, startPoint, endPoint,str('Algorithm used: A*\n(Cost = {c})'.format(c = minCost)))
    return
    
