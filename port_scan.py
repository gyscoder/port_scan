#!/bin/python

import sys
import socket
from datetime import datetime

#set
target = ''
horario = str(datetime.now())
#defina o alvo

if len(sys.argv) == 2:
        target = socket.gethostbyname(sys.argv[1]) #traduz o hostname para ipv4
else:
        print("[-] Quantia de argumentos invalidos! [-]")
        print("[!] Sintaxe: python3 port_scan.py <ip/host> [!]")

#estética, add um banner
print("-" * 50)
print("[!] Alvo de varredura {} [!]".format(target))
print("[--:--] Tempo em que começou {} [--:--]".format(horario[0:19]))
print("-" * 50)

try:
        for port in range(1, 65535):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                socket.setdefaulttimeout(1)
                result = s.connect_ex((target, port)) #retorna um erro, se a porta estiver aberta retorna 0, se nao estiver aberta ele retorna 1
                #print("[+] Checando porta {}  [+]".format(port)) #< mostra todas as portas que estao sendo checadas
                if result == 0:
                        print("[+] Porta {} esta aberta [+]".format(port))
                s.close()

except KeyboardInterrupt:
        print("\n[!] Parando o scan [!]")
        sys.exit()

except socket.gaierror:
        print("[!] Hostname nao pode ser resolvida  [!]")
        sys.exit()

except socket.error:
        print("[!] Falha ao tentar se conectar ao servidor [!]")
        sys.exit()


