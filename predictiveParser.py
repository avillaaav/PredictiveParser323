def parse(input_str, table, start_symbol):
    stack, i = ['$', start_symbol], 0
    while len(stack) > 1:
        top, symbol = stack[-1], input_str[i]
        print(f'Current Symbol: "{symbol}" --> Stack: {stack}')
        if (top, symbol) in table:
            stack.pop()
            production = table[(top, symbol)]
            print(f"Applied Rule: {top} -> {production}")
            if production != 'ɛ':
                stack.extend(reversed(production))
        elif top == symbol:
            stack.pop()
            i += 1
        else:
            return False
    print(f'Final Stack: {stack}')
    return i == len(input_str) - 1 and stack[0] == '$'

table = {
    ('E', 'a'): 'TQ', ('E', '('): 'TQ', ('Q', '+'): '+TQ', ('Q', '-'): '-TQ',
    ('Q', ')'): 'ɛ', ('Q', '$'): 'ɛ', ('T', 'a'): 'FR', ('T', '('): 'FR',
    ('F', 'a'): 'a', ('F', '('): '(E)', ('R', '*'): '*FR', ('R', '/'): '/FR',
    ('R', '+'): 'ɛ', ('R', '-'): 'ɛ', ('R', ')'): 'ɛ', ('R', '$'): 'ɛ',
}

for input_str in ['(a+a)$']:
    print(f'Input: {input_str}\nAccepted: {parse(input_str, table, "E")}\n')
    print(f'---------------------------------------------------------------')
