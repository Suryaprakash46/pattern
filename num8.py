for i in range(5):
    for j in range(5-i-1):
        print(' ',end=' ')
    for j in range(i,-1,-1):
        print(5-i,end=' ')
    print()
