import csv


fin = open('wares.csv', 'r', encoding='utf-8')

row_reader = csv.reader(fin, delimiter=';')

items = []

for row in row_reader:
    name, price = row
    items.append((name, int(price)))

fin.close()

items.sort(key=lambda x: x[1])

result = []
total = 1000

for item in items:
    q = total // item[1]
    if q > 10:
        q = 10
    for _ in range(q):
        result.append(item[0])
    total -= item[1] * q

if result:
    print(", ".join(result))  # print(*result, sep=', ')
else:
    print("error")
