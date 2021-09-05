# port_scan
port scan script in python, tested on kali linux


#!/bin/python 			< mostra o local do python

import sys 			< importa biblioteca sys, serve para executar comandos do sistema

import socket			< importa biblioteca socket, conexão com a rede

from datetime import datetime 	< importa biblioteca datetime, horarios, datas etc

#set

target = ''

horario = str(datetime.now())	< pega o horário e data atual do sistema

#defina o alvo


if len(sys.argv) == 2:		< se argumentos de sistema for igual a 2

	target = socket.gethostbyname(sys.argv[1]) #traduz o hostname para ipv4 < então target resolve hostname

else:				< caso contrário

	print("[-] Quantia de argumentos invalidos! [-]")		< mostra "[-] Quantia de argumentos invalidos! [-]"
        
	print("[!] Sintaxe: python3 port_scan.py <ip/host> [!]")	< mostra "[!] Sintaxe: python3 port_scan.py <ip/host> [!]"

#estética, add um banner

print("-" * 50)			< mostra 50 vezes um hífem

print("[!] Alvo de varredura {} [!]".format(target))			< mostra ("[!] Alvo de varredura <ip/host> [!]", .format insere dentro de {} o valor da variavel target

print("[--:--] Tempo em que começou {} [--:--]".format(horario[0:19]))	< mostra "[--:--] Tempo em que começou {} [--:--]".format(horario[0:19]), horario[0:19] é para selecionar somente até 2 digitos depois de minutos, caso contrário ele mostra milesegundos, mostra o dia, ano e mês também

print("-" * 50)


try:				< tente

	for port in range(1, 65535):					< para porta numa faixa de 1 até 65535
        
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)	< cria a conexão com o ip
                
		socket.setdefaulttimeout(1)				< define um tempo limite pra tentar conectar
                
		result = s.connect_ex((target, port)) 			#retorna um erro, se a porta estiver aberta retorna 0, se nao estiver aberta ele retorna 1        
		
		#print("[+] Checando porta {}  [+]".format(port)) 	#< mostra todas as portas que estao sendo checadas                
                
		if result == 0:						< se resultado for igual a zero
                
			print("[+] Porta {} esta aberta [+]".format(port))	< mostra a porta que está aberta
                
		s.close()						< fecha conexão


except KeyboardInterrupt:						< recebe uma excecao, no caso se o script for interrompido por um teclado/

	print("\n[!] Parando o scan [!]")				< mostra "[!] Parando o scan [!]", o “\n” quebra uma linha
        
	sys.exit()							< para o sistema


except socket.gaierror:							< recebe uma excecao, no caso de um hostname nao conseguir ser resolvido

	print("[!] Hostname nao pode ser resolvida  [!]")		< mostra "[!] Hostname nao pode ser resolvida  [!]"
        
	sys.exit()
	

except socket.error:							< recebe uma excecao, no caso de nao conseguir se conectar ao servidor

	print("[!] Falha ao tentar se conectar ao servidor [!]")	< mostra “[!] Falha ao tentar se conectar ao servidor [!]"
        
	sys.exit()
