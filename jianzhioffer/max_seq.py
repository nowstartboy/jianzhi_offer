def maxSeq(x):
    max_seq = 0
    max_emdding = 0
    for i in range(x):
        max_emdding += i
        if max_emdding<0:
            max_emdding = 0
        max_seq = max(max_seq,max_emdding)
    return max_seq