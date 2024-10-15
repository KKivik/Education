#with open('results.txt', 'w', encoding='utf-8') as fout:
#    print("Moscow never sleeps!", file=fout)
#    a, b = 10, 20
#    print(a, '+', b, '=', a + b, file = fout)

with open('1.txt', 'w', encoding='utf-8') as writer:
    for i in range(15):
        writer.write(str(i) +  ' ')
