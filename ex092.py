from datetime import datetime
empregado = {}
empregado['nome'] = str(input('Nome: '))
empregado['anonasc'] = int(input('Ano de Nascimento: '))
empregado['carteira'] = int(input('Nº Carteira de Trabalho: '))
if empregado['carteira'] != 0:
    empregado['anocontrat'] = int(input('Ano de contratação: '))
    empregado['salario'] = float(input('Salário: '))
    empregado['idade'] = datetime.now().year - empregado['anonasc']
    anoaposent = empregado['anocontrat'] + 35
    empregado['aposent'] = empregado['anocontrat'] + 35 - empregado['anonasc']
    print(f'{empregado["nome"]}, que nasceu em '
          f'{empregado["anonasc"]}, tem carteira '
          f'de trabalho nº {empregado["carteira"]}, '
          f'hoje tem {empregado["idade"]} anos e vai '
          f'se aposentar com {empregado["aposent"]} anos.')
else:
    print(f'{empregado["nome"]}, com ano de nascimento de {empregado["anonasc"]}, possui carteira de trabalho nº {empregado["carteira"]}.')
#print(empregado)
