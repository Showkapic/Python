montant=5000
rendement=2
print(f"Vous avez {montant}.")
gain=(montant*rendement)/100
print(f"Chaque année vous gagnerez {gain}.")
retrait=int(input("Combien souhaitez vous retirez?"))
montant=montant-retrait
if retrait>=(montant*10)/100:
    rendement=1
print(f"Vous avez{montant}.")
gain=(montant*rendement)/100
print(f"Chaque année vous gagnerez {gain}.")