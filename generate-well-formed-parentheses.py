# leetcode solution as I was not abe to come up with one
def generate_parentheses(n):
    # ")" must only come after "("
    # all parentheses appended to ans
    stack = []
    res = []
    # start recursive function to backtrack through and generate different combos of parentheses
    def backfunction(openN,closedN):
        if openN == closedN == n:
            res.append("".join(stack))
            return
        if openN < n:
            stack.append("(")
            backfunction(openN+1,closedN) #initiate backfunciton(1,0), then backfunction(2,0), (2,1) etc
            stack.pop() #pop the open parentheses off, send to next if statement. this generates new combos
        if closedN < openN:
            stack.append(")")
            backfunction(openN,closedN+1)
            stack.pop()
    backfunction(0,0) #initiate backtrack function
    return res