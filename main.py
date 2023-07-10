import PySimpleGUI as g
import numpy as np
import neuro

ic = 'mai.ico'

g.theme('default1')

layout_1 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОНА', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Input('0', enable_events=True, key='Input_1',  tooltip='Например 0', size=(5, 1), justification='center', pad=(60, 5)),
             g.Input('2', enable_events=True, key='-INPUT1-', tooltip='Например 2', size=(5, 1), justification='center', pad=(165, 5))],
            [g.Input('4', enable_events=True, key='bias',     tooltip='Например 2', size=(5, 1),  justification='center'),
             g.Image(source='neuron.png')],
            [g.Input('1', enable_events=True, key='Input_2',  tooltip='Например 1', size=(5, 1), justification='center', pad=(60, 5)),
             g.Input('3', enable_events=True, key='-INPUT2-', tooltip='Например 3', size=(5, 1), justification='center', pad=(165, 5))],
            [g.Button('Посчитать', enable_events=True, key='-COUNT-',), g.Output(expand_x=True)],
            [g.StatusBar('НИЖНИЙ ТЕКСТ', justification='center', expand_x=True, font='Impact 30 normal')]]

layout_2 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Image(source='image.png')],
            [],
            [g.FileBrowse('Выбрать файл'), g.FileSaveAs('Сохранить как'), g.Button('Настроить', enable_events=True, key='Parametrize')]]

layout_3 = [[g.Text('ПАРАМЕТРЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Text('x: '), g.Input('0', enable_events=True, key='Input_x', size=(5, 1), justification='center'), g.Text('weight: '), g.Input('2', enable_events=True, key='Input_weight_x', size=(15, 1), justification='center')],
            [g.Text('y: '), g.Input('1', enable_events=True, key='Input_y', size=(5, 1), justification='center'), g.Text('weight: '), g.Input('3', enable_events=True, key='Input_weight_y', size=(15, 1), justification='center')],
            [],
            [g.Button('Return', enable_events=True, key='return')]]

layout_0 = [[g.TabGroup([[g.Tab('Нейрон', layout_1), g.Tab('Сеть', layout_2)]])]]
window = g.Window('Нейросети', layout_0, finalize=True, icon=ic)
window_params = g.Window('Нейросети', layout_3, finalize=True, icon=ic, enable_close_attempted_event=True)
window_params.disappear()


while True:
    event, values = window.read()
    if event == g.WIN_CLOSED:
        break

    if event in ['-INPUT1-', '-INPUT2-', 'Input_1', 'Input_2', 'bias']:
        if values[event] != "":
            if values[event][0] not in ('-0123456789'):
                g.popup("Only digits allowed")
                window[event].update(values[event][1:])
            elif len(values[event]) > 1 and values[event][-1] not in ('0123456789'):
                g.popup("Only digits allowed")
                window[event].update(values[event][:-1])

    if event == '-COUNT-':
        try:
            n = neuro.Neuron(np.array([int(layout_1[1][0].get()), int(layout_1[3][0].get())]), int(layout_1[2][0].get()))
            print('\nРезультат: ', n.feedforward(np.array([int(layout_1[1][1].get()), int(layout_1[3][1].get())])), end="")
        except:
            g.popup("Check all parametres. They must be digitals for sure!")

    if event == 'Parametrize':
        window.disappear()
        window_params.reappear()
        while True:
            event_p, values_p = window_params.read()
            if event_p == 'return':
                window_params.disappear()
                window.reappear()
                break

            if event_p in ['Input_x', 'Input_y', 'Input_weight_x', 'Input_weight_y']:
                if len(values_p[event_p]) == 1 and values_p[event_p][0] not in ('0123456789'):
                    g.popup("Only digits allowed")
                    window_params[event_p].update("")
                if len(values_p[event_p]) > 1:
                    if values_p[event_p][-1] not in ('0123456789'):
                        g.popup("Only digits allowed")
                        window_params[event_p].update(values_p['Input_x'][:-1])
                    if values_p[event_p][0] not in ('0123456789'):
                        g.popup("Only digits allowed")
                        window_params[event_p].update(values_p[event_p][1:])

window.close()
exit(0)