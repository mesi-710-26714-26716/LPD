#!/usr/bin/env python3
#
# Mestrado em Engenharia de Segurança da Informação
# Linguangem de programacao Dinamica - LPD - Python - Prof. Armando Ventura
# Aluno: Lino Silva - 26714
# Módulo: main.py - Modulo principal, exibe as opcoes do projeto e executa cada modulo separadamente
# Exibe o resultao na tela
# Criado em 03/02/2026
# Historio de modificacoes:
# 05/02/2026 - Inclusao do modulo (1) 
# 05/02/2026 - Inclusao do modulo (2)
# 
from scanner import scanport
from analiselogs import analyzer
from udpflood import udpdos

def show_menu():
    print("\n==============================")
    print(" Ferramenta de Segurança LPD ")
    print("==============================\n")

    print("Selecione uma opção:")
    print("1 - Scanner de Portos de Rede")
    print("2 - Análise de Logs de Serviços")
    print("3 - UDP Flood para um IP")
    print("4 - Port Knocking (SSH)")
    print("5 - Password Manager")
    print("0 - Sair\n")


def get_user_option():
    try:
        option = int(input("Opção selecionada: "))
        return option
    except ValueError:
        return -1


def main():
    show_menu()
    option = get_user_option()

    print("\n------------------------------")

    if option == 0:
        print("A encerrar a aplicação.")
    elif option == 1:
        scanport.run() 
    elif option == 2:
        analyzer.run()
    elif option == 3:
        udpdos.run()
    elif option == 4:
        print("Opção selecionada: Port Knocking (SSH)")
    elif option == 5:
        print("Opção selecionada: Password Manager")
    else:
        print("Opção inválida. Por favor execute novamente a aplicação.")

    print("------------------------------\n")


if __name__ == "__main__":
    main()

