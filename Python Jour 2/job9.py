pair=""
impair=""
for i in range (31):
    if i % 2 == 0:
        pair+=" "+(str(i))
    else:
        impair+=" "+(str(i))
print("Nombre Pair:")
print(pair)
print("Nombre Impair")
print(impair)