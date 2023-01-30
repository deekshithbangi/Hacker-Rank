def breakingRecords(scores):
    # Write your code here
    best = scores[0]
    worst = scores[0]
    bestcount,worstcount = 0,0 
    for i in range(1,len(scores)):
        if scores[i] > best:
            best = scores[i]
            bestcount +=1
        if  scores[i] < worst :
            worst =scores[i]
            worstcount+=1
    return [bestcount,worstcount]