qtd=int(input("Digite numero: "))
with open("texto.txt","w") as arquivo:
    for x in range(qtd):
        txt=input("Digite algo: ")
        arquivo.write(f"{txt}\n")
with open("texto.txt", "r") as arquivo:
    print(arquivo.read())