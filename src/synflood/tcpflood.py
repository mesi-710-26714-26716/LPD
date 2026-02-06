#!/usr/bin/env python3
#
# Mestrado em Engenharia de Segurança da Informação
# Linguangem de programacao Dinamica - LPD - Python - Prof. Armando Ventura
# Aluno: Lino Silva - 26714
# Módulo: synflood.py - Faz ataque DoS via TCP para um IP selecionado.
# Exibe o resultao na tela
# Criado em 06/02/2026
# Historio de modificacoes:
# 06/02/2026 - 
#
import socket
import sys


import socket
import sys

def tcpflood():
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(2)

    print("Teste de conectividade TCP")

    ip = input("IP de destino: ").strip()
    port = input("Porta: ").strip()

    try:
        server_address = (ip, int(port))
        sock.connect(server_address)
        print("Conexão TCP estabelecida com sucesso!")

        for i in range(1,200):
           message = f"Mensagem TCP nº {i}".encode()
           sock.sendall(message)
           print(f"Enviada: {message.decode()}")
           try:
              data = sock.recv(1024)
              print("Resposta recebida:", data.decode(errors="ignore"))
           except socket.timeout:
              print("Sem resposta do servidor (timeout)")

    except ConnectionRefusedError:
        print("Conexão recusada pelo destino (porta fechada)")

    except KeyboardInterrupt:
        print("Execução interrompida pelo utilizador (CTRL+C)")

    except socket.timeout:
        print("Tempo de conexão excedido (possível firewall)")

    except ValueError:
        print("Porta inválida")

    except socket.gaierror:
        print("IP ou hostname inválido")

    except socket.error as e:
        print(f"Erro de socket: {e}")

    finally:
        sock.close()
        print("Socket fechado")

def run():
    tcpflood()
