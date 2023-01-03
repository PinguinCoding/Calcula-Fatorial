num = int(input('Insira número: '))
fatorial = 1
count = num
print(f'{num}! = ', end='')
while count >= 1:
    fatorial *= count
    count -= 1
    print(count+1, end=' X ')
print(f'= {fatorial}')
