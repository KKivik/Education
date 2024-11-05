import csv

fin = open("File 03.csv", "r")

row_reader = csv.reader(fin, delimiter=';', quotechar='"')

#print(*row_reader)
for row in row_reader:
    print(row)

fin.close()
