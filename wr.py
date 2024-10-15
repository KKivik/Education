fout = open('results.txt', 'w', encoding='utf-8')

# fout.write("Moscow never sleeps!\n") #не поставив \n строки не будут на разных строках и 1 запишется поверх другой
# fout.write('Москва никогда не спит!')

print("Moscow never sleeps!", file=fout)

a, b = 10, 20
print(a, '+', b, '=', a + b, file = fout)

fout.close()
