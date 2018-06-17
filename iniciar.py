from broadcast_client import *
from tcp_client import *
from projetoforca import *

udp = udpclient()
ip = udp.loop()
cli = cliente(ip)
cli.enviar("entrei")
resposta = cli.receber()

if resposta == "True":
	cli.enviar("escolha")
	dados = cli.receber()	
	print resposta
	cli.enviar("quemjoga")
	quemjoga = cli.receber()	
	print quemjoga
	jogo(cli, dados, quemjoga)
