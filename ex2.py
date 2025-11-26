longas=0
repitidas=0
total=0
with open("texto.txt","r") as arquivo:
        conteudo=arquivo.read()

with open("relatorio.txt","w") as arquivo:
  arquivo.write(conteudo)

with open("relatorio.txt","r") as arquivo:
    for linha in arquivo:
        total+=1
        frase=linha.strip()
        if len(frase)>80:
            longas+=1
        palavras=frase.lower()
        for p in set(palavras):
            if palavras.count(p)>=3:
                repitidas+=1
                break
with open("relatorio.txt","w",encoding="UTF-8") as arquivo:
    arquivo.write(f"total de palavras repitidas[{repitidas}]\n")
    arquivo.write(f"total de frases longas[{longas}]\n")
    arquivo.write(f"Total de linhas[{total}]")