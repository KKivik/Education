fin = open("File 01.csv", "r")

statistics = dict()

# Первая строка нас не интересует: это заголовок таблицы.
# Просто прочитаем эту строку и пропустим её.
fin.readline()

# А вот все последующие строки нам уже интересны.
for s in fin:
    a, b, c, d, e, f = s.rstrip("\n").split(";")
    A = [a, b, c, d, int(e), f]
    print(A)

fin.close()
