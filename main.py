import PySimpleGUI as g
import numpy as np
import neuro

ic = 'mai.ico'

g.theme('default1')

layout_1 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОНА', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Input('0', enable_events=True, key='Input_1',  tooltip='Например 0', size=(5, 1), justification='center', pad=(60, 5)),
             g.Input('2', enable_events=True, key='-INPUT1-', tooltip='Например 2', size=(5, 1), justification='center', pad=(165, 5))],
            [g.Input('4', enable_events=True, key='bias',     tooltip='Например 4', size=(5, 1),  justification='center'),
             g.Image(source='neuron.png')],
            [g.Input('1', enable_events=True, key='Input_2',  tooltip='Например 1', size=(5, 1), justification='center', pad=(60, 5)),
             g.Input('3', enable_events=True, key='-INPUT2-', tooltip='Например 3', size=(5, 1), justification='center', pad=(165, 5))],
            [g.Button('Посчитать', enable_events=True, key='-COUNT-',)],
            ]

layout_2 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Image(source='image.png')],
            [],
            [g.Button('Настроить', enable_events=True, key='Parametrize'), g.Button('Информация', enable_events=True, key='Info')],
            [g.Button('Посчитать', enable_events=True, key='count',)]]

layout_3 = [[g.Text('ПАРАМЕТРЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Text('x:   '), g.Input('0', enable_events=True, key='Input_x', tooltip='Например 0', size=(5, 1), justification='center'),
             g.Text('weight 1: '), g.Input('2', enable_events=True, key='Input_weight_x_1', tooltip='Например 2', size=(15, 1), justification='center'),
             g.Text('weight 3: '), g.Input('2', enable_events=True, key='Input_weight_x_2', tooltip='Например 2', size=(15, 1), justification='center')],
            [g.Text('y:   '), g.Input('1', enable_events=True, key='Input_y', tooltip='Например 1', size=(5, 1), justification='center'),
             g.Text('weight 2: '), g.Input('3', enable_events=True, key='Input_weight_y_1', tooltip='Например 3', size=(15, 1), justification='center'),
             g.Text('weight 4: '), g.Input('2', enable_events=True, key='Input_weight_y_2', tooltip='Например 2', size=(15, 1), justification='center')],
            [g.Text('b1: '), g.Input('1', enable_events=True, key='Input_b1', tooltip='Например 1', size=(5, 1), justification='center'),
             g.Text('weight 5: '), g.Input('3', enable_events=True, key='Input_weight_b1', tooltip='Например 3', size=(15, 1), justification='center')],
            [g.Text('b2: '), g.Input('1', enable_events=True, key='Input_b2', tooltip='Например 1', size=(5, 1), justification='center'),
             g.Text('weight 6: '), g.Input('3', enable_events=True, key='Input_weight_b2', tooltip='Например 3', size=(15, 1), justification='center')],
            [g.Text('b3: '), g.Input('1', enable_events=True, key='Input_b3', tooltip='Например 1', size=(5, 1), justification='center')],
            [g.Button('Save and return', enable_events=True, key='save_and_return')]]

layout_info = [[g.Text('ПАРАМЕТРЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
               [g.Text('ПАРАМЕТРЫ НЕЙРОСЕТИ', justification='center', expand_x=True, expand_y=True)],
               [g.Button('ОК', enable_events=True, key='return')]]

layout_0 = [[g.TabGroup([[g.Tab('Нейрон', layout_1), g.Tab('Сеть', layout_2)]])], [g.Output(expand_x=True)]]
window = g.Window('Нейросети', layout_0, finalize=True, icon=ic)
window_params = g.Window('Нейросети', layout_3, finalize=True, icon=ic, enable_close_attempted_event=True)
window_params.disappear()
window_info = g.Window('Нейросети', layout_info, finalize=True, icon=ic, enable_close_attempted_event=True)
window_info.disappear()
data = np.array([
    [-2, -1],
    [25, 6],
    [17, 4],
    [-15, -6],
])

all_y_trues = np.array([
    1,
    0,
    0,
    1,
])

p_s = ''
w = [int(layout_3[1][3].get()), int(layout_3[1][5].get()), int(layout_3[2][3].get()), int(layout_3[2][5].get()), int(layout_3[3][3].get()), int(layout_3[4][3].get())]
b = [int(layout_3[3][1].get()), int(layout_3[4][1].get()), int(layout_3[5][1].get())]
global nw
nw = neuro.OurNeuralNetwork(2, 3, w, b)
while True:
    event, values = window.read()
    if event == g.WIN_CLOSED:
        break

    if event in ['-INPUT1-', '-INPUT2-', 'Input_1', 'Input_2', 'bias']:
        if values[event] != "":
            if values[event][0] not in ('-0123456789'):
                g.popup("Только цифры!")
                window[event].update(values[event][1:])
            elif len(values[event]) > 1 and values[event][-1] not in ('0123456789'):
                g.popup("Только цифры!")
                window[event].update(values[event][:-1])

    if event == '-COUNT-':
        try:
            n = neuro.Neuron(np.array([int(layout_1[1][0].get()), int(layout_1[3][0].get())]), int(layout_1[2][0].get()))
            print('\nРезультат: ', n.feedforward(np.array([int(layout_1[1][1].get()), int(layout_1[3][1].get())])), end="")
        except:
            g.popup("Проверьте все значения, они должны являться числами.")

    if event == 'count':
        try:
            w = [int(layout_3[1][3].get()), int(layout_3[1][5].get()), int(layout_3[2][3].get()), int(layout_3[2][5].get()), int(layout_3[3][3].get()), int(layout_3[4][3].get())]
            b = [int(layout_3[3][1].get()), int(layout_3[4][1].get()), int(layout_3[5][1].get())]
            nw = neuro.OurNeuralNetwork(2, 3, w, b)
            nw.train(data, all_y_trues)
            inp = np.array([int(layout_3[1][1].get()), int(layout_3[2][1].get())])
            if nw.feedforward(inp) > 0.5:
                print("\nПервый тип. Значение: %.15f" % nw.feedforward(inp), end="")
            else:
                print("\nВторой тип. Значение: %.15f" % nw.feedforward(inp), end="")
        except:
            g.popup("Проверьте все значения, они должны являться числами.")

    if event == 'Parametrize':
        window.disable()
        window_params.reappear()
        window_params.force_focus()
        while True:
            event_p, values_p = window_params.read()
            if event_p == 'save_and_return':
                window_params.disappear()
                window.enable()
                break
            if event_p in ['Input_x', 'Input_y', 'Input_b1', 'Input_b2', 'Input_b3', 'Input_weight_x_1', 'Input_weight_x_2', 'Input_weight_y_1', 'Input_weight_y_2', 'Input_weight_b1', 'Input_weight_b2']:
                if len(values_p[event_p]) == 1 and values_p[event_p][0] not in ('-0123456789'):
                    g.popup("Только цифры!")
                    window_params[event_p].update("")
                if len(values_p[event_p]) > 1:
                    if values_p[event_p][-1] not in ('0123456789'):
                        g.popup("Только цифры!")
                        window_params[event_p].update(values_p['Input_x'][:-1])
                    if values_p[event_p][0] not in ('-0123456789'):
                        g.popup("Только цифры!")
                        window_params[event_p].update(values_p[event_p][1:])

    if event == 'Info':
        window.disable()
        layout_info[1][0].update(nw.GetInfo())
        window_info.reappear()
        window_info.force_focus()
        while True:
            event_i, values_i = window_info.read()
            if event_i == 'return':
                window_info.disappear()
                window.enable()
                break