def CadastroDeMaterias():
    Materias = {}

    Materias["Materia"] = input('Matéria: ')
    Materias["Prioridade"] = input('Nível de Prioridade (Alta, Média ou Baixa): ').lower()
    Materias["Tempo"] = int(input('Tempo (em minutos): '))

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
        if Materia["Prioridade"] == 'alta':
            print(f'{cont}. {Materia["Materia"]} | Prioridade: {Materia["Prioridade"]} | Tempo: {Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')
            cont += 1

    for Materia in ListaMaterias:
        if Materia["Prioridade"] in ('media', 'média'):
            print(f'{cont}. {Materia["Materia"]} | Prioridade: {Materia["Prioridade"]} | Tempo: {Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')
            cont += 1

    for Materia in ListaMaterias:
        if Materia["Prioridade"] == 'baixa':
            print(f'{cont}. {Materia["Materia"]} | Prioridade: {Materia["Prioridade"]} | Tempo: {Materia["Tempo"]//60:02d}:{Materia["Tempo"]%60:02d}')
            cont += 1

    print(f'Tempo Total: {TempoTotal(ListaMaterias)}\n')


ListaMaterias = []

print('1. Cadastrar Matéria\n'
      '2. Visualizar Matérias de Hoje\n'
      '3. Encerrar')

while True:
    Menu = int(input('O que deseja fazer: '))

    if Menu == 1:
        Materia = CadastroDeMaterias()
        ListaMaterias.append(Materia)
    elif Menu == 2:
        VisualizarMaterias(ListaMaterias)
    elif Menu == 3:
        break
    else:
        print('Opção invalida! Tente novamente\n')

    print('1. Cadastrar Matéria\n'
          '2. Visualizar Matérias de Hoje\n'
          '3. Encerrar')
