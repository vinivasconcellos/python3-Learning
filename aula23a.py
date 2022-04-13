try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
#Maneira geral:
#except:
#    print('Infelizmente deu erro :(')
#Maneira com classificação, mas que serve mais para o desenvolvedor saber, e não para aparecer na tela do usuário:
#except Exception as erro:
#    print(f'Problema encontrado foi {erro.__class__}')
#É possível fazer vários except:
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou.')
except ZeroDivisionError:
    print('Não é possível dividir um número por zero!')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados!')
except Exception as erro:
    print(f'Problema encontrado foi {erro.__cause__}')
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Volte sempre! Obrigado!')
