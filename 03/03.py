import os

def part1():

    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 53)))
    charlist=[]
    total=0

    with open("03/input.txt") as f:
            lines = f.readlines()
            for line in lines:
                comprt1 = line[:len(line)//2]
                comprt2 = line[len(line)//2:]
                common_characters = ''.join(set(comprt1).intersection(comprt2))
                charlist.append({'item': common_characters, 'count': value[common_characters]})
            for charlist in charlist:
                total += charlist['count']
    print(f'The sum of priorities part 1:\t{total}')

def part2():
    char = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    value = dict(zip("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", range(1, 53)))
    charlist=[]
    total=0   
    i=0
 
    with open("03/input.txt") as f:
            lines = f.read().splitlines()
            for line in lines:
                if i < len(lines):
                    charlist.append(lines[i])
                    charlist.append(lines[i+1])
                    charlist.append(lines[i+2])
                    common = ''.join(set.intersection(*map(set,charlist)))
                    total += value[common]      
                    i += 3
                    charlist=[]
    print(f'The sum of priorities part 2:\t{total}')

if __name__ == "__main__":
    part1()
    part2()