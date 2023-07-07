import PySimpleGUI as g

import neuro

ic = 'mai.ico'

g.theme('default1')

layout_1 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОНА', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Input('2', enable_events=True, key='-INPUT1-', tooltip='Например 2', size=(13, 1), justification='center', pad=(213, 5))],
            [g.Image(source='neuron.png')],
            [g.Input('3', enable_events=True, key='-INPUT2-', tooltip='Например 3', size=(13, 1), justification='center', pad=(213, 5))],
            [g.Button('Посчитать', enable_events=True, key='-COUNT-',), g.Output(expand_x=True)],
            [g.StatusBar('НИЖНИЙ ТЕКСТ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Input('0', size=(13, 1), justification='left', key='Input_1', enable_events=True)],
            [g.Input('1', size=(13, 1), justification='left', key='Input_2', enable_events=True)]]

layout_2 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Image(source='image.png')],
            [],
            [g.FileBrowse('Выбрать файл'), g.FileSaveAs('Сохранить как')]]

layout_0 = [[g.TabGroup([[g.Tab('Нейрон', layout_1), g.Tab('Сеть', layout_2)]])]]
window = g.Window('Нейросети', layout_0, finalize=True, icon=ic)

print('Результат', end="")
while True:
    event, values = window.read()
    if event == g.WIN_CLOSED:
        break
    if event == '-INPUT1-':
        if values['-INPUT1-'][-1] not in ('0123456789'):
            g.popup("Only digits allowed")
            window['-INPUT1-'].update(values['-INPUT1-'][:-1])
    if event == '-INPUT2-':
        if values['-INPUT2-'][-1] not in ('0123456789'):
            g.popup("Only digits allowed")
            window['-INPUT2-'].update(values['-INPUT2-'][:-1])
    if event == 'Input_1':
        if values['Input_1'][-1] not in ('0123456789'):
            g.popup("Only digits allowed")
            window['Input_1'].update(values['Input_1'][:-1])
    if event == 'Input_2':
        if values['Input_2'][-1] not in ('0123456789'):
            g.popup("Only digits allowed")
            window['Input_2'].update(values['Input_2'][:-1])
    if event == 'COUNT-':
        True
    print('\nРезультат: ', end="")
window.close()