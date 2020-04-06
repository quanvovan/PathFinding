from path_map import *
from best_first_search import *
from astar import *
from preprocess import *
from breadth_first_search import *
from pick_up import *
from usc import *

#Level 1+2:

#Test case 1:
print("TEST CASE 1: ")
"""Initialize data"""
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input1_1.txt')

"""Apply Breadth-First Search Algorithm"""
A1 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A1, cost1 = Breadth_First_Search(A1, Xmax, Ymax, startPoint, endPoint)
showMap(A1, Xmax, Ymax, startPoint, endPoint, 'Breadth-First Search Algorithm\n(Cost = {c})'.format(c=cost1))

"""Apply Greedy Best-First Search Algorithm"""
A2 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A2,cost2 = Greedy_Best_First_Search(A2, Xmax, Ymax, startPoint, endPoint)
showMap(A2, Xmax, Ymax, startPoint, endPoint, 'Greedy Best-First Search Algorithm\n(Cost = {c})'.format(c=cost2))

"""Apply A-Star Algorithm"""
A3 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A3, cost3 = A_Star(A3, Xmax, Ymax, startPoint, endPoint)
showMap(A3, Xmax, Ymax, startPoint, endPoint, 'A* Search Algorithm\n(Cost = {c})'.format(c=cost3))

"""Apply Uniform Cost Search Algorithm"""
A4 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A4, cost4 = USC(A4, Xmax, Ymax, startPoint, endPoint)
showMap(A4, Xmax, Ymax, startPoint, endPoint, 'Uniform Cost Search Algorithm\n(Cost = {c})'.format(c=cost4))

#Test case 2:
print("TEST CASE 2: ")
"""Initialize data"""
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input1_2.txt')

"""Apply Breadth-First Search Algorithm"""
A1 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A1, cost1 = Breadth_First_Search(A1, Xmax, Ymax, startPoint, endPoint)
showMap(A1, Xmax, Ymax, startPoint, endPoint, 'Breadth-First Search Algorithm\n(Cost = {c})'.format(c=cost1))

"""Apply Greedy Best-First Search Algorithm"""
A2 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A2,cost2 = Greedy_Best_First_Search(A2, Xmax, Ymax, startPoint, endPoint)
showMap(A2, Xmax, Ymax, startPoint, endPoint, 'Greedy Best-First Search Algorithm\n(Cost = {c})'.format(c=cost2))

"""Apply A-Star Algorithm"""
A3 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A3, cost3 = A_Star(A3, Xmax, Ymax, startPoint, endPoint)
showMap(A3, Xmax, Ymax, startPoint, endPoint, 'A* Search Algorithm\n(Cost = {c})'.format(c=cost3))

"""Apply Uniform Cost Search Algorithm"""
A4 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A4, cost4 = USC(A4, Xmax, Ymax, startPoint, endPoint)
showMap(A4, Xmax, Ymax, startPoint, endPoint, 'Uniform Cost Search Algorithm\n(Cost = {c})'.format(c=cost4))

#Test case 3:
print("TEST CASE 3: ")
"""Initialize data"""
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input1_3.txt')

"""Apply Breadth-First Search Algorithm"""
A1 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A1, cost1 = Breadth_First_Search(A1, Xmax, Ymax, startPoint, endPoint)
showMap(A1, Xmax, Ymax, startPoint, endPoint, 'Breadth-First Search Algorithm\n(Cost = {c})'.format(c=cost1))

"""Apply Greedy Best-First Search Algorithm"""
A2 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A2,cost2 = Greedy_Best_First_Search(A2, Xmax, Ymax, startPoint, endPoint)
showMap(A2, Xmax, Ymax, startPoint, endPoint, 'Greedy Best-First Search Algorithm\n(Cost = {c})'.format(c=cost2))

"""Apply A-Star Algorithm"""
A3 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A3, cost3 = A_Star(A3, Xmax, Ymax, startPoint, endPoint)
showMap(A3, Xmax, Ymax, startPoint, endPoint, 'A* Search Algorithm\n(Cost = {c})'.format(c=cost3))

"""Apply Uniform Cost Search Algorithm"""
A4 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A4, cost4 = USC(A4, Xmax, Ymax, startPoint, endPoint)
showMap(A4, Xmax, Ymax, startPoint, endPoint, 'Uniform Cost Search Algorithm\n(Cost = {c})'.format(c=cost4))

#Test case 4:
print("TEST CASE 4: ")
"""Initialize data"""
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input1_4.txt')

"""Apply Breadth-First Search Algorithm"""
A1 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A1, cost1 = Breadth_First_Search(A1, Xmax, Ymax, startPoint, endPoint)
showMap(A1, Xmax, Ymax, startPoint, endPoint, 'Breadth-First Search Algorithm\n(Cost = {c})'.format(c=cost1))

"""Apply Greedy Best-First Search Algorithm"""
A2 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A2,cost2 = Greedy_Best_First_Search(A2, Xmax, Ymax, startPoint, endPoint)
showMap(A2, Xmax, Ymax, startPoint, endPoint, 'Greedy Best-First Search Algorithm\n(Cost = {c})'.format(c=cost2))

"""Apply A-Star Algorithm"""
A3 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A3, cost3 = A_Star(A3, Xmax, Ymax, startPoint, endPoint)
showMap(A3, Xmax, Ymax, startPoint, endPoint, 'A* Search Algorithm\n(Cost = {c})'.format(c=cost3))

"""Apply Uniform Cost Search Algorithm"""
A4 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A4, cost4 = USC(A4, Xmax, Ymax, startPoint, endPoint)
showMap(A4, Xmax, Ymax, startPoint, endPoint, 'Uniform Cost Search Algorithm\n(Cost = {c})'.format(c=cost4))

#Test case 5:
print("TEST CASE 5: ")
"""Initialize data"""
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input1_5.txt')

"""Apply Breadth-First Search Algorithm"""
A1 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A1, cost1 = Breadth_First_Search(A1, Xmax, Ymax, startPoint, endPoint)
showMap(A1, Xmax, Ymax, startPoint, endPoint, 'Breadth-First Search Algorithm\n(Cost = {c})'.format(c=cost1))

"""Apply Greedy Best-First Search Algorithm"""
A2 = [[A[j][i] for i in range(Ymax + 1) ] for j in range(Xmax + 1)]
A2,cost2 = Greedy_Best_First_Search(A2, Xmax, Ymax, startPoint, endPoint)
showMap(A2, Xmax, Ymax, startPoint, endPoint, 'Greedy Best-First Search Algorithm\n(Cost = {c})'.format(c=cost2))

"""Apply A-Star Algorithm"""
A3 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A3, cost3 = A_Star(A3, Xmax, Ymax, startPoint, endPoint)
showMap(A3, Xmax, Ymax, startPoint, endPoint, 'A* Search Algorithm\n(Cost = {c})'.format(c=cost3))

"""Apply Uniform Cost Search Algorithm"""
A4 = [[A[j][i] for i in range(Ymax + 1)] for j in range(Xmax + 1)]
A4, cost4 = USC(A4, Xmax, Ymax, startPoint, endPoint)
showMap(A4, Xmax, Ymax, startPoint, endPoint, 'Uniform Cost Search Algorithm\n(Cost = {c})'.format(c=cost4))

#Level 3:

#Test case 1:
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input2_1.txt')
Pickup(A, Xmax, Ymax, startPoint, endPoint, pickupPoints)

#Test case 2:
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input2_2.txt')
Pickup(A, Xmax, Ymax, startPoint, endPoint, pickupPoints)

#Test case 3:
A, Xmax, Ymax, startPoint, endPoint, pickupPoints, N, shape = readInput('data/input2_3.txt')
Pickup(A, Xmax, Ymax, startPoint, endPoint, pickupPoints)