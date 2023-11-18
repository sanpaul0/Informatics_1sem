def operation(num1, num2, oper):  # 2 3 - 12 10 - * 4 2 / +
    #global res
    res = 0
    if oper == '+':
        res = float(num2) + float(num1)
    if oper == '-':
        res = float(num1) - float(num2)
    if oper == '*':
        res = float(num2) * float(num1)
    if oper == '/':
        res = float(num1) / float(num2)
    return res


def polish_answer():
    polish = input().split()
    try:
        operations = ['+', '-', '*', '/']
        count = 0
        simple_polish = []
        for i in range(len(polish)):
            if i >= len(polish):
                break
            if polish[count] not in operations and polish[count + 1] not in operations:
                simple_polish.append(str(operation(float(polish[count]), float(polish[count + 1]), polish[count + 2])))
                polish.remove(polish[count])
                polish.remove(polish[count])
                polish.remove(polish[count])
            else:
                count += 1
        print(simple_polish)
        print(polish)
    except ValueError:
        print('SyntaxError')
        exit(0)
    if len(simple_polish) - 1 != len(polish):
        return SyntaxError
    for i in range(len(polish)):
        simple_polish[i + 1] = operation(simple_polish[i], simple_polish[i + 1], polish[i])
    return simple_polish[-1]


print(polish_answer())
