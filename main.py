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
            if int(Tipo) == 1:
                Tarefa["Tipo"] = 'Estudos'
                Escolha = input('1. Escolher Materia\n'
                                    '2. Cadastrar Nova Matéria\n'
                                    ':')
                while True:
                    if int(Escolha) == 1:
                        if not ListaMaterias:
                            print('Não há matérias cadastradas')
                            Op = input('Deseja cadastrar uma nova matéria?'
                                       '1. Sim'
                                       '2. Não'
                                       ':')
                            while True:
                                if Op == 1:

                        for i, Materia in enumerate(ListaMaterias, start= 1):
                            print(f'{i}. {Materia}\n')
                        IndiceMateria = int(input('Matéria: '))
                        if IndiceMateria >= 1 and IndiceMateria <= len(ListaMaterias):
                            Tarefa["Materia"] = ListaMaterias[IndiceMateria - 1]
                        else:
                            Escolha = input('Digite uma opção válida: ')
                            continue

                    elif int(Escolha) == 2:
                        NovaMateria = CadastroDeMaterias()
                        ListaMaterias.append(NovaMateria)
                        Tarefa["Materia"] = NovaMateria
                    else:
                        Escolha = input('Digite uma opção válida: ')
                        continue
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
            Tipo = input('Digite uma opção válida: ')
            continue
        break

    Prioridade = input('1. Alta\n'
                       '2. Média\n'
                       '3. Baixa\n'
                       'Escolha o nível de prioridade: ')
    while True:
        if Prioridade.isnumeric():
            if int(Prioridade) in (1, 2, 3):
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

    for Materia in ListaTarefas:
        Total += Materia["Tempo"]

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
def VisualizarListaTarefas(ListaTarefas):
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
    Menu = int(input('1. Cadastrar Tarefas do dia\n'
                     '2. Visualizar Matérias\n'
                     '3. Visualizar Afazeres de hoje\n'
                     '4. Remover Tarefa\n'
                     '5. Remover Matéria\n'
                     '6. Encerrar\n'
                     'O que deseja fazer: '))

    if Menu == 1:
        ListaTarefas.append(CadastroDeTarefas(ListaMaterias))
    elif Menu == 2:
        VisualizarMaterias(ListaMaterias)
    elif Menu == 3:
        VisualizarListaTarefas(ListaTarefas)
    elif Menu == 4:
        RemoverTarefa(ListaTarefas)
    elif Menu == 5:
        RemoverMateria(ListaMaterias)
    elif Menu == 6:
        break
    else:
        print('Opção invalida! Tente novamente\n')
