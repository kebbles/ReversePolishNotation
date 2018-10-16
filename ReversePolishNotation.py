def reversePolish(string):
    stack = []
    expression = string.split(' ')
    for i in expression:
        result = i
        if i in ['+','-','/','*']:
            num2 = int(stack.pop())
            num1 = int(stack.pop())
            if i == '+':
                result = num1 + num2
            elif i == '-':
                result = num1 - num2
            elif i == '*':
                result = num1 * num2
            else:
                result = num1 / num2
        stack.append(result)
    return stack

def main():
    while input("Continue?") == 'y':
        expression = input("Enter an expression\n")
        print(reversePolish(expression))
    

main()
