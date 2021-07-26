from string import Template
from PyInquirer import prompt

from pprint import pprint

questions = [
    {
        'type': 'list',
        'name': 'rgb_or_hex',
        'message': 'Deseja entrar com a cor em hexadecimal ou RGB? ',
        'choices': [
            'Hexadecimal',
            'RGB'
        ]
    },
    {
        'type': 'input',
        'name': 'rgb_val',
        'message': 'Entre com o valor RGB (formato r,g,b ): ',
        'when': lambda ans: ans['rgb_or_hex'] == 'RGB'
    },
    {
        'type': 'input',
        'name': 'hex_val',
        'message': 'Entre com o valor hexadecimal (formato #XXXXXX ): ',
        'when': lambda ans: ans['rgb_or_hex'] == 'Hexadecimal'
    }
]


def hex_to_rgb(c):
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
    def __init__(self, learning_rate) -> None:
        self.weights = [0, 0, 0]
        self.y = 0
        self.learning_rate = learning_rate

    def calculate(self, vals) -> float:

        res = []

        for x, w in zip(vals, self.weights):
            res.append(x*w)

        self.y = sum(res)

        return self.y

    def correct_weights(self, inputs, expected) -> None:
        error = expected - self.y
        for i in range(len(self.weights)):
            self.weights[i] = self.weights[i] + \
                self.learning_rate * error * inputs[i]


class Perceptron:
    def __init__(self, dados, learning_rate=0.2, epochs=1) -> None:
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

    def predict(self, inputs) -> str:

        s = Template(
            f'\033[38;2;{inputs[0]};{inputs[1]};{inputs[2]}m$color\033[0m')

        predicts = [self.neurons[i].calculate(
            normalization(inputs)) for i in range(len(self.neurons))]
        color = predicts.index(max(predicts))

        if color == 0:
            return s.substitute(color='Vermelho!')
        elif color == 1:
            return s.substitute(color='Verde!')
        elif color == 2:
            return s.substitute(color='Azul!')
        elif color == 3:
            return s.substitute(color='Preto!')
        elif color == 4:
            return s.substitute(color='Branco!')
        elif color == 5:
            return s.substitute(color='Amarelo!')
        elif color == 6:
            return s.substitute(color='Magenta!')
        else:
            return s.substitute(color='Ciano!')


def main():

    answers = prompt(questions)

    if 'rgb_val' in answers:
        color = list(map(int, answers['rgb_val'].split(',')))
    else:
        color = hex_to_rgb(answers['hex_val'])

    perceptron = Perceptron(dados)
    perceptron.train()

    print(perceptron.predict(color))


if __name__ == '__main__':
    main()
