#Funções 
 
def cadastrar_funcionario(id): #Cadastrar funcionários 
    print('-' * 20 + ' MENU CADASTRAR FUNCIONÁRIO ' + 20 * '-')  # Realce 
    print(f'Id do funcionário: {id}') 
    funcionario['id'] = id 
    funcionario['nome'] = input('Por favor, entre com o nome do funcionário: ') 
    funcionario['setor'] = input('Por favor, entre com o setor do funcionário: ') 
    funcionario['salário'] = float(input('Por favor, entre com o salário do funcionário: ')) 
    lista_funcionarios.append(funcionario.copy()) #Copiar o dicionário para a lista 
    print('Funcionário cadastrado com sucesso!') 
 
def consultar_funcionarios(): #Consultar funcionários 
    while True: 
        print('-' * 20 + ' MENU CONSULTAR FUNCIONÁRIO ' + 20 * '-')  # Realce 
        print('1. Consultar Todos') 
        print('2. Consultar por Id') 
        print('3. Consultar por Setor') 
        print('4. Retornar ao menu') 
        op = int(input('Escolha a opção desejada: ')) 
 
        if op == 1: #Consultar Todos 
            for funcionarios in lista_funcionarios: 
                print('') #Espaço 
                for chave, valor in funcionarios.items(): #Acessar o par chave e valor 
                    print(f'{chave}: {valor}') 
 
        elif op == 2: #Consultar funcionários por Id 
            id_consulta = int(input('Digite o Id do funcionário: ')) 
            for funcionarios in lista_funcionarios: 
                print('') 
                if funcionarios['id'] == id_consulta: 
                    for chave, valor in funcionarios.items():  # Acessar o par chave e valor 
                        print(f'{chave}: {valor}') 
 
        elif op == 3: #Consultar funcionários por setor 
            setor_consulta = input('Digite o setor do(s) funcionário(s): ') 
            for funcionarios in lista_funcionarios: 
                print('') 
                if funcionarios['setor'] == setor_consulta: 
                    for chave, valor in funcionarios.items(): 
                        print(f'{chave}: {valor}') 
 
        elif op == 4: 
            return #Voltar para o Menu Principal 
 
        else: 
            print('Opção inválida!') 
 
def remover_funcionario(): #Remover funcionário 
    while True: 
        id_remover = int(input('Digite o Id do funcionário a ser removido: ')) 
        for funcionarios in lista_funcionarios: 
            if funcionarios['id'] == id_remover: 
                lista_funcionarios.remove(funcionarios) #Excluir o dicionário da lista! 
                print('Funcionário removido com sucesso!') 
                return #Voltar para o Menu Principal 
 
        else: #Se o laço de repetição não encontrar o Id 
            print('Id inválido!') 
 
#Programa principal 
 
funcionario ={} #Dicionário vazio 
lista_funcionarios = [] #Lista vazia 
id_global = 5245139 #RU 
 
while True: #Início do laço de repetição 
 
    print(' Bem vindo a empresa do Jason L. Frazão de Almeida!') 
    print('-' * 28 + 28 * '-') 
    print('-' * 20 + ' MENU PRINCIPAL ' + 20 * '-')  # Realce 
    print('Escolha a opção desejada: ') 
    print('\n1 - Cadastrar Funcionários \n2 - Consultar Funcionário(s) \n3 - Remover Funcionário \n4 - Sair') 
    opcao = int(input('Digite a opção desejada: ')) 
 
    if opcao == 1: #Cadastrar funcionário 
        id_global += 1 #Incrementar em um id_global 
        cadastrar_funcionario(id_global) 
 
    elif opcao == 2: #Consultar Funcionário(s) 
        consultar_funcionarios() 
 
    elif opcao == 3:  #Remover funcionário 
        remover_funcionario() 
 
    elif opcao == 4: #Encerrar o programa 
        break 
    else: 
        print('Opção inválida!') 
