N=int(input("Entrez un nombre supérieur à 0."))
if N<1:
    print("Error!")
    StopIteration
for i in range(1,N+1):
    print("Table de", i)
    for j in range(1,11):
        print(f"{i} X {j} = {i*j}")