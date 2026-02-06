import geoip2.database

GEOIP_DB = "/root/LPD/Projeto_Lino_26714/src/analiselogs/GeoLite2-Country.mmdb"
reader = geoip2.database.Reader(GEOIP_DB)
response = reader.country("220.181.108.106")
print(response.country.name)  # Deve imprimir "United States"
reader.close()

