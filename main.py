#Realiza o Cadastro de Tarefas, Verifica se o usuário deseja estudar o fazer outra coisa, se o usuário preferir
# estudar, ele deverá escolher uma matéria já cadastrada ou cadastrar uma nova, o mesmo deve acontecer com demais
# atividades
def CadastroDeTarefas():
    Tipo = int(input('1. Estudos'
                      '2. Outros'
                      'Qual atividade deseja cadastrar hoje?'))
    if Tipo == 1:
        

#Realiza o cadastro das matérias
def CadastroDeMaterias():
    Materia = {}

    Materiainput = input('Matéria: ').strip()
    while True:
        if Materia:
            Materia["Materia"] = Materiainput
            break
        else:
            Materiainput = input('Digite uma matéria válida: ').strip()

    Prioridade = input('1. Alta\n'
                       '2. Média\n'
                       '3. Baixa\n'
                       'Escolha o nível de prioridade: ')
    while True:
        if Prioridade.isnumeric():
            if int(Prioridade) in (1, 2, 3):
                Materia['Prioridade'] = int(Prioridade)
                break

        Prioridade = input('Digite um tipo de prioridade válida: ')

    Tempo = input('Tempo: ')
    while True:
        if Tempo.isnumeric():
            Tempo = int(Tempo)
            if Tempo > 0:
                Materia["Tempo"] = Tempo
                break

        Tempo = input('Digite uma quantidade de tempo válida: ')

    return Materia

def TempoTotal(ListaMaterias):
    Total = 0

    for Materia in ListaMaterias:
        Total += Materia["Tempo"]

    TotalHoras = Total // 60
    TotalMin = Total % 60

    return f'{TotalHoras:02d}:{TotalMin:02d}'

def OrganizarMaterias(ListaMaterias):

    if not ListaMaterias:
        return

    for _ in range(len(ListaMaterias) - 1):
        for j in range(len(ListaMaterias) - 1):
            if ListaMaterias[j]["Prioridade"] > ListaMaterias[j+1]["Prioridade"]:
                ListaMaterias[j], ListaMaterias[j+1] = ListaMaterias[j+1], ListaMaterias[j]

def VisualizarMaterias(ListaMaterias):
    NiveisPrioridades = {
        1: "Alta",
        2: "Média",
        3: "Baixa",
    }
    OrganizarMaterias(ListaMaterias)

    if not ListaMaterias:
        print('Não há matérias para estudar hoje')
        return

    for i, Materia in enumerate(ListaMaterias, start=1):
            print(f'{i}. {Materia["Materia"]} | Prioridade: {NiveisPrioridades[Materia["Prioridade"]]}  | Tempo: '
                  f'{Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')

    print(f'Tempo Total: {TempoTotal(ListaMaterias)}\n')


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
        VisualizarMaterias(ListaMaterias)
    elif Menu == 3:

    elif Menu == 4:

    elif Menu == 5:

    elif Menu == 6:
        break
    else:
        print('Opção invalida! Tente novamente\n')
