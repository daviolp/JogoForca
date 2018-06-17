import thread
import random
from broadcast_server import *
from socket import *
import time
class servidor(): 
    def __init__(self):
        self.serverPort = 12000
        self.serverSocket = socket(AF_INET,SOCK_STREAM)
        self.serverSocket.bind(('',self.serverPort))
        self.serverSocket.listen(1)
        self.usuarios = []
        self.nomes = {}    
        self.loop()

    def tudocerto(self):
        if ((len(self.usuarios)) % 2 == 0):
            self.usuarios[len(self.usuarios)-1].send("True")
            self.usuarios[len(self.usuarios)-2].send("True")
    def escolha(self, connectionSocket):
        num = self.usuarios.index(connectionSocket)
        if (num % 2) == 0:
            palavra = self.sortea()
            self.usuarios[num+1].send(palavra)
            self.usuarios[num].send(palavra)
    def sortea(self):
        atributos = [("arara","ave"), ("chapeu","acessorio"), ("cadeira","sentar"),("bola","jabulane"), ("livro","escritor"), ("flauta","instrumento musical"), ("carro","automovel"), ("casa","imovel"), ("salgadinho","feito de milho"), ("palheta","objeto que auxilia o musico"),("helicoptero","aeronave"), ("handeboll","esporte"), ("fotossintese","processo de alimentacao de uma planta"), ("butano","estrutura organica do gas de cozinha"), ("fundamentos-de-programacao","disciplina de redes de computadores"), ("sniper","arma de fogo de longo alcance"), ("raio","fenomeno da natureza"), ("aero-smit","banda de rock"), ("helton-jonh","cantor ingles"), ("rock","genero musical"), ("quadriciculo","motocicleta"), ("preparoxitona","regra gramatical da lingua portuguesa"), ("antropocentrismo","teoria de que o homem esta no centro de tudo "), ("ariano-suassuna","grande escritor brasileiro "), ("pneumoultramicroscopicossilicovulcanoconiose","maior palavra da lingua portuguesa registrada em um dicionario"), ("anticonstitucionalissimamente","quando a atitude vai contra a constituicao"), ("anne-frank","garota que escreveu um livro sofrendo sobre o holocausto nazista"), ("massachusetts","um dos estados do Estados Unidos"), ("otorrinolaringologista ","especialista nas partes do corpo como nariz, orelha,e garganta"), ("hipopotomonstrosesquipedaliofobia","doenca psicologica que se caracteriza pelo medo irracional de pronuciar palavras grandes ou complicados")]
        num = random.randint(0, 27)
        string = atributos[num][0]+"*"+atributos[num][1]      
        return string

    def quemjoga(self, conect):
        num = self.usuarios.index(conect)
        if (num % 2) == 0:
            self.usuarios[num+1].send("segundo")
            self.usuarios[num].send("primeiro")
    
    def receber(self,connectionSocket, addr):
        while 1:
            sentence = connectionSocket.recv(1024)
            print sentence
            try:
                nome = sentence.split("*")[1]
                sentence = sentence.split("*")[0]
            except:
                pass

            if sentence == "quemjoga":
                #time.sleep(randint(1,5))
                self.quemjoga(connectionSocket)
            elif sentence == "player":
                self.nomes[connectionSocket] = nome

            elif sentence == "quem":
                num = self.usuarios.index(connectionSocket)
                if (num % 2) == 0:
                    try:
                        valor = self.nomes[self.usuarios[num+1]]
                        self.usuarios[num].send("nome"+"*"+valor)
                    except:
                        pass
                else:
                    try:
                        valor = self.nomes[self.usuarios[num-1]]
                        self.usuarios[num].send("nome"+"*"+valor)
                    except:
                        pass
            elif sentence == "escolha":
                self.escolha(connectionSocket)    
            elif sentence == "entrei":
                self.usuarios.append(connectionSocket)
                self.tudocerto()
            else:
                num = self.usuarios.index(connectionSocket)

                if (num % 2) == 0:
                    print sentence
                    self.usuarios[num+1].send("letra"+"*"+sentence)
                else:
                    self.usuarios[num-1].send("letra"+"*"+sentence)

        connectionSocket.close()
        thread.exit()
    def udpserver(self, nada):
        udpserver()
    def loop(self):
        while 1:
            try:
                thread.start_new_thread(self.udpserver, tuple([""]))
                connectionSocket, addr = self.serverSocket.accept()
                thread.start_new_thread(self.receber, tuple([connectionSocket, addr]))
            except:
                thread.exit()
                self.serverSocket.close()

servidor()