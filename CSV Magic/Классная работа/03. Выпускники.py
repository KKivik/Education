import csv


n = int(input())

fin = open('vps.csv', 'r', encoding='utf-8')

row_reader = csv.reader(fin, delimiter=';')

i = -1

for row in row_reader:
    i += 1 
    if i == 0:
        continue
    a, b, c, d, e, f = row
    e = int(e)
    if e >= n:
        print(a)

fin.close()
