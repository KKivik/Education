import csv


fin = open("File 03.csv", "r")

row_reader = csv.DictReader(fin, delimiter=';', quotechar='"')

for row in row_reader:
    print(row['Класс'])

fin.close()