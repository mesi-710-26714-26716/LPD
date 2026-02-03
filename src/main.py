#!/usr/bin/env python3
"""
LPD - Projeto de Segurança Informática
Mestrado em Engenharia de Segurança da Informação
Lino Silva - 26714
Módulo principal (CLI)
"""

def show_menu():
    print("\n==============================")
    print(" Ferramenta de Segurança LPD ")
    print("==============================\n")

    print("Selecione uma opção:")
    print("1 - Scanner de Portos de Rede")
    print("2 - Análise de Logs de Serviços")
    print("3 - Serviço de Mensagens Seguras")
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
        print("Opção selecionada: Scanner de Portos de Rede")
    elif option == 2:
        print("Opção selecionada: Análise de Logs de Serviços")
    elif option == 3:
        print("Opção selecionada: Serviço de Mensagens Seguras")
    elif option == 4:
        print("Opção selecionada: Port Knocking (SSH)")
    elif option == 5:
        print("Opção selecionada: Password Manager")
    else:
        print("Opção inválida. Por favor execute novamente a aplicação.")

    print("------------------------------\n")


if __name__ == "__main__":
    main()

