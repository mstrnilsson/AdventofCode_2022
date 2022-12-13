import copy
def readtxt(table, instructions):

    with open("05/input.txt") as file:
        lines = file.readlines()
        for line in lines[0:8]:
            table.append([line[0:3],line[4:7],line[8:11],line[12:15],line[16:19],line[20:23],line[24:27], line[28:31],line[32:35]])

        for line in lines[10:512]:
            instructions.append([int(n) for n in line.split() if n.isdigit()])


def prepare_table(table, addrows, column_to, rows, last_table):
    f = -1
    
    if table[addrows][column_to] != "   ":

        while len(table) != addrows+rows:
            table.append([])

        for y in last_table:
            table[f]=last_table[f]
            f -= 1

        while f != -(len(table)+1):
            table[f]=["   ","   ","   ","   ","   ","   ","   ","   ","   "]
            f -= 1
    


def move_items1(table, addrows, column_to, column_from):
    b, c = -1, -1

    if table[addrows][column_to] == "   " and table[b][column_from] != "   ":

        for d in range(addrows):

            while table[b][column_from] != "   ":
                b -= 1
            move=table[b+d+1][column_from]
            table[b+d+1][column_from]= "   "
            while table[c][column_to] != "   ":
                c -=1
            table[c][column_to] = move
        


def move_items2(table, addrows, column_to, column_from):
    b, c = -1, -1
    
    if table[addrows][column_to] == "   " and table[b][column_from] != "   ":

        for d in range(addrows):

            while table[b][column_from] != "   ":
                b -= 1
            move=table[b+d+1][column_from]
            table[b+d+1][column_from]= "   "
            while table[c][column_to] != "   ":
                c -=1
            table[c-addrows+d+1][column_to] = move

    

def print_t(print_table, table):
    for z in table:
        if z != ["   ","   ","   ","   ","   ","   ","   ","   ","   "]:
            print_table.append(copy.copy(z))


def part1():
    for i in range(2):
        column_from, column_to, addrows, rows = 0, 0, 0, 0
        table=[]
        last_table=[]
        print_table=[]
        instructions=[]

        readtxt(table, instructions)
    
        if i==0:
            
            for addrows, y, z in instructions:
                
                column_from = y-1
                column_to = z-1
                
                rows = len(table)
                last_table = table[:].copy()
                
                prepare_table(table, addrows, column_to, rows, last_table)
                
                move_items1(table, addrows, column_to, column_from)

            print_t(print_table, table)
            print('\n\t----First part----')
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in print_table]))

        if i==1:

            for addrows, y, z in instructions:
                
                column_from = y-1
                column_to = z-1
                
                rows = len(table)
                last_table = table[:].copy()
                
                prepare_table(table, addrows, column_to, rows, last_table)

                move_items2(table, addrows, column_to, column_from)

            print_t(print_table, table)
            print('\n\t----Second part----\n')
            print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in print_table]))


if __name__ == "__main__":
    part1()