A=list(map(int,input().split()))
for i in range(len(A)):
    if A.count(A[i])==1:
        print(A[i])

