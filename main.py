import PySimpleGUI as g

ic = 'mai.ico'

g.theme('default1')

layout_1 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОНА', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Input('2', tooltip='Например 2', size=(13, 1), justification='center', pad=(213, 5))],
            [g.Image(source='neuron.png')],
            [g.Input('3', tooltip='Например 3', size=(13, 1), justification='center', pad=(213, 5))],
            [g.Button('Посчитать'), g.Output(expand_x=True)],
            [g.StatusBar('НИЖНИЙ ТЕКСТ', justification='center', expand_x=True, font='Impact 30 normal')]]

layout_2 = [[g.Text('ПРИМЕР РАБОТЫ НЕЙРОСЕТИ', justification='center', expand_x=True, font='Impact 30 normal')],
            [g.Image(source='image.png')],
            [],
            [g.FileBrowse('Выбрать файл'), g.FileSaveAs('Сохранить как')]]

layout_0 = [[g.TabGroup([[g.Tab('Нейрон', layout_1), g.Tab('Сеть', layout_2)]])]]
window = g.Window('Нейросети', layout_0, finalize=True, icon=ic)

print('Результат')
while True:
    event, values = window.read()
    if event == g.WIN_CLOSED:
        break
    print('Результат')
window.close()
