from collections import defaultdict

def checkOverlap(l1, l2):
    if ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) <= 0 and ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) <= 0:
        if ccw(l1[0], l1[1], l2[0]) * ccw(l1[0], l1[1], l2[1]) == 0 and ccw(l2[0], l2[1], l1[0]) * ccw(l2[0], l2[1], l1[1]) == 0:
            if max(l1[0][0], l1[1][0]) >= min(l2[0][0], l2[1][0]) and max(l2[0][0], l2[1][0]) >= min(l1[0][0], l1[1][0]) and max(l1[0][1], l1[1][1]) >= min(l2[0][1], l2[1][1]) and max(l2[0][1], l2[1][1]) >= min(l1[0][1], l1[1][1]):
                return True
        else:
            return True
    return False


def ccw(a, b, c):
    return a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(b[0]*a[1]+c[0]*b[1]+a[0]*c[1])

def unionParent(x, y):
    x = findParent(x)
    y = findParent(y)
    if x<y:
        parent[y] = x
    else:
        parent[x] = y
        
def findParent(c):
    if parent[c] != c:
        parent[c] = findParent(parent[c])
    return parent[c]

if __name__ == "__main__":
    n = int(input())
    coordinates = []
    parent = [i for i in range(n)]
    line = []
    
    for i in range(n):
        x1,y1,x2,y2 = map(int, input().split())
        coordinates.append([[x1,y1],[x2,y2]])
        for j in range(i):
            if checkOverlap(coordinates[i], coordinates[j]):
                line.append([i,j])
                
    for c1,c2 in line:
        unionParent(c1,c2)
        
    res = defaultdict(int)
    for i in range(n):
        res[parent[i]]+=1
    print(len(res.keys()))
    print(max(res.values()))
    