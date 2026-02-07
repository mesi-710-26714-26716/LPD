#!/usr/bin/env python3
#
# Mestrado em Engenharia de Segurança da Informação
# Linguangem de programacao Dinamica - LPD - Python - Prof. Armando Ventura
# Aluno: Lino Silva - 26714
# Módulo: scanport.py - Solicita um endereço IP ou subrede e faz scan das portas disponviveis.
# Exibe o resultao na tela
# Criado em 05/02/2026
# Historio de modificacoes:
# 05/02/2026 - Exibir o IP mesmo que nao tenha porta aberta ou IP for inalcansavel 
# 07/02/2026 - Melhria no codigo para exibir as portass abertas durante o scan 
# 
import socket
import ipaddress


COMMON_PORTS = [21, 22, 23, 25, 53, 80, 110, 139, 143, 443, 445, 3306, 8080]


def scan_port(ip, port, timeout=0.5):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(timeout)
        result = sock.connect_ex((str(ip), port))
        sock.close()

        if result == 0:
            return "Aberta"
        else:
            return "Fechada"
    except socket.timeout:
        return "Sem resposta(pode estar bloqueada)"
    except socket.error:
        return "Erro"

def scan_host(ip):
    open_ports = []

    for port in COMMON_PORTS:
        status = scan_port(ip, port)
        print(f"{ip}:{port} -> {status}")

        if status == "Aberta":
            open_ports.append(port)

    return open_ports

def run():
    print("\n[ Scanner de Portos de Rede ]\n")
    target = input("Introduza um IP ou subrede (ex: 192.168.1.10 ou 192.168.1.0/24): ")

    try:
        network = ipaddress.ip_network(target, strict=False)
    except ValueError:
        print("Formato de IP ou subrede inválido.")
        return

    print(f"\nInício do scan em: {network}\n")

    for ip in network.hosts():
        print(f"\n--- Scan em {ip} ---")
        ports = scan_host(ip)

        if ports:
            print(f"[+] {ip} -> Portos abertos encontrados: {ports}")
        else:
            print(f"[-] {ip} -> Nenhuma porta aberta detectada")

    print("\nScan concluído.\n")
