from random import randint

users_path = 'Users.csv'

class Play:
    def __init__(self):
        self.level = int(input('Write Table Size(10, 15, 25): '))
        self.matrix = []
        for i in range(self.level):
            row = []
            for j in range(self.level):
                row.append('*')
            self.matrix.append(row)
        for i in range(int(self.level * self.level * 0.2)):
            self.matrix[randint(0, self.level - 1)][randint(0, self.level - 1)] = 'b'

    def start(self):
        counter = 0
        while True:
            number1, number2 = input('Please Enter Row & Column: ').split()
            number1 = int(number1)
            number2 = int(number2)
            if self.matrix[number1][number2] == 'b':
                print('Lose :(')
                for i in range(self.level):
                    s = ''
                    for j in range(self.level):
                        if self.matrix[i][j] == 'b':
                            s += 'x '
                        else:
                            s +='* '
                    print(s)
                return counter
            elif self.matrix[number1][number2] == '-':
                continue
            else:
                counter += 1
                self.matrix[number1][number2] = '-'
            self.print_state()
            num = 0
            for i in range(self.level):
                for j in range(self.level):
                    if self.matrix[i][j] == '*':
                        num = 1
                        break
            if num == 0:
                print('Win :)')
                return counter


    def print_state(self):
        for i in range(self.level):
            s = ''
            for j in range(self.level):
                if self.matrix[i][j] == '*' or self.matrix[i][j] == 'b':
                    s += '*'
                elif self.matrix[i][j] == '-':
                    counter = 0
                    if i > 1 and self.matrix[i-1][j] == 'b':
                        counter += 1
                    if i < self.level - 1 and self.matrix[i+1][j] == 'b':
                        counter += 1
                    if j > 1 and self.matrix[i][j-1] == 'b':
                        counter += 1
                    if j < self.level - 1 and self.matrix[i][j+1] == 'b':
                        counter += 1
                    s += str(counter)
                s += ' '
            print(s)