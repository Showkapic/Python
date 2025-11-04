def tapis(L,C):
    for i in range(1, L+1):
        for j in range(1,C+1):
            if j == 1 or j == C:
                print ("|",end="")
            elif i == 1 or i == L:
                print("-",end="")
            elif j == (L-i+1):
                print(" ",end="")
            else:
                print("#",end="")
        print()

tapis(10,10)
