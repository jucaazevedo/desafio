import datetime

nomearq = datetime.datetime.now().strftime("%Y%m%d")

print('----------------------------------------------')

for linha in open(nomearq) :
	campos = linha.split('|')

	print (campos[0])
	print ('1)' + campos[1])
	print ('2)' + campos[2])
	print ('3)' + campos[3])

	resposta = input('Escolha uma opção: ')
	print('resposta = ' + resposta)
	print ('campo 4 eh ' + campos[4])

	if resposta == campos[4]:
		print ("Você acertou! \o/ ")
	else:
		print ("Você se enganou")

	print('----------------------------------------------')
