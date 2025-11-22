def triangulo(numero_alvo):
    if numero_alvo<6:
        return False,None
    raiz_cubica=int(numero_alvo**(1/3))-1
    for n in range(raiz_cubica, raiz_cubica+5):
        if n<1: continue
        produto=n*(n+1)*(n+2)
        if produto==numero_alvo:
            return True,(n,n+1,n+2)
        elif produto>numero_alvo:
            break
    return False,None
try:
    num=int(input("Digite o  numero: "))
    if num<0:
        print("ERRO: DIGITE UM NUMERO POSITIVO")
    else:
        is_triangular, fatores=triangulo(num)
        if is_triangular:
            n,n2,n3=fatores
            print(f"o numero: [{num}] é triangular, pois [{n}]*[{n2}]*[{n3}]=[{num}]")
        else:
            print(f"o numero [{num}] não é triangular")
except Exception as erro:
    print(f'ERRO DE [{erro}]')