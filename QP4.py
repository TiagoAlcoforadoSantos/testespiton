nomes_lista=[]
from collections import Counter

with open("lista_nomes.txt","w")as arquivo:
    while True:
        menu=input("Digite sair para sair ou continuar para continuar: ").lower()
        if menu=='sair':
            break
        else:
            nomes=input("Digite o nome: ").lower()
            nomes_lista.append(nomes)
            arquivo.write(f"{nomes}\n")

with open("lista_nomes.txt","r") as arquivo:
    for linha in arquivo:
        nome=linha.strip()
        if nome:
            nomes_lista.append(nome.lower())

    contagem_nomes= Counter(nomes_lista)
    duplicados = [nome for nome, count in contagem_nomes.items() if count > 1]
    if duplicados:
        print("\nOs seguintes nomes apareceram mais de uma vez:")
        for nome_duplicado in duplicados:            
            print(f"- {nome_duplicado.capitalize()}: {contagem_nomes[nome_duplicado]} vezes")
    else:
        print("\nNenhum nome duplicado foi encontrado no registro.")