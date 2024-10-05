qty_lines = int(input())

is_balanced = True
open_bracket = False

for i in range(qty_lines):
    current_input = input()

    if current_input == '(':
        if open_bracket == True:
            is_balanced = False
        else:
            open_bracket = True
    elif current_input == ')':
        if open_bracket == False:
            is_balanced = False
        else:
            open_bracket = False
    else:
        pass

if is_balanced == True:
    print(f'BALANCED')
else:
    print(f'UNBALANCED')
