# Parse File

def remove_comments(program:list) -> list:
    for i, line in enumerate(program):
        newLine = line.split("//")[0]
        program[i] = newLine
    program = [line for line in program if line != ''] # Removes all blank '' lines
    return program

def parse_file(path: str) -> None:
    program = []
    with open(path, "r") as file:
        for line in file:
            line = line.replace(" ", "")
            line = line.replace("\n", "")
            if line: # Doesn't add empty strings
                program.append(line)
            # print(line, end="")
    program = remove_comments(program)
    return program

program = parse_file(r"C:\Users\ryabinkyj\Documents\programming other\nand2tetris\projects\06\max\Max.asm")
print(program)
print(*program, sep='\n')