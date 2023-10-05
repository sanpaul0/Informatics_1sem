X, Y, X1, Y1 = [], [], [], []
a=0
x, y = 10, 10
def evklid_nod(num1, num2):
    global nod
    while num1!=0 and num2!=0:
        if num1>num2:
            num1 = num1%num2
        else:
            num2 = num2%num1
    nod = num1 + num2
    print(nod)

def evklid_koef(num1, num2):
    global a
    for i in range(11):
        if (abs(nod - num1 * (i - 10))) % num2 == 0 and (abs(nod - num1 * (i - 10)) == nod - num1 * (i - 10)) :
            Y.append((nod - num1 * (i - 10)) / num2)
            X.append(i - 10)
        elif (abs(nod - num1 * (i - 10))) % num2 == 0 and (-abs(nod - num1 * (i - 10)) == nod - num1 * (i - 10)) :
            Y.append((nod - num1 * (i - 10)) / num2)
            X.append(i - 10)
    x, y = X[0], Y[0]

    for j in range(len(X)):
        if abs(X[j]) + abs(Y[j]) < abs(x) + abs(y):
            x=X[j]
            y=Y[j]
    #Xj = X1[0]
    #for k in range(len(X1)):
       # if X1[k]<Xj:
          #  Xj=X1[k]
          #  a=k
    print(x, y, nod)

nums = list(map(int,input().split()))
num1 = nums[0]
num2= nums[1]
evklid_nod(num1, num2)
evklid_koef(num1,num2)





        #elif (abs(nod-num1*(i-10)))%b == 0 and -abs(nod-num1*(i-10)) == nod-num1*(i-10):
            #X.append(i-10)
            #Y.append(-abs(nod-num1*(i-10)))/b)
            
            
            
            
            








