import datetime
import sys

dia_yyyymmdd = datetime.datetime.now().strftime("%Y%m%d")
jogador = sys.argv[1].strip()
nome_arq_perguntas = 'perguntas/' + jogador + dia_yyyymmdd


try:
	open(nome_arq_perguntas)

	print('----------------------------------------------')
	print('')
	
	lista_bloqueios = open('bloqueios').read().splitlines()
	conteudo_bloqueio = lista_bloqueios[int(sys.argv[2])].split('|')
	
	print (conteudo_bloqueio[0])
	print ('1) Sim')
	print ('2) Não')
	
	resposta = input('Escolha uma opção: ')
	
	if resposta.strip() != '1':
		print('')
		print(conteudo_bloqueio[1])
		print('----------------------------------------------')
		print('')
	else:
		
		arq_certas = jogador + 'certas'
		arq_erradas = jogador + 'erradas'
		
		acum_certas = int(open(arq_certas).readline())
		acum_erradas = int(open(arq_erradas).readline())
		
		certas = 0
		erradas = 0
		
		print('')
		print('----------------------------------------------')
		print('')
		
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
				print ("Você se enganou... A resposta correta era a " + campos[4])
		
			print('')
			print('----------------------------------------------')
			print('')
		
		print ('Respostas corretas: ' + str(certas))
		print ('Respostas incorretas: ' + str(erradas))
		print('')

		for linha_premiacao in open('premiacao'):
			campos = linha_premiacao.split('|')

			if int(campos[0]) > acum_certas and acum_certas + certas >= int(campos[0]):
				print(campos[1])

		
		acum_certas += certas
		acum_erradas += erradas
		
		f = open(arq_certas,"w+")
		f.write(str(acum_certas))
		f = open(arq_erradas,"w+")
		f.write(str(acum_erradas))
		
		print ('Total de corretas: ' + str(acum_certas))
		print ('Total de incorretas: ' + str(acum_erradas))

	
	
except (OSError, IOError) as e:
	print('******************************************')
	print(' Hoje não tem desafio. ')
	print('******************************************')
