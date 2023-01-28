def miniMaxSum(arr):
    ans = []
    for i in range(len(arr)):
        s = 0
        for j in range(len(arr)):
            if i!=j:
                s+=arr[j]
        ans.append(s)
    print(min(ans), max(ans))