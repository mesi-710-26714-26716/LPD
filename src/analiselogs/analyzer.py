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
import os
import geoip2.database
import geoip2.errors

# Caminhos
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(BASE_DIR, "ufw.log")
GEOIP_DB = os.path.join(BASE_DIR, "GeoLite2-Country.mmdb")

# Regex para logs UFW
LOG_PATTERN = re.compile(
    r'(?P<timestamp>\w{3}\s+\d+\s[\d:]+).*'
    r'SRC=(?P<src>\S+).*'
    r'DST=(?P<dst>\S+)'
    r'(?:.*SPT=(?P<spt>\d+))?'
    r'(?:.*DPT=(?P<dpt>\d+))?'
)

# Reader global
reader = None


def get_country(ip):
    """
    Retorna o país de origem de um IP
    """
    try:
        response = reader.country(ip)
        return response.country.name
    except geoip2.errors.AddressNotFoundError:
        return "Privado/Desconhecido"  # IP privado ou não mapeado
    except Exception as e:
        print(f"Erro GeoIP para {ip}: {e}")
        return "Desconhecido"


def analyze_logs():
    print("\n[ Análise de Logs UFW ]\n")

    if not os.path.exists(LOG_FILE):
        print("Ficheiro de log não encontrado.")
        return

    with open(LOG_FILE, "r") as file:
        for line in file:
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
    global reader
    reader = geoip2.database.Reader(GEOIP_DB)
    analyze_logs()
    reader.close()
