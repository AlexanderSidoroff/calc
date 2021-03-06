str_command = input("Please type command a+b or a-b: ")

str_A = ''
str_B = ''
operation = ''

for letter in str_command:
    print(letter)
    if letter == '+' or letter == '-' or letter == '*' or letter == '/' or letter == '^':
        operation = letter
    else:
        if operation == '':
            str_A = str_A + letter
        else: 
            str_B = str_B + letter

str_A = str_A.strip()
str_B = str_B.strip()
print(str_A)
print(str_B)
 
delimoe = float(str_A)
#print(type(a))

delitel = float(str_B)
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