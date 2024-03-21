transactions = [
('Կարապետ', 'Կարապետյան', 11000, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 13700, 'zangakbookstore'),
('Կարապետ', 'Կարապետյան', 7200, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 10900, 'zangakbookstore'),
('Կարապետ', 'Կարապետյան', 6200, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 5000, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 4500, 'aperitivo'),
('Կարապետ', 'Կարապետյան', 2800, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 9430, 'sassupermarket'),
('Կարապետ', 'Կարապետյան', 1700, 'aperitivo'),
]

business_totals = {}

for transaction in transactions:
    amount = transaction[2]
    business = transaction[3]
    if business in business_totals:
        business_totals[business] += amount
    else:
        business_totals[business] = amount

max_spending_business = max(business_totals)

print(max_spending_business + ": " + str(business_totals[max_spending_business]))
