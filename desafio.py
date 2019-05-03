import datetime
import sys

print('----------------------------------------------')
print('')

print ('Você já tomou banho?')
print ('1) Sim')
print ('2) Não')

resposta = input('Escolha uma opção: ')

if resposta.strip() == '2':
	print('Só pode jogar depois do banho.')
else:
	
	jogador = sys.argv[1].strip()
	
	dia_yyyymmdd = datetime.datetime.now().strftime("%Y%m%d")
	nome_arq_perguntas = 'perguntas/' + jogador + dia_yyyymmdd
	
	arq_certas = jogador + 'certas'
	arq_erradas = jogador + 'erradas'
	
	acum_certas = int(open(arq_certas).readline())
	acum_erradas = int(open(arq_erradas).readline())
	
	certas = 0
	erradas = 0
	
	print('')
	print('----------------------------------------------')
	
	for linha in open(nome_arq_perguntas) :
		campos = linha.split('|')
	
		print (campos[0])
		print('')
		print ('1) ' + campos[1])
		print ('2) ' + campos[2])
		print ('3) ' + campos[3])
		print('')
	
		resposta = input('Escolha uma opção: ')
	
		if resposta.strip() == campos[4].strip():
			certas += 1
			print ("Você acertou! \o/ ")
		else:
			erradas += 1
			print ("Você se enganou...")
	
		print('')
		print('----------------------------------------------')
		print('')
	
	print ('Respostas corretas: ' + str(certas))
	print ('Respostas incorretas: ' + str(erradas))
	print('')
	
	acum_certas += certas
	acum_erradas += erradas
	
	f = open(arq_certas,"w+")
	f.write(str(acum_certas))
	f = open(arq_erradas,"w+")
	f.write(str(acum_erradas))
	
	print ('Total de corretas: ' + str(acum_certas))
	print ('Total de incorretas: ' + str(acum_erradas))
	
	
