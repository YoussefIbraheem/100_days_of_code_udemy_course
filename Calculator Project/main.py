from art import logo

def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def multiply(n1 , n2):
    return n1 * n2

def divide(n1 , n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    print(logo)
    should_accumulate = True
    num1 = int( input("input your first number: ") )

    while should_accumulate:
        chosen_operation = input("Pick an operation: ")
        if not chosen_operation in operations:
            should_accumulate = False
            print("invalid operation")
            print("\n" * 20)
            calculator()

        num2 = int( input("What is the next Number") )

        result = operations[chosen_operation](num1,num2)
        print(f"{num1} {chosen_operation} {num2} = {result}")
        should_continue = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ")

        if should_continue.lower() == 'y':
            num1 = result
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()


calculator()



