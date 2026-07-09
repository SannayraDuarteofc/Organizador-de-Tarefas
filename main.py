def CadastroDeMaterias():
    Materias = {}

    Materia = input('Matéria: ').strip()
    while True:
        if Materia:
            Materias["Materia"] = Materia
            break
        else:
            Materia = input('Digite uma matéria válida: ').strip()

    Prioridade = input('1. Alta\n'
                       '2. Média\n'
                       '3. Baixa\n'
                       'Escolha o nível de prioridade: ')
    while True:
        if Prioridade.isnumeric():
            if int(Prioridade) in (1, 2, 3):
                Materias['Prioridade'] = int(Prioridade)
                break

        Prioridade = input('Digite um tipo de prioridade válida: ')

    Tempo = input('Tempo: ')
    while True:
        if Tempo.isnumeric():
            Tempo = int(Tempo)
            if Tempo > 0:
                Materias["Tempo"] = Tempo
                break

        Tempo = input('Digite uma quantidade de tempo válida: ')

    return Materias

def TempoTotal(ListaMaterias):
    Total = 0

    for Materia in ListaMaterias:
        Total += Materia["Tempo"]

    TotalHoras = Total // 60
    TotalMin = Total % 60

    return f'{TotalHoras:02d}:{TotalMin:02d}'

def VisualizarMaterias(ListaMaterias):
    NiveisPrioridades = {
        1: "Alta",
        2: "Média",
        3: "Baixa",
    }

    if not ListaMaterias:
        print('Não há matérias para estudar hoje')
        return
    for _ in range(len(ListaMaterias) - 1):
        for j in range(len(ListaMaterias) - 1):
            if ListaMaterias[j]["Prioridade"] > ListaMaterias[j+1]["Prioridade"]:
                ListaMaterias[j], ListaMaterias[j+1] = ListaMaterias[j+1], ListaMaterias[j]

    for i, Materia in enumerate(ListaMaterias, start=1):
            print(f'{i}. {Materia["Materia"]} | Prioridade: {NiveisPrioridades[Materia["Prioridade"]]}  | Tempo: '
                  f'{Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')

    print(f'Tempo Total: {TempoTotal(ListaMaterias)}\n')


ListaMaterias = []

while True:
    Menu = int(input('1. Cadastrar Tarefas do dia\n'
                     '2. Cadastrar Matéria\n'
                     '3. Visualizar Matérias de Hoje\n'
                     '4. Remover Matérias\n'
                     '5. Encerrar\n'
                     'O que deseja fazer: '))

    if Menu == 1:
        Materia = CadastroDeMaterias()
        ListaMaterias.append(Materia)
    elif Menu == 2:
        VisualizarMaterias(ListaMaterias)
    elif Menu == 3:
        break
    else:
        print('Opção invalida! Tente novamente\n')
