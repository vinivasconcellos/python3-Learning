from time import sleep
c = ('\033[m',
     '\033[0;30;41m',
     '\033[0;30;42m',
     '\033[0;30;44m',
     '\033[5;30m'
     );


def ajuda(com):
    título(f'Acessando o Manual do Comando \'{com}\'', 3)
    print(c[2], end='')
    help(com)
    print(c[0], end='')
    sleep(2)


def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('-' * tam)
    print(f'  {msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


#Main Program
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input('Função ou Biblioteca > '))
    if comando.upper() != 'FIM':
        ajuda(comando)
    else:
        break
título('ATÉ LOGO!', 3)
