def get_next(s1):
    prefix = set()
    postfix = set()
    ret = []
    for i in range(1,len(s1)):
        prefix.add(s1[:i])
        postfix = {s1[j:i+1] for j in range(1,i+1)}
        print (prefix&postfix)
        ret.append(len(((prefix&postfix) or {''}).pop()))
    return ret

def kmp_match(s,p):
    m = len(s)
    n = len(p)
    cur = 0
    table = get_next(p)
    while cur < m-n:
        for i in range(n):
            if s[cur+i] != p[i]:
                cur += max(i-table[i-1],1)
                break;
        return True
    return False

if __name__ == '__main__':
    ret = get_next('ABCDABD')
    print (ret)
    s = 'BBC ABCDAB ABCDABCDABDE'
    p = 'ABCDABD'
    print (kmp_match(s,p))