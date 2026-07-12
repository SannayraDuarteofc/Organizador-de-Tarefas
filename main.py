#Realiza o Cadastro de Tarefas, Verifica se o usuário deseja estudar o fazer outra coisa, se o usuário preferir
# estudar, ele deverá escolher uma matéria já cadastrada ou cadastrar uma nova, o mesmo deve acontecer com demais
# atividades
def CadastroDeTarefas(ListaMaterias):
    Tarefa = {}

    Tipo = input('1. Estudos\n'
                '2. Outros\n'
                'Qual atividade deseja cadastrar hoje?')
    while True:
        if Tipo.isnumeric() and int(Tipo) in (1, 2):
            Tipo = int(Tipo)
            if Tipo == 1:
                Tarefa["Tipo"] = 'Estudos'
                Escolha = input('1. Escolher Materia\n'
                                    '2. Cadastrar Nova Matéria\n'
                                    ':')
                while True:
                    if Escolha.isnumeric() and int(Escolha) in (1, 2):
                        Escolha = int(Escolha)
                        if Escolha == 1:
                            if not ListaMaterias:
                                print('Não há matérias cadastradas')
                                Op = input('Deseja cadastrar uma nova matéria?\n'
                                           '1. Sim\n'
                                           '2. Não\n'
                                           ':')
                                while True:
                                    if Op.isnumeric() and int(Op) in (1, 2):
                                        Op = int(Op)
                                        if Op == 1:
                                            Escolha = '2'
                                            break
                                        elif Op == 2:
                                            return
                                    else:
                                        Op = input("Digite uma opção válida: ")

                                continue

                            for i, Materia in enumerate(ListaMaterias, start= 1):
                                print(f'{i}. {Materia}\n')
                            IndiceMateria = input('Matéria: ')
                            while True:
                                if IndiceMateria.isnumeric():
                                    IndiceMateria = int(IndiceMateria)
                                    if IndiceMateria >= 1 and IndiceMateria <= len(ListaMaterias):
                                        Tarefa["Materia"] = ListaMaterias[IndiceMateria - 1]
                                        break
                                    else:
                                        IndiceMateria = input('Digite uma opção válida: ')
                                else:
                                    IndiceMateria = input('Digite uma opção válida: ')

                        else:
                            NovaMateria = CadastroDeMaterias()
                            ListaMaterias.append(NovaMateria)
                            Tarefa["Materia"] = NovaMateria
                        break

            else:
                Tarefa["Tipo"] = 'Outros'
                NovaTarefa = input('Tarefa:').strip()
                while True:
                    if NovaTarefa:
                        Tarefa["Afazer"] = NovaTarefa
                        break
                    NovaTarefa = input('Digite uma tarefa válida: ').strip()
        else:
            Tipo = input('Digite uma opção válida: ').strip()
            continue
        break

    Prioridade = input('1. Alta\n'
                       '2. Média\n'
                       '3. Baixa\n'
                       'Escolha o nível de prioridade: ')
    while True:
        if Prioridade.isnumeric():
            if int(Prioridade) in range(1, 4):
                Tarefa['Prioridade'] = int(Prioridade)
                break

        Prioridade = input('Digite um tipo de prioridade válida: ')

    Tempo = input('Tempo: ')
    while True:
        if Tempo.isnumeric():
            Tempo = int(Tempo)
            if Tempo > 0:
                Tarefa["Tempo"] = Tempo
                break

        Tempo = input('Digite uma quantidade de tempo válida: ')

    return Tarefa

#Realiza o cadastro das matérias
def CadastroDeMaterias():
    Materia = input('Matéria: ').strip()

    while True:
        if Materia:
            break

        Materia = input('Digite uma matéria válida: ').strip()

    return Materia

#Calcula o tempo total gasto nas tarefas e retorna o valor em horas e minutos no formato: HH:MM
def TempoTotal(ListaTarefas):
    Total = 0

    for Tarefa in ListaTarefas:
        Total += Tarefa["Tempo"]

    TotalHoras = Total // 60
    TotalMin = Total % 60

    return f'{TotalHoras:02d}:{TotalMin:02d}'

#Organiza as tarefas em ordem de prioridade com o tipo de ordenação Bublle Sort
def OrganizarTarefas(ListaTarefas):

    if not ListaTarefas:
        return

    for _ in range(len(ListaTarefas) - 1):
        for j in range(len(ListaTarefas) - 1):
            if ListaTarefas[j]["Prioridade"] > ListaTarefas[j+1]["Prioridade"]:
                ListaTarefas[j], ListaTarefas[j+1] = ListaTarefas[j+1], ListaTarefas[j]

#Mostra todas as matérias cadastradas, caso haja alguma
def VisualizarMaterias(ListaMaterias):
    if not ListaMaterias:
        print('Não há matérias cadastradas')
        return

    for i, Materia in enumerate(ListaMaterias, start=1):
        print(f'{i}. {Materia}')

#Imprime as tarefas do dia já ordenadas, caso haja
def VisualizarTarefas(ListaTarefas):
    NiveisPrioridades = {
        1: "Alta",
        2: "Média",
        3: "Baixa",
    }

    if not ListaTarefas:
        print('Não há tarefas para hoje')
        return

    OrganizarTarefas(ListaTarefas)

    for i, Tarefa in enumerate(ListaTarefas, start=1):
        if Tarefa["Tipo"] == 'Outros':
            print(f'{i}. Tipo: {Tarefa["Tipo"]} | Afazer: {Tarefa["Afazer"]} | Prioridade:'
                  f' {NiveisPrioridades[Tarefa["Prioridade"]]}  | '
                  f'Tempo: {Tarefa["Tempo"]//60:02d}:{Tarefa["Tempo"]%60:02d}')
        elif Tarefa["Tipo"] == 'Estudos':
            print(f'{i}. Tipo: {Tarefa["Tipo"]} | Matéria: {Tarefa["Materia"]} | Prioridade:'
                  f' {NiveisPrioridades[Tarefa["Prioridade"]]}  | '
                  f'Tempo: {Tarefa["Tempo"] // 60:02d}:{Tarefa["Tempo"] % 60:02d}')

    print(f'Tempo Total: {TempoTotal(ListaTarefas)}\n')


ListaTarefas = []
ListaMaterias = []

while True:
    Menu = input('1. Cadastrar Tarefas do dia\n'
                 '2. Visualizar Matérias\n'
                 '3. Visualizar Afazeres de hoje\n'
                 '4. Remover Tarefa\n'
                 '5. Remover Matéria\n'
                 '6. Encerrar\n'
                 'O que deseja fazer: ')
    if Menu.isnumeric() and int(Menu) in range(1, 7):
        Menu = int(Menu)
        if Menu == 1:
            Tarefa = CadastroDeTarefas(ListaMaterias)
            if Tarefa is not None:
                ListaTarefas.append(Tarefa)
        elif Menu == 2:
            VisualizarMaterias(ListaMaterias)
        elif Menu == 3:
            VisualizarTarefas(ListaTarefas)
        elif Menu == 4:
            RemoverTarefa(ListaTarefas)
        elif Menu == 5:
            RemoverMateria(ListaMaterias)
        elif Menu == 6:
            break
    else:
        print('Opção invalida! Tente novamente:')
