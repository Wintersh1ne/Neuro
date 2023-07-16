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
            [g.Button('Посчитать', enable_events=True, key='-COUNT-',), g.Output(expand_x=True)],
            [g.StatusBar('НИЖНИЙ ТЕКСТ', justification='center', expand_x=True, font='Impact 30 normal')]]

layout_2 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Image(source='image.png')],
            [],
            [g.Button('Настроить', enable_events=True, key='Parametrize')],
            [g.Button('Посчитать', enable_events=True, key='count',), g.Output(expand_x=True)]]

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

layout_0 = [[g.TabGroup([[g.Tab('Нейрон', layout_1), g.Tab('Сеть', layout_2)]])]]
window = g.Window('Нейросети', layout_0, finalize=True, icon=ic)
window_params = g.Window('Нейросети', layout_3, finalize=True, icon=ic, enable_close_attempted_event=True)
window_params.disappear()
data = np.array([
    [-2, -1],  # Alice
    [25, 6],  # Bob
    [17, 4],  # Charlie
    [-15, -6],  # Diana
])

all_y_trues = np.array([
    1,  # Alice
    0,  # Bob
    0,  # Charlie
    1,  # Diana
])

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

    if event == 'count':        #дописать
        try:
            w = [int(layout_3[1][3].get()), int(layout_3[1][5].get()), int(layout_3[2][3].get()), int(layout_3[2][5].get()), int(layout_3[3][3].get()), int(layout_3[4][3].get())]
            b = [int(layout_3[3][1].get()), int(layout_3[4][1].get()), int(layout_3[5][1].get())]
            nw = neuro.OurNeuralNetwork(2, 3, w, b)
            nw.train(data, all_y_trues)
            inp = np.array([int(layout_3[1][1].get()), int(layout_3[2][1].get())])
            if nw.feedforward(inp) > 0.5:
                print("\n1st case with %.15f number" % nw.feedforward(inp), end="")
            else:
                print("\n2nd case with %.15f number" % nw.feedforward(inp), end="")
        except:
            g.popup("Check all parametres. They must be digitals for sure!")

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
                if len(values_p[event_p]) == 1 and values_p[event_p][0] not in ('0123456789'):
                    g.popup("Only digits allowed")
                    window_params[event_p].update("")
                if len(values_p[event_p]) > 1:
                    if values_p[event_p][-1] not in ('0123456789'):
                        g.popup("Only digits allowed")
                        window_params[event_p].update(values_p['Input_x'][:-1])
                    if values_p[event_p][0] not in ('-0123456789'):
                        g.popup("Only digits allowed")
                        window_params[event_p].update(values_p[event_p][1:])

window.close()
exit(0)