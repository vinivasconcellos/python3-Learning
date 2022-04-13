extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    n = int(input('Digite um número: '))
    if n in range(0, 21):
        break
    print('Tente novamente.', end='')
print(f'Você digitou {extenso[n]}.')

#if n in range(0, 20):
#    print(f'Você digitou {extenso[n]}.')
