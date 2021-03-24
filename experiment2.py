
supported_ops = ('+-*/^sqrt')

ops = {'+':2, '-':2, '/':1, '*':1, '^':0, 'sqrt':0}

INPUT = input("Введите выражение: ").replace(' ', '')

stack = []
OUTPUT = []
digit = False
INPUT = list(INPUT)
result = ''
variables = ['']
operations = []
stroka = []


for i, letter in enumerate(INPUT):
    if letter in '+-*/^' and (i > 0) and variables[len(operations)] != '':
        operations.append(letter)
        variables.append('')
    else:
        index = len(operations)
        variables[index] = variables[index] + letter

print(variables)
print(operations)

for i in range(max(len(variables), len(operations))):
    if i < len(variables):
        stroka.append(variables[i])
    if i < len(operations):
        stroka.append(operations[i])

print(stroka)

for i, l in enumerate(stroka):
    if '-' in str(l) and ('1' in str(l) or '2' in str(l) or '3' in str(l) or '4' in str(l) or '5' in str(l) or '6' in str(l) or '7' in str(l) or '8' in str(l) or '9' in str(l)):
        stroka[i] = str('0' + stroka[i])


INPUT = ''.join(stroka)


print(INPUT)
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

print('инфиксная запись:\t%s' % (INPUT))
print('постфиксная запись:\t%s' % (" ".join(reversed(OUTPUT))))
OUTPUT = " ".join(reversed(OUTPUT))
print(OUTPUT)

# выражение 2+2*2 в польской 222*+, считаем:

'''
выражение l = 222*+ - OUTPUT     range {0, 1 , 2, 3, 4}
          i = 01234
'''


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