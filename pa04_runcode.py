def check(s):     
    ans = 1001
    
    if len(s) == 1:
        return 1
    
    for i in range(1, len(s)//2+1):
        cnt = 1
        res = ''
        sstr = s[:i]
        
        for j in range(i, len(s)+i, i):
            if sstr == s[j:j+i]:
                cnt += 1
            else:
                if cnt == 1:
                    res += sstr
                else:
                    res += str(cnt) + sstr
                sstr = s[j:j+i]
                cnt = 1
        ans = min(ans, len(res))
    return ans

if __name__ == "__main__":
    snum = int(input())
    
    sarray = [input() for i in range(snum)]
    
    for i in range(snum):
        print(check(sarray[i]))