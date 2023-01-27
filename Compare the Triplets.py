def compareTriplets(a, b):
    alice, bob = 0,0
    for i,j in zip(a,b):
        if i>j:
            alice+=1
        elif i<j:
            bob +=1
    ans = [alice,bob]
    return ans