def CadastroDeMaterias():
    Materias = {}

    Materia = input('Matéria: ').strip()
    while True:
        if Materia:
            Materias["Materia"] = Materia
            break
        else:
            Materia = input('Digite uma matéria válida: ').strip()

    Prioridade = input('1. Alta'
                       '\n2. Média\n'
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
    cont = 1

    if not ListaMaterias:
        print('Não há matérias para estudar hoje')
        return

    for Materia in ListaMaterias:
        if Materia["Prioridade"] == 1:
            print(f'{cont}. {Materia["Materia"]} | Prioridade: Alta | Tempo: '
                  f'{Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')
            cont += 1

    for Materia in ListaMaterias:
        if Materia["Prioridade"] == 2:
            print(f'{cont}. {Materia["Materia"]} | Prioridade: Média | Tempo: {Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')
            cont += 1

    for Materia in ListaMaterias:
        if Materia["Prioridade"] == 3:
            print(f'{cont}. {Materia["Materia"]} | Prioridade: Baixa | Tempo: {Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')
            cont += 1

    print(f'Tempo Total: {TempoTotal(ListaMaterias)}\n')


ListaMaterias = []

while True:
    Menu = int(input('1. Cadastrar Matéria\n'
                     '2. Visualizar Matérias de Hoje\n'
                     '3. Encerrar\n'
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
