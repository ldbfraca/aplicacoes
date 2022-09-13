import PySimpleGUI as sg
import distribuicao

def recebeusalario(salario):
    investir = salario * 0.3
    usarcommanu = salario * 0.15
    usarcomlucas = salario * 0.2
    cartao = salario * 0.1
    reserva = salario * 0.25
    return (f'tem R$ {investir:.2f} pra investir, Inter\n'
          f'tem R$ {reserva:.2f} pra reserva, Mercado pago\n'
          f'tem R$ {usarcomlucas:.2f} pra gastar consigo, Banco do Brasil\n'
          f'tem R$ {usarcommanu:.2f} pra usar com namorada, Nubank\n'
          f'tem R$ {cartao:.2f} pra pagar cartão, Itaú')

def recebeuporfora(salario):
    investir = salario * 0.5
    usarcomlucas = salario * 0.2
    cartaocasaefuturo = salario * 0.3
    return (f'tem R$ {investir:.2f} pra investir, Inter\n'
            f'tem R$ {usarcomlucas:.2f} pra gastar consigo, Banco do Brasil\n'
            f'tem R$ {cartaocasaefuturo:.2f} cartões, Itaú\n')

def investimentos(salario):
    fundos = 0.7 * 0.7 * salario
    acoes = 0.7 * 0.25 * salario
    etf = 0.7 * 0.05 * salario
    moedas = 0.1 * 0.95 * salario
    cripto = 0.05 * 0.1 * salario
    caixa = 0.1 * salario
    exterior = 0.1 * salario
    return (f'tem R$ {fundos:.2f} para FIIs\n'
            f'tem R$ {acoes:.2f} para ações\n'
            f'tem R$ {etf:.2f} para ETFs\n'
            f'tem R$ {moedas:.2f} para dólar virtual e físico\n'
            f'tem R$ {cripto:.2f} para cripto moedas\n'
            f'tem R$ {caixa:.2f} para guardar em LCI, caixa\n'
            f'tem R$ {exterior:.2f} para Stocks\n'
    )


layout = [[sg.T("                   "), sg.Checkbox('Recebeu Salário?', default=False, key='salario')],
          [sg.T("                   "), sg.Checkbox('Recebeu Por Fora?', default=False, key='recebeu fora')],
          [sg.T("                   "), sg.Checkbox('Quer investir??', default=False, key='investimento')],
          [sg.T("Quanto recebeu?"), sg.InputText('', key='valor')],
          [sg.Button('Calcular'), sg.Cancel()],
          [sg.Text('', key='valor recebido')],
          ]
janela = sg.Window('LOTAR DINHEIRINHO sem ter reserva', layout, size=(400, 300))
while True:
    eventos, valores = janela.read()
    if eventos == sg.WIN_CLOSED or eventos == 'Cancel':
        break

    if eventos == 'Calcular':
        reais = int(valores['valor'])


        if valores['salario'] == True and valores['recebeu fora'] == True and valores['investimento'] == True \
                or valores['salario'] == True and valores['recebeu fora'] == True \
                or valores['salario'] == True and valores['investimento'] == True \
                or valores['recebeu fora'] == True and valores['investimento'] == True:
            janela['valor recebido'].update('APERTOU DOIS OU MAIS')


        elif valores['salario'] == True and valores['recebeu fora'] == False and valores['investimento'] == False:#só salario é verdadeiro
            janela['valor recebido'].update(distribuicao.recebeusalario(reais))


        elif valores['recebeu fora'] == True and valores['salario'] == False and valores['investimento'] == False: #só recebeu fora verdadeiro
            janela['valor recebido'].update(distribuicao.recebeuporfora(reais))


        elif valores['recebeu fora'] == False and valores['salario'] == False and valores['investimento'] == True:
            janela['valor recebido'].update(distribuicao.investimentos(reais))

        else:
            janela['valor recebido'].update('APERTE AO MENOS UM PARA CALCULAR')
janela.close()
