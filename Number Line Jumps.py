import os
def kangaroo(x1, v1, x2, v2):
    # Write your code here
    if v2 < v1:
        while not(x1>10000) and not(x2>10000):
            x1+=v1
            x2+=v2
            if x1 == x2:
                return 'YES'
    else:
        return 'NO'
    return 'NO'