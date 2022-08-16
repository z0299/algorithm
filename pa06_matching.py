def RK(ps, ts):
    d = 256
    q = 2**16

    M = len(ps)
    N = len(ts)
    
    count1 = 0
    count2 = 0
    i = 0
    j = 0
    p = 0
    t = 0
    h = 1
    
    for i in range(M-1):
        h = (h*d)%q
    
    for i in range(M):
        p = (d*p+ord(ps[i]))%q
        t = (d*t+ord(ts[i]))%q
     
    for i in range(N-M+1):
        count2 += 1
        if p == t:
            for j in range(M):
                count1 += 1
                if ts[i+j] != ps[j]:
                    break
                
            j += 1
            if j == M:
                return count1+count2
        
        if i < N-M:
            t = (d*(t-ord(ts[i])*h) + ord(ts[i+M]))%q
            if t < 0:
                t = t + q
    return count1+count2

def KMP(ps, ts):
    M = len(ps)
    N = len(ts)
    
    count1 = 0
    i = 0
    j = 0
    
    lps = LPS(ps)
    
    while i < N:
        count1 += 1
        if ps[j] == ts[i]:
            i += 1
            j += 1
            if j == M:
                j = lps[j-1]
                break
        elif ps[j] != ts[i]:
            if j != 0: 
                j = lps[j-1]
            else:
                i += 1
        
    return count1
    
def LPS(ps):
    lps = [0]*(len(ps))
    length = 0
    
    i = 1
    while i < len(ps):
        if ps[i] == ps[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
    
    return lps
  
def BM(ps, ts):
    M = len(ps)
    N = len(ts)
    
    count1 = 0
    j = M-1
    i = M-1
    skip = initSkip(ps)
    
    while j >= 0:
        count1 += 1
        while ts[i] != ps[j]:
            count1 += 1
            k = skip[ord(ts[i]) - ord('A')]
            if M-j > k:
                i = i + M - j
            else:
                i = i + k
            if i >= N:
                return count1
            j = M - 1
        i = i - 1
        j = j - 1
    return count1

def initSkip(ps):
    num = 26
    M = len(ps)
    skip = [M for i in range(num)]
    for i in range(M):
        skip[ord(ps[i]) - ord('A')] = M-i-1
    return skip

if __name__ == "__main__":
    p_string = ''
    t_string = ''
    
    p_line = int(input())
    for i in range(p_line):
        p_string += input()
    t_line = int(input())
    for i in range(t_line):
        t_string += input()
    
    countList = {}
    count1 = RK(p_string, t_string)
    count2 = KMP(p_string, t_string)
    count3 = BM(p_string, t_string)
    countList[1] = count1
    countList[2] = count2
    countList[3] = count3
    
    sortedCountList = sorted(countList.items(), key = lambda item: item[1])
    x=[]
    for i in sortedCountList:
        x.append(list(i))
    
    result = ''
    if x[0][1] == x[1][1] and x[1][1] == x[2][1]:
        result += '0 0 0'
    elif x[0][1] == x[1][1]:
        result += '0 0 '
        result += str(x[2][0])
    elif x[1][1] == x[2][1]:
        result += str(x[0][0])
        result += ' 0 0'
    else:
        result += str(x[0][0])+' '
        result += str(x[1][0])+' '
        result += str(x[2][0])
    
    print(result)