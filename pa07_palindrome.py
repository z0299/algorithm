def checkPalindrome(string, left, right):
    while(left < right):
        if string[left] == string[right]:
            left += 1
            right -= 1
        else:
            if left == 0:
                return 0
            if string[left] == string[right-1]:
                if string[left+1:right-1] == list(reversed(string[left+1:right-1])):
                    return(len(string)-1) 
                else:
                    return left*2+1
            elif string[left+1] == string[right]:
                if string[left+2:right] == list(reversed(string[left+2:right])):
                    return(len(string)-1) 
                else:
                    return left*2+1
            elif string[left] == string[left+1] or string[right] == string[right-1]:
                return left*2+2
            else:
                return left*2+1
    return len(string)

if __name__ == "__main__":
    n = int(input())
    clist = []
    
    f = open("./07_palinderome_data2/3.inp",'r')
    array = f.readlines()
    del array[0]
    search = "\n"
    for i,a in enumerate(array):
        if search in a:
            array[i] = a.strip(search)
        
    for i in array:
        left = 0
        right = len(i)-1
        counts = checkPalindrome(list(i), left, right)
        clist.append(counts)
    """
    for i in range(n):
        s = input()
        left = 0
        right = len(s)-1
        counts = checkPalindrome(list(s), left, right)
        clist.append(counts)
    """
    for i in clist:
        print(i)