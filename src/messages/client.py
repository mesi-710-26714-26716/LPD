#!/usr/bin/env python3
#
# Mestrado em Engenharia de Segurança da Informação
# Linguangem de programacao Dinamica - LPD - Python - Prof. Armando Ventura
# Aluno: Lino Silva - 26714
# Módulo: client.py - modulo para troca de mensagem segura, lado cliente
# Exibe o resultao na tela
# Criado em 06/02/2026
# Historio de modificacoes:
# 06/02/2026 - Alterado para adicionar msg de Fim conexao
#
import socket
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.fernet import Fernet

SERVER_IP = "127.0.0.1"
PORT = 9000

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((SERVER_IP, PORT))

# Recebe chave pública
public_pem = sock.recv(2048)
public_key = serialization.load_pem_public_key(public_pem)

# Gera chave AES
aes_key = Fernet.generate_key()
cipher = Fernet(aes_key)

# Envia chave AES cifrada
encrypted_key = public_key.encrypt(
    aes_key,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)
sock.sendall(encrypted_key)

print("[+] Canal seguro estabelecido")
print("Digite 'Fim comunicacao' para terminar")

while True:
    msg = input("Mensagem: ")

    encrypted_msg = cipher.encrypt(msg.encode())
    sock.sendall(encrypted_msg)

    data = sock.recv(4096)
    response = cipher.decrypt(data).decode()
    print("Servidor:", response)

    if msg == "Fim comunicacao":
        break

sock.close()
print("[+] Comunicacao finalizada pelo cliente")

