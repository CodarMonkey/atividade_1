aluno = 'Aluno:Wallace Silva'
ru = 'Ru:3236'
print((len(aluno)*'*')+(len(ru)*'*')+(3*'*'))
print(f"{aluno}, {ru}")
print((len(aluno)*'*')+(len(ru)*'*')+(3*'*'))
lfincionarios = []
rgid = 0

#--------------Inicio função de cadastro de Funcionario--------------
def cadastrarFunc(Id):
    print("-------------Cadastrar Funcionario-------------")
    try:
        nome = input('Nome: ')
        setor = input('Setor: ')
        salario = float(input('salario: '))
        funcionarios = {'id': Id,'nome': nome, 'setor': setor, 'salario': salario}
        lfincionarios.append(funcionarios.copy())
    except ValueError:
        print('Valor não reconhecido')
    #print(lfincionarios)
    for rgid in lfincionarios:
        if rgid == rgid:
            print(f'Funcionario: {nome}, Setor: {setor}, Salario: {salario},\n'
                  f'>>Cadastrado com sucesso')
            print()
            break
        else:
            print('Funcionario não cadastrado')
            print()
#---------------Fim função de cadastro de Funcionario----------------


#---------------Inicio função de Menu consulta------------------------
def consultar():
    while True:
        print("-------------MENU DE CONSULTA-------------")
        print('1 - Consultar todos\n'
              '2 - Consultar por Id\n'
              '3 - Consultar por setor\n'
              '4 - Retornar\n')
        opc2 = input('Digite o número da opção: ')

        if opc2 == '1':
            consultarTodos()
            print()
            continue
        elif opc2 == '2':
            print("-------------CONSULTAR POR ID-------------")
            consultarId()
            print()
            continue
        elif opc2 == '3':
            consultarSetor()
            print()
            continue
        elif opc2 == '4':
            return
        else:
            print('>>>Opção invalida<<<')
#----------------Fim função de Menu de consulta------------------------


#-----------------Inicio função de consulta por id---------------------
def consultarId():
    #print("-------------CONSULTAR POR ID-------------")
    while True:
        rid = input('Informe o ID: ')
        if not rid.isnumeric():
            print('!!!!Opção invalida!!')
        else:
            rid = int(rid)
            for ri in lfincionarios:
                if ri['id'] == rid:
                    for key, value in ri.items():
                        print(f'{key}: ', end='' f'{value}, ')
                    print()
                    break

            else:
                print('Id não encotrado!')
                consultarId()

        break

#-----------------Fim função de consulta por id-------------------------


##----------------Inicio função de consulta por setor-------------------
def consultarSetor():
    print("-------------CONSULTA POR SETOR-------------")
    vazio()
    try:
        s = input('Informe o setor: ')
        for se in lfincionarios:
            if se['setor'] == s:
                for key, value in se.items():
                    print(f'{key}: ', end='' f'{value}, ')
                print()
    except ValueError:
        print(">>Id não cadastrado")
#-----------------Fim função de consuta por setor------------------------


#-----------------Inicio função verificação de lista vazia---------------
def vazio():
    if lfincionarios == []:
        print('Nem um funcionario cadastrado')
        return
#-----------------Fim função verificação de lista vazia------------------


#-----------------Inicio função consultar todos os cadastros-------------
def consultarTodos():
    print("-------------CONSULTAR TODOS-------------")
    vazio()
    for f in lfincionarios:
        for key, value in f.items():
            print(f'{key}: ', end='' f'{value}, ')
        print()
#-----------------Fim função consultar todos os cadastros-----------------


#----------------------Inicio função remove cadastro----------------------
def removerFunc():
    print("-------------REMOVER FUNCIONARIO-------------")
    try:
        s = int(input('Informe o ID: '))
        vazio()
        for se in lfincionarios:
            if se['id'] == s:
                lfincionarios.remove(se)
                print('>>removido com sucesso.')
                break
        else:
            print(">>Funcionario inesistente.")
    except ValueError:
        print(">>Id Invalido!")

#-------------------Fim função consultar remove cadastro------------------


#-------------------inicio da Função principal----------------------------
def main():
    global rgid # #global variavel
    print()
    print('>>>>>>>Bem vindo a Consulta e Cadastro de Funcionario.<<<<<<<')
    print()
    while True:
        ic = input('Deseja iniciar? (S para sim N para encerrar): ').lower()# iniciar ou finalizar sistema
        if ic == 'n': # verifica resposta do usuario e finaliza o sistema
            print('Sistema finalizado.')
            break
        elif ic == 's': # verifica resposta do usuario e inicia menu principal
            while True:
#--------------------inicio do menu preincipal----------------------------
                print("-------------MENU PRINCIPAL-------------")
                print('1 - Cadastrar Funcionario\n'
                      '2 - Consultar Funcionario\n'
                      '3 - Remover funcionario\n'
                      '0 - Sair')
                opc = input('Escolha uma opção: ')

                '''if opc != '1' or '2' or '3':
                    print('!!!Opção invalida!')
                    continue'''
                if opc == '1': #
                    rgid += 1 # variavel geradora de id
                    cadastrarFunc(rgid) #chamada de função de cadastrar na lista
                elif opc == '2':
                    consultar() #chamada de menu de consuta
                elif opc == '3':
                    removerFunc() #chamada de função para remover da lista
                elif opc == '0':
                    quit()
                else:
                    print('!!!Opção invalida!')
        elif ic != 's' or 'n':
            print('!!!Opção invalida!')
#--------------------Fim da Função principal-------------------------------


if __name__ == '__main__':
    main()
