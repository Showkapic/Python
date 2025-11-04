def triangle(H):
    for i in range (1,H+1):
        for j in range (1,2*H):
            if j == H-i+1:
                print("/",end="")
            elif j == H+i-1:
                print("\\",end="")
            elif i == H:
                print("-",end="")
            else:
                print(" ",end="")
        print()


triangle(11)
