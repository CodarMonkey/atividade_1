m = ''
metrage = ''
tipo = ''
adnal = []
tb_adcional = {'1': 10, '2': 12, '3': 20}
tb_tipo = {'b': 1, 'c': 1.30}
metrimim = 30
metrimax = 700
metrmed = 300
mvmini = 60
mulmini = 0.3
mvmax = 120
multmax = 0.5

#----------------------Inicio função principal-----------------------------------
def main():
    iden()
    print("Bem vindo a Limpa-Mais")
    Menu1()
    Menu2()
    Menu3()
    #ad = sum(adnal)
    #print(f'adcional {ad}')
    #print(f'metragem {metrage}')
    #print(f'tipo {tipo}')
    total = (metrage * tipo) + sum(adnal)
    print(f'Total: R$ {total} (Metragem: {metrage} * Tipo: {tipo} + Adicional: {sum(adnal)})')
#----------------------Fim função principal-----------------------------------


#----------------------Inicio função menu 1-----------------------------------
def Menu1():
    print('--------Menu 1 de 3 - Metragem de limpeza--------')
    print('!!Não aceitamos casas com metragem a baixo de 30m² e acima de 700m²!!')
    Metragem()
#----------------------Fim função meu 1-----------------------------------


#----------------------Inicio função menu 2-----------------------------------
def Menu2():
    print('--------Menu 2 de 3 - Tipo de limpeza--------')
    print('B - Básica - Indicada para limpezas semanais ou quinzenais\n'
          'C - Completa (30% a mais) - Indicada para sujeiras antigas')
    TipoLimpeza()
#----------------------Fim função menu 2-----------------------------------


#----------------------Inicio função menu 3-----------------------------------
def Menu3():
    print('--------Menu 3 de 3 - Adicional de limpeza--------')

    Adicional()
#----------------------Fim função menu 3-----------------------------------


#----------------------Inicio função idenficação aluno-----------------------------------
def iden():
    aluno = 'Wallace Silva'
    ru = '3236'
    print(f"------------Aluno: {aluno}, Ru: {ru}------------")
#----------------------Fim função identificação aluno-----------------------------------


#----------------------Inicio função de metragem-----------------------------------
def Metragem():
    global metrage, m

    while True:
        try:
            m = float(input("Informe a metragem total desejado: "))
            if m > metrimax or m < metrimim:
                print('!!!Metragem acima ou a baixo do permitido!!!')
            elif type(m) is float:
                if m < metrmed:
                    metrage = mvmini+mulmini*m
                    break
                elif m >= metrmed:
                    metrage = mvmax+multmax*m
                    break
        except ValueError:
            print('!!!Metragem não reconhecida.!!!')
#----------------------Fim função de metragem-----------------------------------


#----------------------Inicio função tipo de limpeza-----------------------------------
def TipoLimpeza():
    global tb_tipo, tipo
    while True:
        tl = input('Informe o tipo de limpeza: ').lower()
        if tl in tb_tipo:
            tipo = tb_tipo[tl]
            break
        else:
            print('!!!Tipo invalido!!!')
#----------------------Fim função tipo de limeza-----------------------------------


#----------------------Inicio função serviço adcional-----------------------------------
def Adicional():
    global tb_adcional, adnal
    while True:
        print('0 - Não desejo mais nada (encerrar)\n'
              '1 - Passar 10 peças de roupas - R$ 10,00\n'
              '2 - Limpeza de um Forno/Micro-ondas - R$ 12,00\n'
              '3 - Limpeza de uma Geladeira/Freezer - R$ 20,00')
        a = input('Deseja servições adicionais? ').lower()
        if a == '0':
            break
        if a in tb_adcional:
            adnal.append(tb_adcional[a])
        else:
            print('Adiciional não reconhecido, escola um adciona ou 0 para finalizar.')
#----------------------Fim função serviço adcional-----------------------------------


main() # Chamada de função principal
