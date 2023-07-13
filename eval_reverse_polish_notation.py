# input of tokens
from operator import add, sub, floordiv, mul


def eval_reverse_polish_notation(tokens):
    # initiate num stack and operand stack
    num_stack = []
    operator_dict = {'+':add, '-':sub, '*':mul, '/': floordiv}
    ans = 0
    base = 0
    base2 = 0
    for i in range(len(tokens)):
        # push leading integers to the stack
        if tokens[i] is int:
            num_stack.append(tokens.pop(i))
        
        # if an operator is encountered, establish base operation
        elif tokens[i] is not int:
            base = int(num_stack.pop())
            base2 = int(num_stack.pop())
            ans = operator_dict[i](base2,base)
            num_stack.append(ans)
        # if operator is encountered and base already set, pop 1 int and move ahead with operations
        # if tokens[i] is not int and base != 0:
        #     base2 = int(num_stack.pop())
        #     ans = operator_dict[i](base2,base)
        #     base=ans
    return ans

    # establish base 

def leet_code_answer(tokens):
    stack =[]
    for c in tokens:
        if c == "+":
            stack.append(stack.pop()+stack.pop())
        elif c == "-":
            a,b = stack.pop(), stack.pop()
            stack.append(b-a)
        elif c == "*":
            stack.append(stack.pop()*stack.pop())
        elif c == "/":
            a, b = stack.pop(), stack.pop()
            stack.append(int(b/a))
        else:
            stack.append(int(c))
    return stack[0]