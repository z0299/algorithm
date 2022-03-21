# Quick Sort
def quick_sort(arr, start, end):
    #원소가 1개인 경우
    if start >= end: 
        return 
    
    pivot = start
    left = start +1
    right = end
    
    while left <= right:
        while left <= end and arr[left] >= arr[pivot]:
            left += 1
        while right > start and arr[right] <= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]
    quick_sort(arr, start, right-1)
    quick_sort(arr, right+1, end)
        
    return arr


def add(arr, k):
    sum = 0
    
    if k == 0 :
        for i in range(len(arr), 0,-1):
            sum += arr[i-1]*i
    else:
        for i in range(len(arr), 0,-1):
            sum += arr[i-2]*i
    
    return sum

if __name__ == "__main__":
    n, k = input().split()
    n = int(n)
    k = int(k)
    
    # 배열 입력 받기
    array = []
    for i in range(n):
        array.append(int(input()))
        
    # 실수하는 사람이 있는 경우 배열 밖으로 빼둔다
    if k > 0:
        last = int(array[k-1])
        del array[k-1]
    
    # 오름차순 정렬
    array = quick_sort(array,0, len(array)-1)
    
    # 실수하는 사람 마지막에 다시 도전
    if k > 0:
        array.append(last)
    
    # 시간 합산
    sum = add(array, k)
    
    print(sum)