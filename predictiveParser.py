def parse(input_str, table, start_symbol):
    stack = ['$', start_symbol]   # init stack with "$" and start of stack
    i = 0                         # init 'i'

    while len(stack) > 1:         # keep going until "$" is left in stack
        top = stack[-1]           # get the top symbol
        symbol = input_str[i]     # get input symbol
        print(f'Current Symbol: "{symbol}" --> Stack: {stack}') # OUTPUT BOTH

        if (top, symbol) in table:  # look for production rule for current symbol
            stack.pop()             # then remove the top symbol
            production = table[(top, symbol)]   # retrieve production rule
            print(f"Applied Rule: {top} -> {production}")   # output which rule it used

            if production != 'ɛ':   # as long as prod rule isnt empty
                stack.extend(reversed(production))  # push the rule onto stack in reverse order

        elif top == symbol: # error tracking, check if top is same as new symbol
            stack.pop() # pop if it is
            i += 1  # iterate to next one

        else:   # IF NO prod rule found & top isnt same, return false for acceptance
            return False

    print(f'Final Stack: {stack}')  # output final stack
    return i == len(input_str) - 1 and stack[0] == '$'  # return if input string is done iterating & stack has end symbol

table = {   # PRODUCTION RULES USED AS A REFERENCE
    ('E', 'a'): 'TQ', ('E', '('): 'TQ', ('Q', '+'): '+TQ', ('Q', '-'): '-TQ',
    ('Q', ')'): 'ɛ', ('Q', '$'): 'ɛ', ('T', 'a'): 'FR', ('T', '('): 'FR',
    ('F', 'a'): 'a', ('F', '('): '(E)', ('R', '*'): '*FR', ('R', '/'): '/FR',
    ('R', '+'): 'ɛ', ('R', '-'): 'ɛ', ('R', ')'): 'ɛ', ('R', '$'): 'ɛ',
}

for input_str in ['(a+a)$']:    # tested with this input string, can try other ones
    print(f'Input: {input_str}\nAccepted: {parse(input_str, table, "E")}\n')
    print(f'---------------------------------------------------------------')
