def processar_votos(lista_votos):

    contador1 = 0 
    contador2 = 0 
    contador3 = 0 

    for voto in lista_votos:
        if voto == 1:
            contador1 += 1
        elif voto == 2:
            contador2 += 1
        else:
            contador3 += 1
    
    print("-" * 30)
    print(f"Resultado Final:")
    print(f"STAR WARS (Voto 1): {contador1} votos")
    print(f"STAR TREK (Voto 2): {contador2} votos")
    print(f"Nulos/Inválidos: {contador3} votos")
    print("-" * 30)

    resultados = [
        (contador1, "STAR WARS"),
        (contador2, "STAR TREK")
    ]

    resultados.sort() 

    menor_votado_votos, menor_votado_nome = resultados[0]
    maior_votado_votos, maior_votado_nome = resultados[-1]


    if contador1 == contador2:
        print("Houve um empate entre Star Wars e Star Trek.")
    else:
        print(f"O MAIOR votado foi: [{maior_votado_nome}] com [{maior_votado_votos}] votos.")
        print(f"O MENOR votado foi: [{menor_votado_nome}] com [{menor_votado_votos}] votos.")
    
    print("-" * 30)



print("QUAL FILME VOCE PREFERE? STAR WARS vote 1 STAR TREK vote 2")


with open("votacao.txt","w", encoding='utf-8') as arquivo:

    for x in range(10): 
        voto=input("Digite aqui seu voto: ")
        arquivo.write(f"{voto}\n")
    print("VOTOS COMPUTADOS E SALVOS")


votacao_inteiros = []
with open("votacao.txt","r", encoding='utf-8') as arquivo:
    for linha in arquivo:
        string_voto = linha.strip() 
        try:
            voto_int = int(string_voto)
            votacao_inteiros.append(voto_int)
        except ValueError:
            print(f'ERRO: Voto inválido "{string_voto}" ignorado.')
            votacao_inteiros.append(0)


processar_votos(votacao_inteiros)