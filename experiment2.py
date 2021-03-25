import math

supported_ops = ('+-*/^sqrt')

ops = {'+':2, '-':2, '/':1, '*':1, '^':0}

INPUT = input("Введите выражение: ").replace(' ', '')

stack = []
OUTPUT = []
digit = False
INPUT = list(INPUT)
result = ''
variables = ['']
variables1 = []
operations = []
oper = []
operand = []
stroka = []
# 2+sqrt2 = 2+2^0.5

for i, letter in enumerate(INPUT):
    if letter in '+-*/^' and (i > 0) and variables[len(operations)] != '':
        operations.append(letter)
        variables.append('')
    else:
        index = len(operations)
        variables[index] = variables[index] + letter


for i in range(max(len(variables), len(operations))):
    if i < len(variables):
        stroka.append(variables[i])
    if i < len(operations):
        stroka.append(operations[i])


for i, l in enumerate(stroka):
    if 'sqrt' in l and '-' in l:
        oper.append('-(' + stroka[i].split('sqrt').pop())
        oper.append('0.5)')
        operand.append('^')
       
    elif 'sqrt' in l:
        oper.append(stroka[i].split('sqrt').pop())
        oper.append(0.5)
        operand.append('^')
    elif 'sin' in l:
        oper.append(stroka[i].split('sin').pop())
        b = float(oper.pop())
        c = str(math.sin(b))
        oper.append(c)
    elif 'cos' in l:
        oper.append(stroka[i].split('cos').pop())
        b = float(oper.pop())
        c = str(math.cos(b))
        oper.append(c)
    else:
        if l in '0123456789.' or ('-' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l))):
            oper.append(l)
        else:
            operand.append(l)

stroka.clear()


for i in range(max(len(oper), len(operand))):
    if i < len(oper):
        stroka.append(str(oper[i]))
    if i < len(operand):
        stroka.append(str(operand[i]))



for i, l in enumerate(stroka):
    if '-' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l)):
        stroka[i] = str('(0' + stroka[i] + ')')


INPUT = ''.join(stroka)


for i in INPUT:
    
    if i in '0123456789.':
        if len(OUTPUT) == 0:
            OUTPUT = [i] + OUTPUT
        else:
            if OUTPUT[0][-1] in '0123456789.' and digit: OUTPUT[0] += i
            else: OUTPUT = [i] + OUTPUT
        digit = True
    else: digit = False
    
    if i == '(':
        stack = [i] + stack
    
    if i == ')':
        while stack != [] and stack[0] != '(': OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
        if stack != [] and stack[0] == '(': stack = stack[1:]
    
    if i in ops:
        while stack != [] and stack[0] in ops and ops[i] >= ops[stack[0]]: OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]
        stack = [i] + stack

while stack != []: OUTPUT, stack = [stack[0]] + OUTPUT, stack[1:]


for i, l in enumerate(OUTPUT):
    if '^' in str(l) and '^' in str(OUTPUT[i+2]):
        OUTPUT[i+1], OUTPUT[i+2] = OUTPUT[i+2], OUTPUT[i+1]

OUTPUT = " ".join(reversed(OUTPUT))


polskiu = []

for i in OUTPUT.split():
    if i == '*':
        g = float(polskiu.pop())
        z = float(polskiu.pop())
        polskiu.append(g * z)
    elif i == '-':
        g = float(polskiu.pop())
        z = float(polskiu.pop())
        polskiu.append(z - g)
    elif i == '+':
        g = float(polskiu.pop())
        z = float(polskiu.pop())
        polskiu.append(g + z)
    elif i == 'sqrt':
        g = polskiu.pop()
        polskiu.append(g ** 0.5)
    elif i == '^':
        g = float(polskiu.pop())
        z = float(polskiu.pop())
        polskiu.append(z ** g)
    elif i == '/':
        g = float(polskiu.pop())
        z = float(polskiu.pop())
        if g == 0:
            print("На ноль делить нельзя")
            result = 'inf'
            break
        else:
            polskiu.append(z / g)
    else:
        polskiu.append(str(i))


if result == 'inf':
    print(result)
else:
    print("Результат: " + str(polskiu[0]))