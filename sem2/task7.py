A = list(map(int, input().split()))
number=0
for i in range(len(A)):
    if number<A.count(A[i]):
        number=A.count(A[i])
        num=A[i]
print(num)