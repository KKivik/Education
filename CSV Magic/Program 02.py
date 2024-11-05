fin = open("File 01.csv", "r")

statistics = dict()

# Первая строка нас не интересует: это заголовок таблицы.
# Просто прочитаем эту строку и пропустим её.
fin.readline()

students = []

# А вот все последующие строки нам уже интересны.
for s in fin:
    ln, fn, patr, cl, yb, email = s.rstrip("\n").split(";")
    student = (ln, fn, patr, cl, int(yb), email)
    students.append(student)

fin.close()

students.sort()
print(*students, sep="\n")
print(students)  # Лучше так: print(*students, sep="\n")
