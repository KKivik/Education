import sys
import csv


header = ['nomen', 'definitio', 'pluma', 'Russian nomen', 'familia', 'Russian nomen familia']

fout = open('plantis.csv', 'w', encoding='utf-8', newline='')

row_writer = csv.DictWriter(fout, fieldnames=header, delimiter=';')

row_writer.writeheader()

for line in sys.stdin:
    n, d, p, rn, f, rnf = line.rstrip('\n').split('\t')
    plant = {'nomen': n, 'definitio': d, 'pluma': p,
             'Russian nomen': rn, 'familia': f, 'Russian nomen familia': rnf}
    row_writer.writerow(plant)

fout.close()
