
import os

i = 0
j=0
total=0
fruitdict = {}
suma ={} 
with open("01/list.txt") as f:
    for num in f:
        if num == '\n':
            i += 1
        else:
            fruitdict.setdefault(i, [])
            fruitdict[i].append(int(float(num)))

suma = {key: sum(value) for key, value in fruitdict.items()}
orded = sorted(((v, k) for k, v in suma.items()), reverse=True)

for o, s in orded:
    if j < 3:
        print(f'Elf {s} - {o} calories')
        total += o
        j += 1
print(f'Total calories: {total}')


