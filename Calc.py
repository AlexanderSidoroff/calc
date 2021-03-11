str_command = input("Please type command a+b or a-b: ")

str_A = ''
str_B = ''

znak_A = ''
znak_B = ''

operation = ''

i = 0

while i < len(str_command) :
    if str_command[i] == '+' or str_command[i] == '-' or str_command[i] == '*' or str_command[i] == '/' or str_command[i] == '^' :
        if str_A == '': 
            znak_A = str_command[i]
        elif operation != '':
            znak_B = str_command[i]
        else:
            operation = str_command[i]
    else:
        if operation == '':
            str_A += str_command[i]
        else:
            str_B += str_command[i]
    i += 1
    

 
delimoe = float(znak_A + str_A)
#print(type(a))

delitel = float(znak_B + str_B)
#print(type(b))

if operation == '/':
    if delitel == 0:
        result = 'Inf'
    else:
        result = delimoe / delitel
elif operation == '+':
    result = delimoe + delitel
elif operation == '-':
    result = delimoe - delitel
elif operation == '*':
    result = delimoe * delitel
elif operation == '^':
    result = delimoe ** delitel
else:
    result = "unknown"
#print(type(result))
print("Result: " + str(result))