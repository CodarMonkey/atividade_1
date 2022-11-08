aluno = 'Wallace Salvador Ferreira da Silva'
ru = '3923326'
print(f"------------Aluno: {aluno}, Ru: {ru}------------")

tr = {'p': 6, 'm': 10, 'g': 18, 'tr': 'Sabores Tradicionais'}
es = {'p': 7, 'm': 12, 'g': 21, 'es': 'Sabores Especiais'}
pr = {'p': 8, 'm': 14, 'g': 24, 'pr': 'Sabores Premium'}
crr = [] #guarda os valos dos pedidos
cg = ''
tp = ''
pd = [] #guarda pedidos
cont = 0
lpd = 'p', 'm', 'g'
lpt = 'tr', 'es', 'pr'


#---------------------------Inicio função cadapio-------------------------------
def cdp():#

    linha = [['TR', 'Sabores-Tradicionais', 'R$ 6,00', 'R$ 6,00', 'R$ 6,00'], # lista cardapio
             ['ES', 'Sabores-Especiais', 'R$ 7,00', 'R$ 12,00', 'R$ 21,00'],
             ['PR', 'Sabores-Premium', 'R$ 8,00', 'R$ 14,00', 'R$ 24,00']]

    # Codigo, Descricao, Tamanho_P, Tamanho_M, Tamanho_G = linha1, linha2, linha3, linha4, linha5
    print(f"{'-' * 31}Cardapio{'-' * 30}")
    print('{:<15}{:<18}{:<13}{:<13}{:<13}'.format('Codigo',    # imprime cabechalho do cardapio
                                                  'Descricao',
                                                  'Tamanho_P',
                                                  'Tamanho_M',
                                                  'Tamanho_G'))

    for v in linha: # imprime tabela de codigos e valores
        Codigo, Descricao, Tamanho_P, Tamanho_M, Tamanho_G = v
        print('{:<7}{:<26}{:<13}{:<13}{:<13}'.format(Codigo, Descricao,
                                                     Tamanho_P, Tamanho_M, Tamanho_G))
    print(f"{'-' * 69}")#
#---------------------------Fim função cadapio-------------------------------


#-----------------------Inicio função de novo pedido----------------------------
def Npedido():
    np = input('Quer adicionar mais itens? S(Sim) N(Não): ')
    if np == 's':
        pedido()
    elif np == 'n':
        tt = float(sum(crr))
        print(f'Valor total R$ {tt:.2f}')
#-----------------------Fim função de novo pedido----------------------------


#-----------------------Inicio função de pedido----------------------------
def pedido():
    tp = input('Informe o tamanho do pode (P/M/G): ')
    while tp not in lpd:
        print('Tamanho ou codigo invalido')
        tp = input('Informe o tamanho do pode (P/M/G): ')

    cg = input('Informe o código do sorvete TR/ES/PR: ')
    while cg not in lpt:
        print('Tamanho ou codigo invalido')
        cg = input('Informe o código do sorvete TR/ES/PR: ')

    if cg == 'tr':
        cr = tr[tp]
        crr.append(tr[tp])
        print(f'Você pediu um sorvete Tradicional, tamanho {tp.upper()}, R$ {float(cr)}')
    elif cg == 'es':
        #pd.append()
        cr = es[tp]
        crr.append(es[tp])
        print(f'Você pediu um sorvete Especial, tamanho {tp.upper()}, R$ {float(cr)}')
    elif cg == 'pr':
        cr = pr[tp]
        crr.append(pr[tp])
        print(f'Você pediu um sorvete Premium, tamanho {tp.upper()}, R$ {float(cr)}')
    Npedido()
#-----------------------Fim função pedido----------------------------


cdp()
pedido()
