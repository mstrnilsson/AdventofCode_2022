def part(charnumber: int) -> None:
    with open("06/input.txt") as f:
        line = f.readlines()[0]
        i = len(line)
        for i in range(0, i - charnumber):
            if len(set(line[i : i + charnumber])) == charnumber:
                print(i + charnumber)
                return

if __name__ == "__main__":
    part(4)
    part(14)