st=input()
L = len(st)
num_steps = L//2+1
flag1 = True
flag2 = True
sym_letters = ['A', 'M', 'H', 'I', 'V', 'W', 'O', 'T', 'X', 'Y', 'U', '1', '8']
mir_letters =['E', '3', 'S', '5', 'Z', '2', 'J', 'L']

for i in range(num_steps):
    if st[i] not in sym_letters and st[i] not in mir_letters and st[i]!=st[-i-1]:
        flag1 = False
        flag2 = False
        break
    elif st[i] not in sym_letters and st[i] not in mir_letters:
        flag1 = False
    else:
        if st[i] in sym_letters:
            if st[i]!=st[-i-1]:
                flag2 = False
                flag1 = False
                break
        elif st[i] in mir_letters:
            if st[i]=='E' and st[-i-1]!='3':
                flag2 = False
                flag1 = False
                break
            else:
                flag2 = False
            if st[i]=='L' and st[-i-1]!='J':
                flag2, flag1 = False
                break
            else:
                flag2 = False
            if st[i]=='Z' and st[-i-1]!='5':
                flag2, flag1 = False
                break
            else:
                flag2 = False
            if st[i]=='S' and st[-i-1]!='2':
                flag2, flag1 = False
                break
            else:
                flag2 = False
    if st[i] not in sym_letters and st[i] not in mir_letters:
        flag1 = False

if flag2== True and flag1==True:
    print(st, 'is a mirrored palindrome.')
elif flag2 == False and flag1 == True:
    print(st, 'is a mirrored string.')
elif flag2== True and flag1== False:
    print(st, 'is a regular palindrome.')
else:
    print(st, 'is not a palindrome.')











#if st[i]='E':
#    if st[-i-1]='3':
#if st[i] in sym_letters
