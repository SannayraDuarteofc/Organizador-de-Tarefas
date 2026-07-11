#Realiza o Cadastro de Tarefas, Verifica se o usuário deseja estudar o fazer outra coisa, se o usuário preferir
# estudar, ele deverá escolher uma matéria já cadastrada ou cadastrar uma nova, o mesmo deve acontecer com demais
# atividades
def CadastroDeTarefas(ListaMaterias):
    Tarefa = {}

    Tipo = int(input('1. Estudos\n'
                      '2. Outros\n'
                      'Qual atividade deseja cadastrar hoje?'))
    while True:
        if int(Tipo) == 1:
            Tarefa["Tipo"] = 'Estudos'
            Escolha = input('1. Escolher Materia\n'
                                '2. Cadastrar Nova Matéria\n'
                                ':')
            while True:
                if int(Escolha) == 1:
                    for i,materia in enumerate(len(ListaMaterias), start= 1):
                        print(f'{i}. {ListaMaterias[materia]}\n')
                    IndiceMateria = int(input('Matéria: '))

                elif int(Escolha) == 2:
                    ListaMaterias.append(CadastroDeMaterias())
                    continue
                else:
                    Escolha = input('Digite uma opção válida: ')
                    continue
                break
            Tarefa["Materia"] = ListaMaterias[IndiceMateria - 1]

        elif Tipo == 2:
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
            if ListaTarefas[j]["Prioridade"] > ListaMaterias[j+1]["Prioridade"]:
                ListaTarefas[j], ListaTarefas[j+1] = ListaTarefas[j+1], ListaTarefas[j]

#Imprime as tarefas do dia já ordenadas
def VisualisarListaTarefas(ListaTarefas, ListaMaterias):
    NiveisPrioridades = {
        1: "Alta",
        2: "Média",
        3: "Baixa",
    }

    if not ListaTarefas:
        print('Não há tarefas para hoje')
        return

    for i, Tarefa in enumerate(ListaTarefas, start=1):
        if Tarefa["Tipo"] == 'Outros':
            print(f'{i}. {Tarefa["Tipo"]} | Afazer: {Tarefa["Afazer"]} | Prioridade:'
                  f' {NiveisPrioridades[Tarefa["Prioridade"]]}  | '
                  f'Tempo: {Tarefa["Tempo"]//60:02d}:{Tarefa["Tempo"]%60:02d}')
        elif Tarefa["Tipo"] == 'Estudos':
            print(f'{i}. {Tarefa["Tipo"]} | Matéria: {Tarefa["Estudos"]} | Prioridade:'
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

    elif Menu == 2:
        VisuaListaTarefas(ListaTarefas)
    elif Menu == 3:

    elif Menu == 4:

    elif Menu == 5:

    elif Menu == 6:
        break
    else:
        print('Opção invalida! Tente novamente\n')
