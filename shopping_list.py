shops = {
    "piekarnia": ['Chleb', 'Pączek', 'Bułki'],
    "warzywniak": ['Marchew', 'Seler', 'Rukola']
}
products = 0
for shop in shops:
    products += len(shops[shop])
    print("idę do", shop, "i kupuję tam", shops[shop])
print("W sumie kupuję", products,"produktów")
