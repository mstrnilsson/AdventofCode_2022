#!/usr/bin/env python3

import sys, operator

totals = []
score = 0
currentindex = 0
i=0



print('--- Day 2: Rock Paper Scissors ---')
for line in open('input.txt', 'r').readlines():
    line=line.strip()
    line=line.replace(" ", "")
    #print(line)
    totals.append({'index':currentindex, 'combination':line})
    i += 1
    if i == 3:
        currentindex += 1
        i = 0

"""
AX=piedra, pierdo tijera 3
BY=papel, empate papel 3 + 2
CZ=tijera, gano piedra 6 + 1
BX=papel, pierdo piedra 1
CY=tijera, empato tijera 3 + 3
AZ=piedra, gano papel 6 + 2
CX=tijera, pierdo papel 2
AY=piedra, empato piedra 3 + 1
BZ=papel, gano tijera 6 + 3
"""
for total in totals:
    if total["combination"] == 'AX':
        score += 3
    elif total["combination"] == 'BY':
        score += 5
    elif total["combination"] == 'CZ':
        score += 7
    if total["combination"] == 'BX':
        score += 1
    elif total["combination"] == 'CY':
        score += 6
    elif total["combination"] == 'AZ':
        score += 8
    if total["combination"] == 'CX':
        score += 2
    elif total["combination"] == 'AY':
        score += 4
    elif total["combination"] == 'BZ':
        score += 9
print(f'Total:\t {score}')




