import matplotlib.pyplot as plt
import numpy as np
import matplotlib

def printCell(ax, xy, w, h, fColor = None, eColor = None, lWidth = None):
    rec = plt.Rectangle(xy, w, h, facecolor = fColor, edgecolor = eColor, linewidth = lWidth)
    ax.add_patch(rec)
    return ax

def showMap(A, Xmax, Ymax, startPoint, endPoint, algorithmName = ''):
    X_Axis, Y_Axis = Ymax + 1, Xmax + 1
    
    fig = plt.figure()
    ax = fig.add_subplot(111)


    for i in range(X_Axis):
        ax = printCell(ax, (i,0), 1, 1, 'grey', 'black', 1)
        ax = printCell(ax, (i, Y_Axis - 1), 1, 1, 'grey', 'black', 1)
        
    for i in range(Y_Axis):
        ax = printCell(ax, (0, i), 1, 1, 'grey', 'black', 1)
        ax = printCell(ax, (X_Axis - 1, i), 1, 1, 'grey', 'black', 1)
    
    for i in range(1, Xmax):
        for j in range(1, Ymax):
            ax = printCell(ax, (j, i), 1, 1, 'white', 'black', 1)
            
    for i in range(1, Xmax):
        for j in range(1, Ymax):
            if A[i][j] == '#':
                ax = printCell(ax, (j, i), 1, 1, 'gold', 'white', 1)
            elif A[i][j] == 'X':
                ax = printCell(ax, (j, i), 1, 1, 'orange', 'white', 1)
            elif A[i][j] == '*':
                ax = printCell(ax, (j+0.2, i+0.2), 0.6, 0.6, 'green', 'black', 1)
            elif A[i][j] == '+':
                cir = plt.Circle((j + 0.5, i + 0.5), radius = 0.2 , facecolor = 'black')
                ax.add_patch(cir)
              
    ax = printCell(ax, (startPoint[1], startPoint[0]), 1, 1, 'red', 'black', 2)
    ax = printCell(ax, (endPoint[1], endPoint[0]), 1, 1, 'blue', 'black', 2)
    
    #plt.xticks(range(0, X_Axis+1))
    #plt.yticks(range(0, Y_Axis+1))
    plt.axis('off')
    plt.axis('equal')
    plt.title(algorithmName, fontsize = 14)
    #s_point = matplotlib.patches.Patch(color='red', label='Start Point- S')
    #g_point = matplotlib.patches.Patch(color='blue', label='End Point - G')
    #p_point = matplotlib.patches.Patch(color='green', label='Intermediate Points')
    #plt.legend(handles=[s_point, g_point, p_point], loc = 'right', fontsize = 14)
    plt.show()
    return# -*- coding: utf-8 -*-

