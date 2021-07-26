from PyInquirer import prompt
from dialog import Dialog
from random import randint
from pprint import pprint

questions = [
    {
        'type': 'input',
        'name': 'color_val',
        'message': 'Entre com a cor (#XXXXXX  r,g,b ou vazio para cor aleatória): ',
    },
    {
        'type': 'input',
        'name': 'learning_rate',
        'message': 'Entre com a taxa de aprendizado: ',
        'default': '0.01'
    },
    {
        'type': 'input',
        'name': 'epochs',
        'message': 'Entre com a quantidade de epochs: ',
        'default': '10'
    },
    {
        'type': 'confirm',
        'name': 'debug',
        'message': 'Mostar os neurônios ativados ?'
    },
]


def hex_to_rgb(c: str) -> list:
    h = c.lstrip('#')
    return list(int(h[i:i+2], 16) for i in (0, 2, 4))


def normalization(val, min: int = 0, max: int = 255) -> float:
    return [2*((v-min)/(max-min) - 0.5) for v in val]


dados = [
    # Vermelho
    [[1, -1, -1], (+1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)],
    # Verde
    [[-1, 1, -1, ], (-1.0, +1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0)],
    # Azul
    [[-1, -1, 1, ], (-1.0, -1.0, +1.0, -1.0, -1.0, -1.0, -1.0, -1.0)],
    # Preto
    [[-1, -1, -1, ], (-1.0, -1.0, -1.0, +1.0, -1.0, -1.0, -1.0, -1.0)],
    # Branca
    [[1, 1, 1, ], (-1.0, -1.0, -1.0, -1.0, +1.0, -1.0, -1.0, -1.0)],
    # Amarelo
    [[1, 1, -1], (-1.0, -1.0, -1.0, -1.0, -1.0, +1.0, -1.0, -1.0)],
    # Magenta
    [[1, -1, 1], (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, +1.0, -1.0)],
    # Ciano
    [[-1, 1, 1, ], (-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0, +1.0)]]


class Neuronio:
    def __init__(self, learning_rate: float) -> None:
        self.weights = [0, 0, 0]
        self.y = 0
        self.learning_rate = learning_rate

    def calculate(self, vals: list) -> float:

        res = [x*w for x, w in zip(vals, self.weights)]
        self.y = sum(res) + 1
        return self.y

    def correct_weights(self, inputs: list, expected: float) -> None:
        error = expected - self.y
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + \
                self.learning_rate * error * inputs[i]


class Perceptron:
    def __init__(self, dados: list, learning_rate: float = 0.2, epochs: int = 1) -> None:
        self.neurons = [Neuronio(learning_rate=learning_rate)
                        for _ in range(8)]
        self.dados = dados
        self.epochs = epochs

    def train(self) -> None:
        for _ in range(self.epochs):
            for input in self.dados:
                for n in range(len(self.neurons)):
                    self.neurons[n].calculate(input[0])
                    self.neurons[n].correct_weights(input[0], input[1][n])

    def predict(self, inputs: list, debug: bool = False) -> Dialog:

        dialog = Dialog(r=inputs[0], g=inputs[1], b=inputs[2])

        predicts = [self.neurons[i].calculate(
            normalization(inputs)) for i in range(len(self.neurons))]
        color = predicts.index(max(predicts))

        if debug:
            pprint(predicts)

        if color == 0:
            dialog.set_text('Vermelho!')
        elif color == 1:
            dialog.set_text('Verde!')
        elif color == 2:
            dialog.set_text('Azul!')
        elif color == 3:
            dialog.set_text('Preto!')
        elif color == 4:
            dialog.set_text('Branco!')
        elif color == 5:
            dialog.set_text('Amarelo!')
        elif color == 6:
            dialog.set_text('Magenta!')
        else:
            dialog.set_text('Ciano!')

        return dialog


def main():

    answers = prompt(questions)

    learning_rate = float(answers['learning_rate'])
    epochs = int(answers['epochs'])

    if '#' in answers['color_val']:
        color = hex_to_rgb(answers['color_val'])
    elif len(answers['color_val']) == 0:
        color = [randint(0, 255), randint(0, 255), randint(0, 255)]
        Dialog(f'Cor aleatória foi: {color}').show()
    else:
        color = list(map(int, answers['color_val'].split(',')))

    perceptron = Perceptron(dados, learning_rate=learning_rate, epochs=epochs)
    perceptron.train()

    perceptron.predict(color, debug=answers['debug']).show()


if __name__ == '__main__':
    main()
