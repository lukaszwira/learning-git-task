sklepy = {
    "piekarnia": ['Chleb', 'Pączek', 'Bułki'],
    "warzywniak": ['Marchew', 'Seler', 'Rukola']
}
produkty = 0
for shops in sklepy:
    produkty += len(sklepy[shops])
    
