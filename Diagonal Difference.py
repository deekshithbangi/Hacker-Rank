def diagonalDifference(arr):
    #Write your code here
    d_left = 0
    d_right = 0
    for i in range(len(arr)):
        d_left += arr[i][i]
    for j in range(len(arr)):
        d_right += arr[j][len(arr) -1-j]
        
    return abs(d_left - d_right)

def diagonalDifference(arr,n):
    d1,d2 = 0,0
    for i in range(n):
        d1 +=arr[i][i]
    for i,j in zip(range(n), range(n-1,-1,-1)):
        d2+=arr[i][j]
    ans = d1 - d2
    return abs(ans)