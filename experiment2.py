str_command = input("Введите выражение: ").replace(' ', '')

variables = ['']
operations = []
stroka = []
stek1 = list([])
stek2 = list([])
x = float()
y = float()
operation = ''
result = ''
for i, letter in enumerate(str_command):
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

#приоритеты
hp_ops = tuple('^')
mp_ops = tuple('*/')
lp_ops = ('+', '-')
#калькулятор

def top(stek2):
    return stek2[len(stek2)-1]

for i in range(len(stroka)):
    if stroka[i] not in '+-*/^':
        print(stroka[i])
        stek1.append(stroka[i])
    else:
        if stroka[i] in '+-*/^' and stek2 == []:
            stek2.append(stroka[i])
        else:
            if stek2 != []:
                if stroka[i] in hp_ops and top(stek2) in lp_ops:
                    stek2 = stek2.append(stroka[i])
                elif stroka[i] in hp_ops and top(stek2) in mp_ops:
                    stek2 = stek2.append(stroka[i])
                elif stroka[i] in hp_ops and top(stek2) in hp_ops:
                    x = stek1.pop()
                    y = stek1.pop()
                    operation = stek2.pop()
                    x = float(x)
                    y = float(y)
                    result = y**x
                    stek1.append(result)
                    stek2.append(stroka[i])
                elif stroka[i] in mp_ops and (top(stek2) in hp_ops or top(stek2) in mp_ops):
                    operations = stek2.pop()
                    x = stek1.pop()
                    y = stek1.pop()
                    x = float(x)
                    y = float(y)
                    stek2.append(stroka[i])
                    if operation == '/':
                        result = y / x
                        stek1.append(result)
                    elif operation == '*':
                        result = y * x
                        stek1.append(result)
                elif stroka[i] in mp_ops and top(stek2) in lp_ops:
                    stek2.append(stroka[i])
                elif stroka[i] in lp_ops and (top(stek2) in lp_ops or top(stek2) in mp_ops or top(stek2) in hp_ops):
                    operation = stek2.pop()
                    x = stek1.pop()
                    y = stek1.pop()
                    x = float(x)
                    y = float(y)
                    stek2.append(stroka[i])
                    if operation == '+':
                        result = y + x
                        stek1.append(result)
                    elif operation == '-':
                        result = y - x
                        stek1.append(result)

i = 0
i = int(i)
if stek2 != []:
    while i < len(stek2):
        x = stek1.pop()
        y = stek1.pop()
        x = float(x)
        y = float(y)
        operation = stek2.pop()
        if operation == '/':
            if x == 0:
                result = 'Inf'
            else:
                result = y / x
                stek1.append(result)
        elif operation == '+':
            result = y + x
            stek1.append(result)
        elif operation == '-':
            result = y - x
            stek1.append(result)
        elif operation == '*':
            result = y * x
            stek1.append(result)
        elif operation == '^':
            result = y ** x
            stek1.append(result)
        else:
            result = "Unknown"
print(stek1)
print(stek2)
