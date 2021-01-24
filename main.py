import pygame
from random import choice


def wall_check(block, mod):
    for i in block:
        if i[mod]:
            return False
    return True


def no_blocks_under(board, level, block):
    for i in range(len(block)):
        for j in range(8):
            if level - i >= 0:
                if block[-i-1][j] and board[level - i][j]:
                    return True
    return False


def level_check(board):
    for item in range(tetris.height):
        if len([i for i in board[item] if i]) == tetris.width:
            if item == tetris.height - 1:
                board = [[0] * tetris.width] + board[1:]
                tetris.levels_broken += 1
            if not item:
                board = [[0] * tetris.width] + board[:-1]
            else:
                board = [[0] * tetris.width] + board[:item] + board[item+1:]
                tetris.levels_broken += 1
        item -= 1
    return board


pygame.init()
size = 378, 630
screen = pygame.display.set_mode(size)

class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[0] * self.width for _ in range(self.height)]
        self.left = 10
        self.top = 120
        self.cell_size = 45
        self.colors = [(0, 0, 0), (255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 0, 255), (0, 128, 0),
                       (0, 255, 255)]
        self.font = pygame.font.Font(None, 40)
        self.levels_broken = 0

    def render(self):
        text = self.font.render(f'Уровней сломано: {self.levels_broken}', True, [255, 255, 255])
        screen.blit(text, (10, 50))
        for y in range(self.height):
            for x in range(self.width):
                pygame.draw.rect(screen, self.colors[self.board[y][x]], (
                    x * self.cell_size + self.left, y * self.cell_size + self.top,
                    self.cell_size, self.cell_size))
                pygame.draw.rect(screen, pygame.Color("white"),
                                 (x * self.cell_size + self.left,
                                  y * self.cell_size + self.top, self.cell_size, self.cell_size), 1)


class Tetris(Board):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.blocks = [
            [
                [[0, 0, 1, 1, 1, 1, 0, 0]],
                [[0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0],
                 [0, 0, 0, 1, 0, 0, 0, 0]],
            ],
            [
                [[0, 0, 0, 2, 0, 0, 0, 0],
                 [0, 0, 0, 2, 2, 2, 0, 0]],
                [[0, 0, 0, 0, 2, 2, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0]],
                [[0, 0, 0, 2, 2, 2, 0, 0],
                 [0, 0, 0, 0, 0, 2, 0, 0]],
                [[0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 0, 2, 0, 0, 0],
                 [0, 0, 0, 2, 2, 0, 0, 0]]
            ],
            [
                [[0, 0, 0, 0, 3, 0, 0, 0],
                 [0, 0, 3, 3, 3, 0, 0, 0]],
                [[0, 0, 0, 3, 0, 0, 0, 0],
                 [0, 0, 0, 3, 0, 0, 0, 0],
                 [0, 0, 0, 3, 3, 0, 0, 0]],
                [[0, 0, 0, 3, 3, 3, 0, 0],
                 [0, 0, 0, 3, 0, 0, 0, 0]],
                [[0, 0, 3, 3, 0, 0, 0, 0],
                 [0, 0, 0, 3, 0, 0, 0, 0],
                 [0, 0, 0, 3, 0, 0, 0, 0]]

            ],
            [
                [[0, 0, 0, 4, 0, 0, 0, 0],
                 [0, 0, 4, 4, 4, 0, 0, 0]],
                [[0, 0, 0, 4, 0, 0, 0, 0],
                 [0, 0, 0, 4, 4, 0, 0, 0],
                 [0, 0, 0, 4, 0, 0, 0, 0]],
                [[0, 0, 4, 4, 4, 0, 0, 0],
                 [0, 0, 0, 4, 0, 0, 0, 0]],
                [[0, 0, 0, 4, 0, 0, 0, 0],
                 [0, 0, 4, 4, 0, 0, 0, 0],
                 [0, 0, 0, 4, 0, 0, 0, 0]]
            ],
            [
                [[0, 0, 0, 5, 5, 0, 0, 0],
                 [0, 0, 0, 0, 5, 5, 0, 0]],
                [[0, 0, 0, 0, 5, 0, 0, 0],
                 [0, 0, 0, 5, 5, 0, 0, 0],
                 [0, 0, 0, 5, 0, 0, 0, 0]]
            ],
            [
                [[0, 0, 0, 6, 6, 0, 0, 0],
                 [0, 0, 6, 6, 0, 0, 0, 0]],
                [[0, 0, 0, 6, 0, 0, 0, 0],
                 [0, 0, 0, 6, 6, 0, 0, 0],
                 [0, 0, 0, 0, 6, 0, 0, 0]]
            ],
            [
                [[0, 0, 0, 7, 7, 0, 0, 0],
                 [0, 0, 0, 7, 7, 0, 0, 0]]
            ]
        ]
        self.saved_board = [[0] * self.width for _ in range(self.height)]
        self.level = 0
        self.game = True
        self.model = 0
        self.block = choice(self.blocks)
        self.b = self.block[self.model]

    def move(self):
        if not (self.level >= 11 or no_blocks_under(self.saved_board, self.level, self.b)):
            self.board = [i for i in self.saved_board]
            for i in range(len(self.b)):
                if self.level - i >= 0:
                    self.board[self.level - i] = [self.b[-i - 1][j] if self.b[-i - 1][j]
                                                  else self.saved_board[self.level - i][j] for j in range(8)]
            self.level += 1
        else:
            self.game = True if self.level else False
            if self.game:
                self.level = 0
                self.model = 0
                self.saved_board = level_check([i for i in self.board])
                self.block = choice(self.blocks)
                self.b = self.block[self.model]


tetris = Tetris(8, 11)
running = True
pygame.display.set_caption('Тетрис')
while running:
    tick = 3
    move_horizontal = ''
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                if not pygame.key.get_pressed()[pygame.K_s]:
                    tick = 4
            if event.key == pygame.K_w:
                if not pygame.key.get_pressed()[pygame.K_w]:
                    old_b = tetris.block[tetris.model]
                    tetris.model = (tetris.model + 1) % len(tetris.block)
                    tetris.b = tetris.block[tetris.model]
                    tetris.level -= 1
                    tick = 5
            if event.key == pygame.K_a:
                if not pygame.key.get_pressed()[pygame.K_a]:
                    move_horizontal = 'left'
            if event.key == pygame.K_d:
                if not pygame.key.get_pressed()[pygame.K_d]:
                    move_horizontal = 'right'
        elif pygame.key.get_pressed():
            if pygame.key.get_pressed()[pygame.K_s]:
                tick = 4
            if pygame.key.get_pressed()[pygame.K_w]:
                if tick != 5:
                    old_b = tetris.block[tetris.model]
                    tetris.model = (tetris.model + 1) % len(tetris.block)
                    tetris.b = tetris.block[tetris.model]
                    tetris.level -= 1
                    tick = 5
            if pygame.key.get_pressed()[pygame.K_a]:
                move_horizontal = 'left'
            if pygame.key.get_pressed()[pygame.K_d]:
                move_horizontal = 'right'
    if tetris.game:
        screen.fill((0, 0, 0))
        if move_horizontal:
            if move_horizontal == 'right':
                for item in tetris.block:
                    if wall_check(item, -1):
                        for j in range(len(item)):
                            item[j] = [item[j][-1]] + item[j][:-1]
                            tick = 4
            else:
                for item in tetris.block:
                    if wall_check(item, 0):
                        for j in range(len(item)):
                            item[j] = item[j][1:] + [item[j][0]]
                            tick = 4

        tetris.move()
        tetris.render()
        pygame.display.flip()
        pygame.time.Clock().tick(tick)
    else:
        running = False
