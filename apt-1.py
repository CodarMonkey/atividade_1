aluno = 'Wallace Silva'
ru = '3236'
print(f"------------Aluno: {aluno}, Ru: {ru}------------")

#-------------Inicio função imprime os resultados finais-------------------
def total():# função imprime valor total
    print(f'Valor total sem o frete R$ {vt:.2f}')# valor sem frete
    print(f'Valor total com frete R$ {vtf:.2f}')# valor com frete
    print(f'Valor do frete R$ {vtf - vt:.2f}')# valor  do frete
#-------------Fim função imprime os resultados finais-------------------

try:
    nome = input("Qual seu nome: ")  # Nome do usuario utilizador

    fp = {11: 30, 101: 60, 1001: 120, 1002: 240}  # Dicioario quantidade e preço

    print(f'Sejá bem vinda(o) {nome}')  # Boas vindas
    vp = float(input(f'Informe o valor do produto {nome}: ').replace(',','.'))  #Pede Valor do produto


    qp = int(input(f'Informe a quantidade de produtos {nome}: '))  # Quantidade de produtos


    if qp <= fp[11]:# vericação de quantidade
        vt = qp * vp
        vtf = vt + fp[11]
        total()
    elif qp <= fp[101]:# vericação de quantidade
        vt = qp * vp#
        vtf = vt + fp[101]
        total()
    elif qp <= fp[1001]:# vericação de quantidade
        vt = qp * vp
        vtf = vt + fp[1001]
        total()
    else:
        vt = qp * vp
        vtf = vt + fp[1002]
        total()
except ValueError:
    print('Quantidade de produto deve ser um inteiro')
