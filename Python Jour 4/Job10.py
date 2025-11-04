def verif_nombre(i):
    if i>0 and i==int(i):   
        if i%2==0:
            print("Le nombre est pair")
        else:
            print("Le nombre est impair")
    else:
        print("Error!Le nombre est décimal")
verif_nombre(3)
verif_nombre(2)
verif_nombre(2.5)