
import re

i, j, k = 0, 0, 0
totalcontain, totaloverlap = 0, 0
sectiondict={}
with open("04/input.txt") as f:
    for line in f:
        pairs=re.search(r'([0-9]*)\-([0-9]*)\,([0-9]*)\-([0-9]*)',line)
        sectiondict.setdefault(i, [])
        sectiondict[i].append(list((range((int(pairs.group(1))),(int(pairs.group(2)))+1))))
        sectiondict[i].append(list((range((int(pairs.group(3))),(int(pairs.group(4)))+1))))
        i += 1
    
for list in sectiondict:
    if (set(sectiondict[j][0]).issubset(sectiondict[j][1])) or (set(sectiondict[j][0]).issuperset(sectiondict[j][1])) == True:
        totalcontain += 1
        j += 1
    else:
        j += 1
    if (set(sectiondict[k][0]).isdisjoint(sectiondict[k][1])) == False:
        totaloverlap += 1
        k += 1
    else:
        k += 1
print(f'The amount assignment pairs that has one range fully contain the other:\t{totalcontain}')
print(f'The amount assignment pairs that the ranges overlap:\t{totaloverlap}')
    