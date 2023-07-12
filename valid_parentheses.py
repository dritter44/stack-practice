def valid_parenthesis(s):
    stack = []
    
    for i in s:
        if i == '(' or i == '{' or i == '[':
            stack.append(i)
            last = i
        elif i == ')'and len(stack) >0:
            if stack[-1] == '(':
                stack.pop()
            else:
                return False
        elif i == '}'and len(stack) >0:
            if stack[-1] == '{':
                stack.pop()
            else: 
                return False
        elif i == ']'and len(stack) >0:
            if stack[-1] =='[':
                stack.pop()
            else: 
                return False
        else:
            return False

    if len(stack) != 0:
        return False
    else: 
        return True

print(valid_parenthesis('(){}[]'))