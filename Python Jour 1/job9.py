prix=499.99
nom="snowboard"
stock=10
print(nom)
print(prix)
print(f"{stock} en stock")
achat=int(input(f"Combien de {nom} souhaitez-vous achetez?"))
if achat>=stock:
    print("Stock insuffisant.")
else:
    print("Merci pour votre achat!")
    stock=(stock-achat)
    print(f"Il  reste {stock} {nom} en stock")