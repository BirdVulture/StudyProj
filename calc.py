
def main():
    calculation()

def input_value(seq):
    s = seq
    user_value = float(input(f"Введите значеие{s}: "))
    return user_value

def input_operation():
    user_operation = input('Введите операцию "*", "/", "+", "-": ')
    return user_operation

def addition(value_one, value_two):
    x = value_one
    y = value_two
    result = x + y
    return result

def substraction(value_one, value_two):
    x = value_one
    y = value_two
    result = x - y
    return result

def multiplication(value_one, value_two):
    x = value_one
    y = value_two
    result = x * y
    return result

def division(value_one, value_two):
    x = value_one
    y = value_two
    result = x / y
    return result

def calculation():
    value_one = input_value("1")
    operation = input_operation()
    value_two = input_value("2")
    if operation == "+":
        result = addition(value_one, value_two)
    if operation == "-":
        result = substraction(value_one, value_two)
    if operation == "*":
        result = multiplication(value_one, value_two)
    if operation == "/":
        result = division(value_one, value_two)
    
    print (value_one,operation,value_two,"=",result)



main()

