# Projeto LPD – Ferramenta de Segurança em Redes

Projeto desenvolvido no âmbito da unidade curricular  
**Linguagem de Programação Dinâmica (LPD)**  
do **Mestrado em Engenharia de Segurança da Informação**.

A aplicação implementa uma ferramenta modular de segurança para análise de logs,
varrimento de portas, simulação de ataques e comunicação segura.

---

## Autor

- **Nome:** Lino Silva  
- **Nº Aluno:** 26714  
- **Curso:** Mestrado em Engenharia de Segurança da Informação  
- **UC:** Linguagem de Programação Dinâmica  
- **Docente:** Prof. Armando Ventura  

---

## Objetivos do Projeto

- Analisar eventos de segurança em sistemas Linux
- Identificar IPs de origem e respetiva localização geográfica
- Detetar tentativas de acesso não autorizado
- Realizar varrimentos de portas TCP
- Simular ataques para fins académicos
- Implementar comunicação segura cliente-servidor
- Produzir relatórios de segurança em CSV e PDF

---

## Estrutura do Projeto

```text
Projeto_LPD/
│
├── main.py
│
├── scanner/
│   └── scanport.py
│
├── analiselogs/
│   ├── analyzer.py
│   ├── ufw.log
│   ├── auth.log
│   └── GeoLite2-Country.mmdb
│
├── udpflood/
│   └── udpdos.py
│
├── synflood/
│   └── tcpflood.py
│
├── messages/
│   ├── server.py
│   └── client.py
│
├── requirements.txt
└── README.md

