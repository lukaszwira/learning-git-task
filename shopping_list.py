shops = {
    "piekarnia": ['Chleb', 'Pączek', 'Bułki'],
    "warzywniak": ['Marchew', 'Seler', 'Rukola']
}
products = 0
for shop in shops:
    products += len(shops[shop])
    print("idę do", shop.upper(), "i kupuję tam", ', '.join(shops[shop]).upper())
print("W sumie kupuję", products,"produktów")
print("nowy commit na zdalne repo")
print("pozdrowienia od kolektywu mieszkańców bloku ćwiartki 3/4")