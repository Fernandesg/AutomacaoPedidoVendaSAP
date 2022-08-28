import PySimpleGUI as sg
import pyautogui
import pygetwindow
import time

btCalendario = b'iVBORw0KGgoAAAANSUhEUgAAABQAAAAUCAYAAACNiR0NAAAACXBIWXMAAA3XAAAN1wFCKJt4AAAAIGNIUk0AAHolAACAgwAA+f8AAIDpAAB1MAAA6mAAADqYAAAXb5JfxUYAAAGuSURBVHjarNS/b85RFMfx11N9tKiGikTSwSKxSAWxdDb4AyQmg/9BiJh0sFjE1jC0xKSLwSCpkjCQdFASosEgpEFoY6BazTH0PM1Jk8ojnpPcnPf9fu8993zO/SEilDYVEd/Wfftbm4uI6fqt26odw2EMowfntGd7sp3FDO6JiPPRORtpRERgFifxCH042GaGM+kPYRxDLcl38AxnsA/P2wx4CV9z7gSGGhHxGw9xEXNYwt42A77HJgxm3Y83ImIeO3TGFhoRsZS1GM30e7EtuYl+zCMwgO9Yxi78wM/k0zjanZOmcf0/s9uP4a7sLKcP3Cj8KvlX9uXiLb5aeBFrB3tr+lFMFZ5NvpylgLEMCpPYnNy3msaq3f6H67ZRG4+IaEn+VGReKfwg+S0+J98tMkcKf6ySW/4x3hV+UerWKsvL3Hn4gKfJzSp5ogOSx6rkL+lncaHwzeT7eJJ8rWxWtZUqdbE8R9sLDyTvXttFdua/9bZUAw6m7y8DKg8VPrHBwe6BRkTM5Yq3sJCLNPNKdeXAloLezGQFW0qwJk5hXkQciIjXHXhc30TEkT8DAFILwAACEvTGAAAAAElFTkSuQmCC'

janelaSAP = 'SAP Business One 9.3 (g2srv11.G2TECNOLOGIA.COM.BR)'
sap = pygetwindow.getWindowsWithTitle(janelaSAP)[0]

itens = []
i=0

def novo_item(i):
    return [[sg.Text('Nº item:'), sg.Input(key=('-CODITEM-', i), size=(9,1), enable_events=True), sg.Text('Quant:'), sg.Input(key=('-QUANTITEM-', i), size=(5,1), enable_events=True), sg.Button('-', key='-REM-', size=(2,1))]]

layout_item = [
    [sg.Text('Nº item:'), sg.Input(key=('-CODITEM-', 0), size=(9,1), enable_events=True), sg.Text('Quant:'), sg.Input(key=('-QUANTITEM-', 0), size=(5,1), enable_events=True), sg.Button('+', key='-ADD-', size=(2,1))]
    ]

layout = [
    [sg.Text('Remetente'),sg.Text('           '), sg.Text('Destinatário')],
    [sg.Combo(['SAP','Osorio','Capão da canoa','Tramandai','Arroio do Sal', 'Viamão'], key='-REMETENTE-', enable_events=True, default_value='SAP'), sg.Combo(['SAP','Osorio','Capão da canoa','Tramandai','Arroio do Sal', 'Viamão'],key='-DESTINO-', enable_events=True), sg.Push()],
    [sg.Text('Data de entrega')],
    [sg.Input(key='data_entrega', size=(19, 1), enable_events=True),sg.CalendarButton('',close_when_date_chosen=True,  target='data_entrega', no_titlebar=False, format='%d/%m/%Y', image_data=btCalendario)],
    [sg.Text('Tipo de frete', enable_events=True)],
    [sg.Combo(['Próprio por conta do Remetente','Próprio por conta do Destinatário'], enable_events=True, key='-TIPOFRETE-')],
    [sg.Column(layout_item, key='-ADDCOLUNA-')],
    [sg.Push(), sg.Button('Criar pedido'), sg.Push()],
    [sg.Push(), sg.Text('Insira o pedido de venda no atalho F12'), sg.Push()]
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
            listaFiltrada = filter(None, listaInfos)
            listaInfoFiltro = list(listaFiltrada)
            listaItens = listaInfoFiltro[4::2]
            listaQuant = listaInfoFiltro[5::2]
            remetente = listaInfoFiltro[0]
            destino = listaInfoFiltro[1]
            tipoFrete = listaInfoFiltro[3]
            dataEntrega = listaInfoFiltro[2]
            print(listaInfoFiltro)
            print(listaItens)
            print(listaQuant)
            print(remetente)
            print(destino)
            print(tipoFrete)
            print('-='*40)
            sap.activate()
            sap.maximize()
            time.sleep(1)
            #Abre pedido de venda
            pyautogui.press('f12')
            time.sleep(1)

            #Insere código cliente
            localcliente = pyautogui.locateCenterOnScreen('cliente.png', confidence=0.8)
            pyautogui.click(localcliente)
            if destino == 'Tramandai':
                pyautogui.write('C619704')
            elif destino == 'Osorio':
                pyautogui.write('C620463')
            elif destino == 'SAP':
                pyautogui.write('C252048')
            elif destino == 'Capão da canoa':
                pyautogui.write('C620466')
            elif destino == 'Arroio do Sal':
                pyautogui.write('C620464')
            elif destino == 'Viamão':
                pyautogui.write('C619548')
            time.sleep(1.5)
            pyautogui.press('tab')
            pyautogui.press('tab')
            time.sleep(2)

            #Seleciona filial
            localFilial = pyautogui.locateCenterOnScreen('filial.png', confidence=0.8)
            pyautogui.click(localFilial.x+100,localFilial.y)
            time.sleep(1)
            localFilialII = pyautogui.locateCenterOnScreen('filialSAPII.png')
            pyautogui.click(localFilialII)

            #Insere itens
            localItem = pyautogui.locateCenterOnScreen('insereItem.png', confidence=0.8)
            pyautogui.click(localItem.x,localItem.y+8)
            for item in listaItens:
                pyautogui.write(item)
                pyautogui.press('tab')
                pyautogui.press('down')

            #Insere quantidades
            localQuant = pyautogui.locateCenterOnScreen('Quant.png', confidence=0.8)
            pyautogui.click(localQuant)
            for quant in listaQuant:
                pyautogui.write(quant)
                pyautogui.press('down')
            
            #Insere filial
            localConfigColuna = pyautogui.locateCenterOnScreen('ConfigColuna.png')
            pyautogui.click(localConfigColuna)
            time.sleep(1)
            localDeposito = pyautogui.locateCenterOnScreen('deposito.png', confidence=0.8)
            pyautogui.click(localDeposito.x+110,localDeposito.y)
            pyautogui.write('56WH')
            pyautogui.press('tab')
            pyautogui.press('enter')
            pyautogui.press('enter')
            time.sleep(2)

            localObs = pyautogui.locateCenterOnScreen('obs.png', confidence=0.8)
            pyautogui.click(localObs.x,localObs.y+50)
            pyautogui.write(f'Solicitação de transferência de {remetente} para {destino}')

            #Insere uso principal
            localusoPrincipal = pyautogui.locateCenterOnScreen('usoPrincipal.png', confidence=0.8)
            pyautogui.click(localusoPrincipal)
            time.sleep(2)
            pyautogui.press('pagedown', presses=3)
            time.sleep(1)
            localUtilizacao = pyautogui.locateCenterOnScreen('utilizacao.png', confidence=0.8)
            pyautogui.click(localUtilizacao)

            localDatas = pyautogui.locateCenterOnScreen('datas.png', confidence=0.8)
            pyautogui.click(localDatas.x+100,localDatas.y)
            pyautogui.write(dataEntrega)
            pyautogui.press('tab')
            pyautogui.press('enter')
            time.sleep(1)
            localImposto = pyautogui.locateCenterOnScreen('imposto.png', confidence=0.8)
            pyautogui.click(localImposto)
            time.sleep(0.5)
            localIncoterms = pyautogui.locateCenterOnScreen('incoterms.png', confidence=0.8)
            pyautogui.click(localIncoterms.x+100,localIncoterms.y)
            if tipoFrete == 'Próprio por conta do Remetente':
                pyautogui.write('3')
            else:
                pyautogui.write('4')
            pyautogui.press('tab')
