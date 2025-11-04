Liste = [1,2,3,4,5]
print(Liste)
chiffre = Liste[0]
Liste[0] = Liste[4]
Liste[4] = chiffre

print(Liste)