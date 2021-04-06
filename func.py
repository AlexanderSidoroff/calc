def parse_command(command: str) -> list:
    parsedlone = command.replace(' ', '')
    res = list(parsedlone)
    return res

def calc(command: str) -> float:
    precalc = ''.join(parse_command(command))
    res = eval(precalc)
    return res

def getfromfile(file_name: str):
    with open(file_name, 'r') as f:
        line = f.readline()
    return line
    

import sys
if len(sys.argv) <= 1:
    command = input("Введите выражение:")
    print(calc(command))
else:
    filename = sys.argv[1]
    command = getfromfile(filename)    
    print(calc(command))
    with open('output.txt', 'w') as f:
        f.writelines(str(calc(command)))
    
