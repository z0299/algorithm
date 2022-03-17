# Selection Sort
def selection_sort(arr, k):
    for i in range(len(arr)-1):
        k -= 1
        if k < 0:
            break
        
        min = i
        for j in range(i+1, len(arr)):
            if arr[min] > arr[j]:
                min = j
        arr[i], arr[min] = arr[min], arr[i]
    return arr


# Heap Sort_오름차순 정렬(최소 힙 트리)
def updateHeap(arr, idx, n):
    min = idx
    left = 2*idx+1
    right = 2*idx+2
    
    if(left < n and arr[left] <= arr[min]):
        min = left
    if(right < n and arr[right] <= arr[min]):
        min = right
    if(min != idx):
        arr[min], arr[idx] = arr[idx], arr[min]
        updateHeap(arr, min, n)

def heap_sort(arr, k):
    n = len(arr)
    
    #최상위 노드가 가장 최소인 min heap구성
    for i in range(n//2-1, -1, -1):
        updateHeap(arr, i, n)
        
    #min값을 기준으로 배열 재 정렬
    for i in range(n-1, 0, -1):
        if k > 0:
            k -= 1
            arr[0], arr[i] = arr[i], arr[0]
            updateHeap(arr, 0, i)
        else:
            break
        
    return arr


# Quick Sort
def quick_sort(arr, start, end, k):
    #원소가 1개인 경우
    if start >= end: 
        return k
    
    pivot = start
    left = start +1
    right = end
    
    if k > 0:
        k -= 1
        while left <= right:
            while left <= end and arr[left] <= arr[pivot]:
                left += 1
            while right > start and arr[right] > arr[pivot]:
                right -= 1
            if left > right:
                arr[right], arr[pivot] = arr[pivot], arr[right]
            else:
                arr[right], arr[left] = arr[left], arr[right]
        k = quick_sort(arr, start, right-1, k)
        if k > 0:
            k = quick_sort(arr, right+1, end, k)

    return k
    
if __name__ == "__main__":
    # 정렬 방법과 pass단계 입력
    sort, k = input().split()
    k = int(k)
   
    array = []
    n = int(input())
    for i in range(n):
        array.append(int(input()))
    

    if(sort == "1"):
        array = selection_sort(array, k)
        for i in range(len(array)):
            print(array[i])
    elif(sort == "2"):
        array = heap_sort(array,k)
        for i in range(n-k):
            print(array[i])
    elif(sort == "3"):
        k = quick_sort(array, 0, len(array)-1, k)
        for i in range(len(array)):
            print(array[i])