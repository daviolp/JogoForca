# -*- coding: utf-8 -*-
import os
import random
import time
import threading



def jogo(cli, dados, quemjoga):
	def forca(num, nome):
		if num == 0:
			print '''
	---------------+
	               |
	               |
	               |
	               |
	               |
	_______________|	
	'''
		elif num == 1:
			print '''
	----------------+
	  o             |
	                |
	                |
	                |
	                |
	 _______________|
	'''
		elif num == 2:
			print '''
	----------------+
	  o             |
	 /              |
	                |
	                |
	                |
	 _______________|
	'''
		elif num == 3:
			print '''
	----------------+
	  o             |
	 /|             |
	                |
	                |
	                |
	 _______________|
	'''
		elif num == 4:
			print '''
	----------------+
	  o             |
	 /|\            |
	                |
	                |
	                |
	 _______________|
	'''
		elif num == 5:
			print '''
	----------------+
	  o             |
	 /|\            |
	 /              |
	                |
	                |
	 _______________|
	'''
		elif num == 6:
			
			print '''
	----------------+
	 \o/            |
	  |             |
	 / \            |
	                |
	                |
	 _______________|
	'''		
			print "-----------------------------------+"
			print "-----------------------------------|"
			print "--VOCE ESGOTOU O LIMITE DE CHANCES-|"
			print "-----------------------------------|"
			print "-----------------------------------|"
			print "-----------------------------------|"
			print "***********************************************************"
			print " A palavra era", nome
			print "************************************************************"

	def lacunas(name):
		vazio = ""
		for letra in nome:
			if letra == "-":
				vazio += letra
			else:
				vazio += "*"
		return vazio
			
	# atributos_facil = [("arara","ave"), ("chapeu","acessorio"), ("cadeira","sentar"),("bola","jabulane"), ("livro","escritor"), ("flauta","instrumento musical"), ("carro","automovel"), ("casa","imovel"), ("salgadinho","feito de milho"), ("palheta","objeto que auxilia o musico")]
	# atributos_moderado = [("helicoptero","aeronave"), ("handeboll","esporte"), ("fotossintese","processo de alimentacao de uma planta"), ("butano","estrutura organica do gas de cozinha"), ("fundamentos-de-programacao","disciplina de redes de computadores"), ("sniper","arma de fogo de longo alcance"), ("raio","fenomeno da natureza"), ("aero-smit","banda de rock"), ("helton-jonh","cantor ingles"), ("rock","genero musical")]
	# atributos_dificil = [("quadriciculo","motocicleta"), ("preparoxitona","regra gramatical da lingua portuguesa"), ("antropocentrismo","teoria de que o homem esta no centro de tudo "), ("ariano-suassuna","grande escritor brasileiro "), ("pneumoultramicroscopicossilicovulcanoconiose","maior palavra da lingua portuguesa registrada em um dicionario"), ("anticonstitucionalissimamente","quando a atitude vai contra a constituicao"), ("anne-frank","garota que escreveu um livro sofrendo sobre o holocausto nazista"), ("massachusetts","um dos estados do Estados Unidos"), ("otorrinolaringologista ","especialista nas partes do corpo como nariz, orelha,e garganta"), ("hipopotomonstrosesquipedaliofobia","doenca psicologica que se caracteriza pelo medo irracional de pronuciar palavras grandes ou complicados")]
	# num = random.randint(0, 9)


	op = True
	nome = dados.split("*")[0]
	dica = dados.split("*")[1]

	recebi = []

	def central():
		nome = cli.receber()
		try:
			if nome.split("*")[0] == "nome":
				recebi.append(nome.split("*")[1])
		except:
			pass		
		return True

	def main(a, b, c):
		nome = a
		dica = b
		asterisco = c
		le_inva = []#aqui e o vetor
		cont_erros = 0

		"""
		while cont_erros <= 6:
			os.system("clear")
			forca(cont_erros,nome)
			print "A palavra e","-----------------------", asterisco
			print "--------------------------------------------------------------"
			print "A DICA E",dica
			print "--------------------------------------------------------------"
			print "Essas sao as letras que ja foram usadas: ", le_inva
			print "--------------------------------------------------------------"
			tenta = raw_input("Digite uma letra: ")
			le_inva.append(tenta)
			
			if tenta in nome:    #aqui verifica se a letra esta na palavra e se nao estiver,printa a forca de acordo com os numeros de erros 
				var = "" 
				for i in nome:
					if i == tenta:
						var += i
					elif i in le_inva or i == "-":
						var += i
					else:
						var += "*"
				asterisco = var
			else:
				cont_erros += 1
			if asterisco == nome:
				print "----------------------------------------------"
				print "Voce acertou!!!!!", "A palavra era",",",asterisco
				break
			if cont_erros == 6:
				forca(cont_erros,nome)
				break
		"""
	while op == True:
		os.system("clear")
		
		print '''
				BEM-VINDO AO JOGO DA FORCA!!!!

			Algumas Regras para o jogo: 

		1:Não digite números,palavras ou espaços.
		2:Não repita letras certas.

		Pronto para começar?

		Se sim, digite "sim"!

		'''
		modo_de_jogo = raw_input("Digite aqui:  ")

		"""
		if modo_de_jogo == "a":
			while True:
				os.system("clear")
				print "Modo: Jogador 1"
				print "---------------------------------------------"
				op = False
				print "Escolha a dificudade:"
				print "a)Facil"
				print "b)moderado"
				print "c)dificil"
				escolha_dificudade = raw_input(": ")
				print "--------------------------"
				
				if escolha_dificudade == "a":
					# nome = atributos_facil[num][0]
					# dica = atributos_facil[num][1]
					print "Vamos la!!!"
					print "---------------------"
					break
				elif escolha_dificudade == "b":
					print "---------------"
					print "Vamos la!!!"
					# nome = atributos_moderado[num][0]
					# dica = atributos_moderado[num][1]
					break
				elif escolha_dificudade == "c":
					print "---------------"
					print "Vamos la!!!"
					# nome = atributos_dificil[num][0]
					# dica = atributos_dificil[num][1]
					break
				else:
					print "opcoes invalidas"
			
			
			
		"""	
		asterisco = lacunas(nome)
		#main(nome, dica, asterisco)

		if modo_de_jogo == "sim":
			os.system("clear")
			continuar = 1
			
			jogador = raw_input("nome do jogador: ")
			cli.enviar("player"+"*"+jogador)
			if quemjoga == "primeiro":
				ordem = True
				jogador_1 = jogador
				teste=True
				t1 = threading.Thread(target=central)
				t1.start()

				while teste:
					cli.enviar("quem")
					if len(recebi) != 0:
						jogador_2 = recebi[0]
						teste = False
						
					time.sleep(1)	
			else:
				ordem = False
				jogador_2 = jogador
				teste=True
				t1 = threading.Thread(target=central)
				t1.start()
				while teste:
					cli.enviar("quem")
					if len(recebi) != 0:
						jogador_1 = recebi[0]
						teste = False
					
					time.sleep(1)	
			# jogador_2 = raw_input("nome do jogador2: ")
			
			

			while continuar == 1:
				le_inva = []

				vez_jogador = jogador_1
				cont = 0

				while cont <= 6:
					os.system("clear")

					forca(cont, nome)

					print "sua vez", vez_jogador
					#aposta = 5
					
					print "A palavra é", asterisco
					print "--------------------------------"
					print "A dica é", dica
					print "--------------------------------"
					#print "cada letra valera: ", aposta
					print "--------------------------------"
					print "Essas são as letras usadas ", le_inva
					print "---------------------------------"
					#print jogador_1, ":", placar1, "pontos"
					#print jogador_2, ":", placar2, "pontos"
					print "--------------------------------"
					
					if ordem:
						tenta = raw_input("Digite uma letra: ")
						cli.enviar(tenta)
					else:
						teste = True
						while teste:
							tenta = cli.receber()
							if tenta.split("*")[0] == "letra":
								tenta = tenta.split("*")[1]
								teste = False
					
					le_inva.append(tenta)


					if tenta in nome:
						var = ""
						for i in nome:
							if i == tenta:
								var += i
							
							elif i in le_inva:
								var += i
							
							else:
								var += "*"
								
						asterisco = var
						
						#if vez_jogador == jogador_1:
						#	placar1 += aposta
						
						#else:
						#	placar2 += aposta
					
					else:
						if vez_jogador == jogador_1:
							vez_jogador = jogador_2
							
							if ordem == True:
								ordem = False
							else:
								ordem = True
						
						else:
							
							vez_jogador = jogador_1
							if ordem == True:
								ordem = False
							else:
								ordem = True

					if tenta not in nome:
						cont += 1
						forca(cont, nome)


					"""
					if cont == 6:
						forca(cont, nome)
						break
					"""
					if asterisco == nome:
						os.system("clear")
						print "----------------------------------------------"
						print "A palavra era",",",asterisco
						"""
						if placar1 > placar2:
							print jogador_1, "voce acertou a palavra mizeravi", "seu placar foi de", placar1
						elif placar2 > placar1:
							print jogador_2, "voce acertou a palavra mizeravi", "seu placar foi de", placar2
						else:
							print "empate"
						"""
						fim = raw_input("Você deseja continuar o jogo: ")
						if fim == "nao" or fim == "sim":
							continuar = 0
						break
                    	
		else:
			print "opção inválida"		
			print "------------------------------------------------"