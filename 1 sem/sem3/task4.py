def tri(size):
    for i in range(size+1):
        print('.'*min(i, size-i+1))
tri(int(input()))


    #if N == 0:
        #return
    #print('.'*i)
    #tri(N-1,i+1)
    #print('.'*i)
#N = int(input())
#if N % 2 == 1:
    #tri(N//2  + 1, 1)
#else:
    #tri(N//2, 1)