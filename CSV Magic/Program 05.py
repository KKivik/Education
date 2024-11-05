import csv


fout = open('Квадраты.csv', 'w', newline='')

row_writer = csv.writer(fout, delimiter=';',
                        quotechar='"', quoting=csv.QUOTE_MINIMAL)
#последнее означает, что разбрасываться кавычками не нужно
for i in range(10):
    row_writer.writerow([i, i ** 2, f"Квадрат числа {i} равен {i ** 2}"])

fout.close()
