from pathlib import Path
from types import CommandTypes as T

class Parser():
    def __init__(self, file_path):
        self.file_path = file_path

    def __enter__(self):
        self.program = open(self.file_path, "r")
        self.current_line = self.program.readline().strip().replace("\n", "")
        return self
    
    def advance(self):
        line = self.program.readline()
        if line: # not eof
            self.current_line = line.strip().replace("\n","")
        else:
            self.current_line = None

    def command_type(self) -> None:
        line = self.current_line.split()
        if line: # Doesn't add empty strings
            match line[0]:
                case "add":
                    return T.ARITHMETIC
                case "sub":
                    return T.ARITHMETIC
                case "neg":
                    return T.ARITHMETIC
                case "eq":
                    return T.ARITHMETIC
                case "gt":
                    return T.ARITHMETIC
                case "lt":
                    return T.ARITHMETIC
                case "and":
                    return T.ARITHMETIC
                case "or":
                    return T.ARITHMETIC
                case "not":
                    return T.ARITHMETIC
                case "push":
                    return T.PUSH
                case "pop":
                    return T.POP
                case "label":
                    return T.LABEL
                case "goto":
                    return T.GOTO
                case "if-goto":
                    return T.IF
                case "function":
                    return T.FUNCTION
                case "return":
                    return T.RETURN
                case "call":
                    return T.CALL
        else:
            return T.END # Signals the end of the program
    
    def arg1(self):
        line = self.current_line.split()
        return line[1]
    
    def arg2(self):
        line = self.current_line.split()
        return line[2]

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()

path = r"C:\Users\ryabinkyj\Documents\programming other\nand2tetris\projects\07\MemoryAccess\BasicTest\BasicTest.vm"