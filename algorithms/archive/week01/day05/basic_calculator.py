def get_num(exp, index) :
    result = 0

    while index < len(exp) and exp[index].isdigit() :
        result *= 10
        result += int(exp[index])
        index += 1

    return result, index

def process(exp, index) :
    result = 0
    sign = 1

    while index < len(exp) and exp[index] != ")" :
        if exp[index] == "(" :
            print("result " , result , " sign " , sign, " processing " , exp[index : ])
            number, index = process(exp, index + 1)
            number *= sign
            result += number
            sign = 1
        elif exp[index] == "+" :
            index += 1
            sign = 1
        elif exp[index] == "-" :
            index += 1
            sign = -1
        elif exp[index].isdigit() :
            number, index = get_num(exp, index)
            number *= sign
            result += number
            sign = 1
        else :
            index += 1

    return result , index + 1

def calculator(expression):
    result, _ = process(expression, 0)
    return result