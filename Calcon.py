str_input = input("A: ")
A = float(str_input)
#print(type(A))
operation = input("+ / * - ^")

str_input2 = input("B: ")
B = float(str_input2)
#print(type(B))

if operation == '/':
    if B == 0:
        result = 'Inf'
    else:
        result = A / B
elif operation == '+':
    result = A + B
elif operation == '-':
    result = A - B
elif operation == '*':
    result = A * B
elif operation == '^':
    result = A ** B
else:
    result = "unknown"
#print(type(result))
print("Result: " + str(result))