import csv


data = [
    {'lastname': 'Иванов', 'firstname': 'Пётр', 'class_number': '9', 'class_letter': 'А'},
    {'lastname': 'Кузнецов', 'firstname': 'Алексей', 'class_number': 9, 'class_letter': 'В'},
    {'lastname': 'Меньшова', 'firstname': 'Алиса', 'class_number': 9, 'class_letter': 'А'},
    {'lastname': 'Иванова', 'firstname': 'Татьяна', 'class_number': 9, 'class_letter': 'Б'}
]

fout = open('Другие ученики.csv', 'w', newline='')

row_writer = csv.DictWriter(fout,
                    fieldnames=['lastname', 'firstname', 'class_number', 'class_letter'],
                    delimiter=';')
#последнее значит, что все загнано в формат строки кроме чисел
row_writer.writeheader()

for d in data:
    row_writer.writerow(d)

fout.close()
