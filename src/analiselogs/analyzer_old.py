#!/usr/bin/env python3
#
# Mestrado em Engenharia de Segurança da Informação
# Linguangem de programacao Dinamica - LPD - Python - Prof. Armando Ventura
# Aluno: Lino Silva - 26714
# Módulo: analyzer.py - Analisa arquivo de log fornecido pelo professor ufw.log.
# Exibe o resultao na tela
# Criado em 05/02/2026
# Historio de modificacoes:
# 05/02/2026 - Adicionei Geolocalizacao pelo database GeoLite2-Country.mmdb
# 06/02/2026 - Otimizacao na leitura do bando de geolocalizacao
#
import re
from datetime import datetime
import geoip2.database
import os


LOG_FILE = os.path.join(os.path.dirname(__file__), "ufw.log")
GEOIP_DB = "/root/LPD/Projeto_Lino_26714/src/analiselogs/GeoLite2-Country.mmdb"

LOG_PATTERN = re.compile(
    r'(?P<timestamp>\w{3}\s+\d+\s[\d:]+).*'
    r'SRC=(?P<src>\S+).*'
    r'DST=(?P<dst>\S+)'
    r'(?:.*SPT=(?P<spt>\d+))?'
    r'(?:.*DPT=(?P<dpt>\d+))?'
)



def get_country(ip):
    """
    Retorna o país de origem de um IP
    """
    try:
        response = reader.country(ip)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return "Desconhecido"  # IP não encontrado no banco (ex: privado)
    except Exception as e:
        print(f"Erro GeoIP para {ip}: {e}")
        return "Desconhecido"

def analyze_logs():
    print("\n[ Análise de Logs UFW ]\n")

    if not os.path.exists(LOG_FILE):
        print("Ficheiro de log não encontrado.")
        return

    with open(LOG_FILE, "r") as file:
        lines = file.readlines()

    for line in lines:
        match = LOG_PATTERN.search(line)
        if match:
            timestamp = match.group("timestamp")
            src_ip = match.group("src")
            dst_ip = match.group("dst")
            spt = match.group("spt") or "N/A"
            dpt = match.group("dpt") or "N/A"

            country = get_country(src_ip)

            print(f"Timestamp : {timestamp}")
            print(f"Origem    : {src_ip} ({country})")
            print(f"Destino   : {dst_ip}")
            print(f"Porta Src : {spt}")
            print(f"Porta Dst : {dpt}")
            print("-" * 40)


def run():
    # Abra o banco uma vez só
    reader = geoip2.database.Reader(GEOIP_DB)
    analyze_logs()
    reader.close()
