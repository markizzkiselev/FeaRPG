import pygame.sprite
from numpy import array
from config import *
from sprite_classes import *
from collide_func import *
from random import choice


class Board:
    def __init__(self, dim, screen):
        self.x_px = dim[0]
        self.y_px = dim[1]

        self.x = self.x_px // CELL_SIZE * 3
        self.y = self.y_px // CELL_SIZE * 3

        self.x_n = 0
        self.y_n = 0

        self.map = [
            '111111111111111111111111111111',
            '100000000000000030000000000001',
            '100000000000000000000003000001',
            '100000000000000300000000000001',
            '100055552255500000004000000001',
            '100052222222500000000000030001',
            '100052222222500000000000000001',
            '100052222229500030000000000001',
            '100052222555500000000000003001',
            '100052222500000000003000000001',
            '100052222500000000000000000001',
            '100052222500000000000030000001',
            '100052222200000000000000000001',
            '100052222200000003000000000001',
            '100052222500000000000000003001',
            '100052222500000000000000000001',
            '100455555500000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '100000000000000000000000000001',
            '774220000000000007700000000001',
            '777227777700000077770000000001',
            '777227777777700777777000000001',
            '100220077777777777777000000041',
            '100000000077777777777700000001',
            '100000000077777777777770000001',
            '100000000000007777777777700001',
            '100110000000007777777777000001',
            '100011000000000777777777000001',
            '100001100000000077777700000001',
            '110000100000000007770000000001',
            '111000100000000007770000000001',
            '111001100000000007770000000001',
            '110001000000000007770000000001',
            '110001000000000007770000000001',
            '100001000000000007700000000001',
            '100001100000000007700000000001',
            '110000100000000007770002200001',
            '110000110000000000777772277001',
            '100000011000000000077772277777',
            '100030001000000000000002200777',
            '110040001000000000000000000007',
            '110000011000000000000000000001',
            '111000010000000000000000000001',
            '111111111111111111111111111111'
        ]

        self.s_matrix = []
        for i in range(60):
            row = []
            for j in range(30):
                row.append(self.map[i][j])
            self.s_matrix.append(row)
        self.matrix = array(self.s_matrix)

        self.speed = 4
        self.count = 0
        self.end = False

        self.screen = screen

        self.block_list = pygame.sprite.Group()
        self.chest_list = pygame.sprite.Group()
        self.all_block_list = pygame.sprite.Group()
        self.inventory_list = pygame.sprite.Group()

        self.IMAGE_0 = pygame.image.load(
            'Sprites/floor_of_icex4.png'
        ).convert_alpha()
        self.IMAGE_1 = pygame.image.load(
            'Sprites/block_of_icex4.png'
        ).convert_alpha()
        self.IMAGE_2 = pygame.image.load(
            'Sprites/boardsx4.png'
        ).convert_alpha()
        self.IMAGE_3 = pygame.image.load(
            'Sprites/treex4.png'
        ).convert_alpha()
        self.IMAGE_4 = pygame.image.load(
            'Sprites/goldchestx4.png'
        ).convert_alpha()
        self.IMAGE_5 = pygame.image.load(
            'Sprites/wallx4.png'
        ).convert_alpha()
        self.IMAGE_6 = pygame.image.load(
            'Sprites/open_goldchestx4.png'
        ).convert_alpha()
        self.IMAGE_7 = pygame.image.load(
            'Sprites/waterx4.png'
        ).convert_alpha()
        self.IMAGE_8 = pygame.image.load(
            'Sprites/open_chestx4.png'
        ).convert_alpha()
        self.IMAGE_9 = pygame.image.load(
            'Sprites/chestx4.png'
        ).convert_alpha()

    def up(self):
        for i in self.block_list:
            if collide(i, h=self.speed):
                return
        self.y_n -= self.speed
        self.draw_map()

    def down(self):
        for i in self.block_list:
            if collide(i, h=-self.speed):
                return
        self.y_n += self.speed
        self.draw_map()

    def right(self):
        for i in self.block_list:
            if collide(i, w=-self.speed):
                return
        self.x_n += self.speed
        self.draw_map()

    def left(self):
        for i in self.block_list:
            if collide(i, w=self.speed):
                return
        self.x_n -= self.speed
        self.draw_map()

    def up_and_left(self):
        for i in self.block_list:
            if collide(i, w=self.speed, h=self.speed):
                return
        self.y_n -= self.speed
        self.x_n -= self.speed
        self.draw_map()

    def up_and_right(self):
        for i in self.block_list:
            if collide(i, w=-self.speed, h=self.speed):
                return
        self.y_n -= self.speed
        self.x_n += self.speed
        self.draw_map()

    def down_and_left(self):
        for i in self.block_list:
            if collide(i, w=self.speed, h=-self.speed):
                return
        self.y_n += self.speed
        self.x_n -= self.speed
        self.draw_map()

    def down_and_right(self):
        for i in self.block_list:
            if collide(i, w=-self.speed, h=-self.speed):
                return
        self.y_n += self.speed
        self.x_n += self.speed
        self.draw_map()

    def is_find(self):
        for i in self.chest_list:
            if collide_1(i):
                return True
        return False

    def open(self):
        for i in self.chest_list:
            if collide_1(i):
                if self.matrix[i.a][i.b] == '9':
                    self.matrix[i.a][i.b] = '8'
                    shovel = Item(len(self.inventory_list),
                                  'Sprites/shovelx8.png', self.inventory_list)
                if self.matrix[i.a][i.b] == '4':
                    self.matrix[i.a][i.b] = '6'
                    self.count += 1
                    if self.count >= 5:
                        self.end = True

    def draw_cell(self, xy):
        try:
            if xy[0] < 0 or xy[1] < 0:
                raise IndexError
            elif self.matrix[xy[0]][xy[1]] == '0':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_0, xy[0], xy[1], self.all_block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '1':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_1, xy[0], xy[1], self.all_block_list,
                    self.block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '2':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_2, xy[0], xy[1], self.all_block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '3':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_3, xy[0], xy[1], self.all_block_list,
                    self.block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '4':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_4, xy[0], xy[1], self.all_block_list,
                    self.block_list, self.chest_list
                )
            elif self.matrix[xy[0]][xy[1]] == '5':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_5, xy[0], xy[1], self.all_block_list,
                    self.block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '6':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_6, xy[0], xy[1], self.all_block_list,
                    self.block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '7':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_7, xy[0], xy[1], self.all_block_list,
                    self.block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '8':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_8, xy[0], xy[1], self.all_block_list,
                    self.block_list
                )
            elif self.matrix[xy[0]][xy[1]] == '9':
                block = Block(
                    xy[0] * CELL_SIZE - self.x_n, xy[1] * CELL_SIZE - self.y_n,
                    self.IMAGE_9, xy[0], xy[1], self.all_block_list,
                    self.block_list, self.chest_list
                )
        except IndexError:
            pass

    def draw_map(self):
        self.screen.fill((214, 255, 250))
        self.block_list = pygame.sprite.Group()
        self.chest_list = pygame.sprite.Group()
        self.all_block_list = pygame.sprite.Group()
        for i in range(self.x_n // CELL_SIZE - 1, self.x_n // CELL_SIZE + self.x_px // CELL_SIZE + 1):
            for j in range(self.y_n // CELL_SIZE - 1, self.y_n // CELL_SIZE + self.y_px // CELL_SIZE + 2):
                self.draw_cell([i, j])
        self.all_block_list.draw(self.screen)

    def draw_text(self):
        font = pygame.font.Font('Fonts/PixelFont.ttf', 64)
        text = font.render(f"{self.count}", True, (255, 255, 255))
        self.screen.blit(text,
                         (DIMENSIONS[0] - CELL_SIZE * 2 -
                          text.get_width() // 2.5,
                          CELL_SIZE * 2 - text.get_height() // 2.5))
