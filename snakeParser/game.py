from snakeParser import SNAKE_DIRECTION
from random import randint
import functools


class SnakeGame:
    """
    SnakeGame class to hold a current game state. Exports to a PIL image (useful in notebooks)
    TODO: write good code != this
    TODO: ooh maybe make this an iterable????
    """

    def __init__(self):
        # Current Frame
        self._frame = 0

        # Size of Gameboard
        self._width = 16
        self._height = 16

        self.alive = True

        self.apple = (0, 0)

        self.snake = [(10, 12), (11, 12), (12, 12)]
        self.direction = SNAKE_DIRECTION['RIGHT']

        # Buffer in which to queue moves for execution
        self.move_buffer = []

    """
    def parse_game(self, gamestr):
        self._events = [(int(e[0]), e[1], *map(int, e[2:])) for e in [e.split(' ') for e in gamestr.split(';')]]
    """
    
    def __iter__(self):
        return self

    # generate new frames until death
    def __next__(self):
        # Load in all events for current frame
        # events = [tuple(*e[1:]) for e in filter(lambda x: x[0] == self._frame, self._events)]

        # Apply events to state
        # for e in events:
        #     if e[0] == 'A':
        #         self.apple = (e[1], e[2])
        #     elif e[0] == 'M':
        #         self.move_buffer.append(e[1])
        if not self:
            raise StopIteration

        # Apply current move from buffer into state
        if self.move_buffer:
            self.direction = self.move_buffer.pop(0)

        # Move one space in direction
        self.snake.pop(0)
        if self.direction == SNAKE_DIRECTION['LEFT']:
            self.snake.append((self.snake[-1][0] - 1, self.snake[-1][1]))
        elif self.direction == SNAKE_DIRECTION['RIGHT']:
            self.snake.append((self.snake[-1][0] + 1, self.snake[-1][1]))
        elif self.direction == SNAKE_DIRECTION['UP']:
            self.snake.append((self.snake[-1][0], self.snake[-1][1] + 1))
        elif self.direction == SNAKE_DIRECTION['DOWN']:
            self.snake.append((self.snake[-1][0], self.snake[-1][1] - 1))

        # detect apple
        if self.snake[-1] == self.apple:
            self.snake.append(self.apple)

        # TODO: write some bloody tests
        """
        Remember that this terrible code has the purpose of emulating the bug in the js version.
        """
        # detect collision internal
        if self.snake[-1] in self.snake[:-2]:
            self.alive = False
        
        # detect external collision y-axis
        if 0 > self.snake[-1][1] or self.snake[-1][1] > 31:
            self.alive = False

        # detect external collision x-axis
        if 0 > self.snake[-1][0] or self.snake[-1][0] > 31:
            self.alive = False

        return self
    
    # Append move to buffer
    def add_move(self, direction):
        self.move_buffer.append(direction)

    def rand_apple_pos(self):
        self.apple = (randint(0, 31), randint(0, 31))
        while self.apple in self.snake:
            self.apple = (randint(0, 31), randint(0, 31))

    # current length of snake
    def __len__(self):
        return len(self.snake) - 3

    # allows for shorthand use of instance to check if alive
    def __bool__(self):
        return self.alive

    """
    # Output ascii representation of gameboard. . use the matplotlib image version in the notebook
    def __repr__(self):
        board = [[' '] * 16] * 16
        board[self.apple[0]][self.apple[1]] = 'A'
        board[self.snake[0][0]][self.snake[0][1]] = 'H'
        for s in self.snake[1:]:
            board[s[0]][s[1]] = 'S'
    """