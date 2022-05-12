def strtoint(fish):
    for i in range(len(fish)):
        fish[i] = int(fish[i])
    return fish

def unflip(farr):
    arr = []
    cmp = []
    
    for i in range(len(farr)):
        arr.append(int(i+1))
    
    for i in range(len(farr)):
        cmp.append(arr[i]-farr[i])
    
    cmp2 = []
    if cmp[0] != 0:
        cmp2.append(cmp[0])
        
    for i in range(1,len(cmp)):
        if cmp[i] != cmp[i-1]:
            cmp2.append(cmp[i])
    
    if cmp2[len(cmp2)-1] == 0:
        del cmp2[len(cmp2)-1]
    
    if len(cmp2) == 1:
        return "one"
    elif len(cmp2) == 2:
        return "two"
    elif len(cmp2) == 3:
        return "two"
    else:
        return "over"
    
if __name__ == "__main__":
    k = int(input())
    array = []
    counts = []
    
    array = [input().split() for i in range(5)]
    
    for i in range(len(array)):
        array[i] = strtoint(array[i])
    
    for i in array:
        count = unflip(i)
        counts.append(count)
    
    for i in counts:
        print(i)