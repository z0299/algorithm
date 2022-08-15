class Node:
    def __init__(self, parent= None, coordinate=None):
        self.parent = parent
        self.coordinate = coordinate
        
        self.f = 0
        self.g = 0
        self.h = 0
        
    def __eq__(self, other):
        return self.coordinate == other.coordinate

def aStar(maze, s, t):
    #시작노드, 도착노드 초기화
    startNode = Node(None, s)
    endNode = Node(None, t)
    
    #openlist, closedlist 초기화
    openList = []
    closedList = []
    
    openList.append(startNode)
    
    while openList:
        currentNode = openList[0]
        currentIdx = 0
        
        #동일한 노드가 openList에 있을때, f값을 비교하여
        #f값이 더 큰 값을 openList에 저장
        for idx, item in enumerate(openList):
            if currentNode.f > item.f:
                currentNode = item
                currentIdx = idx
                
        #확정된 노드 closedList에 저장
        openList.pop(currentIdx)
        closedList.append(currentNode)
        
        if currentNode == endNode:
            """
            current = currentNode
            path = []
            while current is not None:
                path.append(current.coordinate)
                current = current.parent
            path = path[::-1]
            """
            return currentNode.f
        
        children = []
        
        for borderPosition in [(currentNode.coordinate[0]+0, currentNode.coordinate[1]-1),
                               (currentNode.coordinate[0]+0, currentNode.coordinate[1]+1),
                               (currentNode.coordinate[0]-1, currentNode.coordinate[1]+0),
                               (currentNode.coordinate[0]+1, currentNode.coordinate[1]+0)]:
            maze_criteria = [
                borderPosition[0] > len(maze)-1,
                borderPosition[0] < 0,
                borderPosition[1] > (len(maze[len(maze) - 1]) -1),
                borderPosition[1] < 0
            ]
            
            #borderPosition이 maze index내에 있는지 확인
            if any(maze_criteria):
                continue
            
            #borderPosition이 장애물이랑 겹치지 않는지 확인
            if maze[borderPosition[0]][borderPosition[1]] != 1:
                continue
            
            newNode = Node(currentNode, borderPosition)
            children.append(newNode)
            
        for child in children:
            if child in closedList:
                continue
            
            child.g = currentNode.g + 3
            child.h = ((child.coordinate[0]-endNode.coordinate[0])**2) + ((child.coordinate[1]-endNode.coordinate[1])**2)
            child.f = child.g + child.h
            
            if len([openNode for openNode in openList if child == openNode and openNode.g < child.g]) > 0:
                continue
            
            openList.append(child)

if __name__ == "__main__":
    #x,y 지도의 크기
    x,y = input().split()
    x = int(x)
    y = int(y)
    maze = [[1 for col in range(x)] for row in range(y)]
    
    #지나갈 수 없는 길(0)
    block = int(input())
    
    for i in range(block):
        b_coordinate = list(map(int, input().split()))
        maze[b_coordinate[1]][b_coordinate[2]] = 0
       
    #시작점, 도착점 좌표 
    start = input().split()
    del start[0]
    start[0] = int(start[0])
    start[1] = int(start[1])
    start = tuple(start)
    
    end = input().split()
    del end[0]
    end[0] = int(end[0])
    end[1] = int(end[1])
    end = tuple(end)
    
    #장애물
    obstacle = input().split()
    del obstacle[0]
    obstacle[0] = int(obstacle[0])
    
    for i in range(obstacle[0]):
        o_coordinate = list(map(int, input().split()))
        for j in range(o_coordinate[0], o_coordinate[2]+1):
            for k in range(o_coordinate[1], o_coordinate[3]+1):
                maze[j][k] = 0
    
    f = aStar(maze, start, end)
    print(f)