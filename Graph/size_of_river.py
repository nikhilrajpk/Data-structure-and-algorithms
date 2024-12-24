"""[[1, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1] ]
 1 -> river, 0 -> land
 we need to find the river size. output will be [1, 5, 2, 1].
 we need to check the nearest neighbours and then the size should be increased.
"""
from collections import deque
class RiverSize:
    def __init__(self):
        self.size = []
        
    def calculateRiverSize(self,matrix):
        visited = [[False] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if visited[i][j]:
                    continue
                elif matrix[i][j] == 0:
                    visited[i][j] = True
                else:
                    self.traverseThroughRiver(i, j, matrix, visited)
        return self.size

    def traverseThroughRiver(self, i, j, matrix, visited):
        currentRiverSize = 0
        nearestNeighbours = deque()
        nearestNeighbours.append([i,j])
        
        while nearestNeighbours:
            currentNode = nearestNeighbours.pop()
            i = currentNode[0]
            j = currentNode[1]
            
            if visited[i][j]:
                continue
            visited[i][j] = True
            
            if matrix[i][j] == 0:
                continue
            
            currentRiverSize += 1
            self.findNearestNeighbour(i, j, matrix, visited, nearestNeighbours)
            
        self.size.append(currentRiverSize)
            
    def findNearestNeighbour(self, i, j, matrix, visited, nearestNeighbours):
        if i > 0 and not visited[i-1][j]:
            nearestNeighbours.append([i-1, j])
            
        if i < len(matrix)-1 and not visited[i+1][j]:
            nearestNeighbours.append([i+1, j])
            
        if j > 0 and not visited[i][j-1]:
            nearestNeighbours.append([i, j-1])
            
        if j < len(matrix[0])-1 and not visited[i][j+1]:
            nearestNeighbours.append([i, j+1])
        
        return nearestNeighbours
    
if __name__ == '__main__':
    river = RiverSize()
    matrix = [  [1, 0, 0, 1, 1],
                [0, 1, 1, 1, 0],
                [0, 0, 0, 0, 1],
                [1, 0, 0, 0, 1] ]
    print(river.calculateRiverSize(matrix))