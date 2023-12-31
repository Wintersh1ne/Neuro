import numpy as np
def sigmoid(x):
    # Наша функция активации: f(x) = 1 / (1 + e^(-x))
    return 1 / (1 + np.exp(-x))


def deriv_sigmoid(x):
    # Производная от sigmoid: f'(x) = f(x) * (1 - f(x))
    fx = sigmoid(x)
    return fx * (1 - fx)


def mse_loss(y_true, y_pred):
    # y_true и y_pred являются массивами numpy с одинаковой длиной
    return ((y_true - y_pred) ** 2).mean()


class Neuron:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def feedforward(self, inputs):
        # Вводные данные о весе, добавление смещения
        # и последующее использование функции активации

        total = np.dot(self.weights, inputs) + self.bias
        return sigmoid(total)


class OurNeuralNetwork:
    def __init__(self, w_count_in, b_count, w, b):
        self.w_count_in = w_count_in
        self.w_count = w_count_in * (b_count - 1) + b_count - 1
        self.w = []
        self.w = w
        self.b = []
        self.b = b
        self.h = [0] * (b_count - 1)
        self.d_ypred_d_h = [0] * len(self.h)
        self.d_ypred_d_w = [0] * len(self.h)
        self.d_ypred_d_b = 0
        self.d_h_d_w = [0] * len(self.h) * w_count_in
        self.d_h_d_b = [0] * len(self.h)
        self.o = -1

    def feedforward(self, x):
        k = 0
        for i in range(0, len(self.b) - 1):
            summ = 0
            for j in range(0, self.w_count_in):
                summ += self.w[j + k] * x[j]
            k += self.w_count_in
            self.h[i] = (sigmoid(summ + self.b[i]))

        summ = 0
        for i in range(0, len(self.b) - 1):
            summ += self.w[len(self.w) - len(self.b) + i] * self.h[i]
        o = sigmoid(summ + self.b[-1])

        self.o = o
        return o

    def train(self, data, all_y_trues):
        learn_rate = 0.1
        epochs = 10000

        for epoch in range(epochs):
            for x, y_true in zip(data, all_y_trues):
                # --- Выполняем обратную связь (нам понадобятся эти значения в дальнейшем)

                sums = [0] * len(self.b)
                for i in range(0, len(self.b) - 1):
                    for j in range(0, len(self.w) // len(self.b)):
                        sums[i] += self.w[j + j * (len(self.w) // len(self.b))] * x[j]
                    self.h[i] = (sigmoid(sums[i] + self.b[i]))

                # +++
                for i in range(0, len(self.b) - 1):
                    sums[-1] += self.w[len(self.w) - len(self.b) - 1 + i] * self.h[i]
                o = sigmoid(sums[-1] + self.b[-1])

                y_pred = o

                # --- Подсчет частных производных
                # --- Наименование: d_L_d_w1 представляет "частично L / частично w1"
                d_L_d_ypred = -2 * (y_true - y_pred)

                # h
                j, k = 0, 0
                for i in range(0, len(self.d_h_d_w)):
                    self.d_h_d_w[i] = x[j] * deriv_sigmoid(sums[k])
                    j += 1
                    if j == len(x):
                        j = 0
                        k += 1

                for i in range(0, len(self.d_h_d_b)):
                    self.d_h_d_b[i] = deriv_sigmoid(sums[i])

                # o
                for i in range(0, len(self.h)):
                    self.d_ypred_d_w[i] = (self.h[i] * deriv_sigmoid(sums[-1]))

                j = 0
                for i in range(self.w_count - len(self.b) + 1, self.w_count):
                    self.d_ypred_d_h[j] = (self.w[i] * deriv_sigmoid(sums[-1]))
                    j += 1

                d_ypred_d_b = deriv_sigmoid(sums[-1])

                j, c = 0, 0
                for i in range(0, self.w_count - self.w_count_in):
                    if c > self.w_count_in:
                        self.b[j] -= learn_rate * d_L_d_ypred * self.d_ypred_d_h[j] * self.d_h_d_b[j]
                        j += 1
                        c = 0
                    self.w[i] -= learn_rate * d_L_d_ypred * self.d_ypred_d_h[j] * self.d_h_d_w[i]

                    c += 1

                j = 0
                for i in range(self.w_count - len(self.b) + 1, self.w_count):
                    self.w[i] -= learn_rate * d_L_d_ypred * self.d_ypred_d_w[j]
                    j += 1
                self.b[-1] -= learn_rate * d_L_d_ypred * d_ypred_d_b

    def GetInfo(self):
        s = ''
        c = 0
        for i in self.w:
            c += 1
            s = s + 'Вес w' + str(c) + ': ' + str(i) + '\n'
        c = 0
        for i in self.h:
            c += 1
            s = s + 'Значение b' + str(c) + ' нейрона скрытого слоя: ' + str(i) + '\n'
        c = 0
        for i in self.b:
            c += 1
            s = s + 'Смещение h' + str(c) + ': ' + str(i) + '\n'
        if self.o != -1:
            s = s + 'Значение нейрона вывода о: ' + str(self.o) + '\n'
        else:
            s += 'Значение нейрона слоя вывода отсутствует. Произведите рассчёты.'

        return s
