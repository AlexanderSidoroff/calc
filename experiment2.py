
supported_ops = ('+-*/^')

ops = {'+':2, '-':2, '/':1, '*':1, '^':0}

INPUT = input("Введите выражение: ").replace(' ', '')

stack = []
OUTPUT = []
digit = False



for i in INPUT:
    
    if i in '0123456789':
        if len(OUTPUT) == 0:
            OUTPUT = [i] + OUTPUT
        else:
            if OUTPUT[0][-1] in '0123456789' and digit: OUTPUT[0] += i
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
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(g * z)
    elif i == '-':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(z - g)
    elif i == '+':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(g + z)
    elif i == '^':
        g = polskiu.pop()
        z = polskiu.pop()
        polskiu.append(z ** g)
    elif i == '/':
        g = polskiu.pop()
        z = polskiu.pop()
        if g == 0:
            print("На ноль делить нельзя")
        else:
            polskiu.append(z / g)
    else:
        polskiu.append(int(i))
print("Результат: " + str(polskiu[0]))