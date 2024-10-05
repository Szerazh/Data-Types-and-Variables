input_a = int(input())
input_b = int(input())

print(f'Before:')
print(f'a = {input_a}')
print(f'b = {input_b}')

input_a, input_b = input_b, input_a

print(f'After:')
print(f'a = {input_a}')
print(f'b = {input_b}')
