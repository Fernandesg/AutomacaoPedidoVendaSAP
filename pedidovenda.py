import PySimpleGUI as sg

itens = []
i=0
def novo_item(i):
    return [[sg.Text('Nº item:'), sg.Input(key=('-CODITEM-', i), size=(9,1), enable_events=True), sg.Text('Quant:'), sg.Input(key=('-QUANTITEM-', i), size=(5,1), enable_events=True), sg.Button('-', key='-REM-', size=(2,1))]]

layout_item = [
    [sg.Text('Nº item:'), sg.Input(key=('-CODITEM-', 0), size=(9,1), enable_events=True), sg.Text('Quant:'), sg.Input(key=('-QUANTITEM-', 0), size=(5,1), enable_events=True), sg.Button('+', key='-ADD-', size=(2,1))]
    ]

layout = [
    [sg.Text('Remetente'),sg.Text('           '), sg.Text('Destinatário')],
    [sg.Combo(['SAP','Osorio','Capão da canoa','Tramandai'], key='-REMETENTE-', enable_events=True), sg.Combo(['SAP','Osorio','Capão da canoa','Tramandai'],key='-DESTINO-', enable_events=True), sg.Push()],
    [sg.Text('Tipo de frete', enable_events=True)],
    [sg.Combo(['Próprio por conta do Remetente','Próprio por conta do Destinatário'], enable_events=True, key='-TIPOFRETE-')],
    [sg.Column(layout_item, key='-ADDCOLUNA-')],
    [sg.Button('Criar pedido')]
    ]

window = sg.Window('Criar pedido de venda', layout=layout)


while True:
    event, values = window.read()
    listaInfos = []
    if event == None:
        break
    match(event):
        case sg.WIN_CLOSED:
            break
        case '-ADD-':
            if i<20:
                window.extend_layout(window['-ADDCOLUNA-'], novo_item(i))
                i += 1
        case 'Criar pedido':
            for valor in values:
                listaInfos.append(values[valor])
            listaItens = listaInfos[3::2]
            listaQuant = listaInfos[4::2]
            remetente = listaInfos[0]
            destino = listaInfos[1]
            tipoFrete = listaInfos[2]
            print(listaItens)
            print(listaQuant)
            print(remetente)
            print(destino)
            print(tipoFrete)
