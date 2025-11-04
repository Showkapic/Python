def taille(L):
    compteur = 0
    for _ in L:
        compteur += 1
    return compteur

def tri(L):
    n=taille(L)
    echange=True
    while echange:
        echange=False
        i=0
        while i+1 < n:
            if L[i]>L[i+1]:
                temp= L[i]
                L[i]=L[i+1]
                L[i+1]=temp
                echange=True
            i+=1
        n-=1
    return L



donnees = [7, 3, 9, -2, 3, 0]
tri(donnees)
print(donnees)

