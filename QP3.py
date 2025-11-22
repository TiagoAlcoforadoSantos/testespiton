import os


NOME_ARQUIVO = "numero.txt"

def ler_numero_do_arquivo():
    """Lê o número armazenado no arquivo. Retorna 0 se o arquivo não existir ou estiver vazio."""
    if not os.path.exists(NOME_ARQUIVO):
        return 0
    try:
        with open(NOME_ARQUIVO, 'r', encoding='utf-8') as arquivo:
            conteudo = arquivo.read().strip()
            if conteudo:

                return int(conteudo)
            else:
                return 0
    except ValueError:

        print(f"Erro: O arquivo '{NOME_ARQUIVO}' contém dados inválidos.")
        return 0
    except IOError as e:
        print(f"Erro ao ler o arquivo: {e}")
        return 0

def escrever_numero_no_arquivo(novo_numero):
    """Escreve um novo número no arquivo, sobrescrevendo o anterior."""
    try:
        with open(NOME_ARQUIVO, 'w', encoding='utf-8') as arquivo:

            arquivo.write(str(novo_numero))
        print(f"Sucesso: O novo número [{novo_numero}] foi salvo no arquivo.")
    except IOError as e:
        print(f"Erro ao escrever no arquivo: {e}")

def menu_principal():
    """Função principal que gerencia o menu e a lógica do programa."""
    while True:
        print("\n--- MENU DE OPÇÕES ---")
        print("[1] Ler o número atual do arquivo")
        print("[2] Escrever (atualizar) um novo número")
        print("[3] Sair")
        print("----------------------")
        
        opcao = input("Escolha uma opção (1, 2 ou 3): ").strip()

        if opcao == '3':
            print("Saindo do programa. Até mais!")
            break
        elif opcao == '1':

            numero_atual = ler_numero_do_arquivo()
            if numero_atual > 0:
                print(f"O número atualmente armazenado é: [{numero_atual}]")
            else:
                print("O arquivo está vazio ou não existe.")
        elif opcao == '2':

            try:

                novo_numero_str = input("Digite o novo número inteiro a ser comparado/salvo: ").strip()
                novo_numero_int = int(novo_numero_str)
                

                numero_existente = ler_numero_do_arquivo()

                if novo_numero_int > numero_existente:
                    print(f"Comparação: O novo número [{novo_numero_int}] é MAIOR que o existente [{numero_existente}].")
                    escrever_numero_no_arquivo(novo_numero_int)
                else:
                    print(f"Comparação: O novo número [{novo_numero_int}] NÃO é maior que o existente [{numero_existente}].")
                    print("O arquivo não foi atualizado.")

            except ValueError:
                print("Entrada inválida. Por favor, digite apenas números inteiros.")
        else:
            print("Opção inválida. Por favor, escolha 1, 2 ou 3.")

if __name__ == "__main__":
    menu_principal()