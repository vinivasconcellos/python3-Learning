teste = []
teste.append('Vinícius')
teste.append(31)
galera = []
galera.append(teste[:])
teste[0]='Maria'
teste[1]=62
galera.append(teste[:])
print(galera)
