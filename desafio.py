import datetime

nomearq = datetime.datetime.now().strftime("%Y%m%d")

certas = 0
erradas = 0

print('')
print('----------------------------------------------')

for linha in open(nomearq) :
	campos = linha.split('|')

	print (campos[0])
	print('')
	print ('1) ' + campos[1])
	print ('2) ' + campos[2])
	print ('3) ' + campos[3])
	print('')

	resposta = input('Escolha uma opção: ')
	print('resposta = ' + resposta)
	print ('campo 4 eh ' + campos[4])

	if resposta.strip() == campos[4].strip():
		certas += 1
		print ("Você acertou! \o/ ")
	else:
		erradas += 1
		print ("Você se enganou")

	print('----------------------------------------------')
	print('')

print ('Respostas corretas: ' + str(certas))
print ('Respostas incorretas: ' + str(erradas))
print('')
