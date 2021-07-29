# Criado por @hr80 apenas
# Modificado para minhas necessidades


class Dialog:
    def __init__(self, *lines: str, r: int = 255, g: int = 255, b: int = 255):
        if len(lines) != 0:
            self.lines = lines
            self.max_len = max(map(lambda x: len(x), lines))
            self.max_len += 2

        self.r = r
        self.g = g
        self.b = b

    def show(self):
        if hasattr(self, 'lines'):
            print(f'\033[38;2;{self.r};{self.g};{self.b}m', end='')
            self.print_division('╔', '╗')
            for line in self.lines:
                self.print_text(line)
            self.print_division('╚', '╝')
            print('\033[0m')
        else:
            print('There is not text to be showed!!! Try setting text with set_text()')

    def print_division(self, begin: str, end: str):
        print(begin + '═' * self.max_len + end)

    def print_text(self, text: str):
        print('║' + text.center(self.max_len, ' ') + '║')

    def set_text(self, *text: str) -> None:
        self.lines = text
        self.max_len = max(map(lambda x: len(x), text))
        self.max_len += 2
