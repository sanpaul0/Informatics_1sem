s=input().split()
G=int(s[0])
st=s[1]
L=len(st)
num = int(L/G)

A=[]
for i in range(num):
    A.append(st[i*G:(i+1)*G])
print(*A)
B=[]
for j in range(len(A)):
    B.append(A[j][::-1])
res=''.join(B)
print(res)



