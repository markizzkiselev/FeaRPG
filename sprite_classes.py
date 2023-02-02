import pygame
from config import *
from resize_func import *


class Inventory(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            'Sprites/inventoryx8.png').convert_alpha()
        self.rect = self.image.get_rect(
            center=(DIMENSIONS[0] / 2, DIMENSIONS[1] - CELL_SIZE * 2))


class StartScreen(pygame.sprite.Sprite):
    def __init__(self, file, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            file).convert_alpha()
        self.rect = self.image.get_rect(
            center=(DIMENSIONS[0] / 2, DIMENSIONS[1] / 2))


class Dad(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image_right = pygame.image.load(
            'Sprites/dadrightx4.png').convert_alpha()
        self.image_left = pygame.image.load(
            'Sprites/dadleftx4.png').convert_alpha()
        self.image_right_1 = pygame.image.load(
            'Sprites/dadrightrun1x4.png').convert_alpha()
        self.image_right_2 = pygame.image.load(
            'Sprites/dadrightrun2x4.png').convert_alpha()
        self.image_left_1 = pygame.image.load(
            'Sprites/dadleftrun1x4.png').convert_alpha()
        self.image_left_2 = pygame.image.load(
            'Sprites/dadleftrun2x4.png').convert_alpha()

        self.run = False
        self.is_right = False
        self.run_image = 1

        self.rect = self.image_left.get_rect(
            center=(DIMENSIONS[0] / 2, DIMENSIONS[1] / 2))
        self.image = self.image_left

    def right(self):
        self.is_right = True

    def left(self):
        self.is_right = False

    def anim(self):
        if self.run:
            if self.is_right:
                if self.run_image == 1:
                    self.image = self.image_right_1
                    self.run_image = 2
                else:
                    self.image = self.image_right_2
                    self.run_image = 1
            else:
                if self.run_image == 1:
                    self.image = self.image_left_1
                    self.run_image = 2
                else:
                    self.image = self.image_left_2
                    self.run_image = 1
        else:
            if self.is_right:
                self.image = self.image_right
            else:
                self.image = self.image_left


class Question(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            'Sprites/questionx4.png').convert_alpha()
        self.rect = self.image.get_rect(
            center=(DIMENSIONS[0] / 2, DIMENSIONS[1] / 2 - CELL_SIZE))


class Dark(pygame.sprite.Sprite):
    def __init__(self, file, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            file).convert_alpha()
        self.rect = self.image.get_rect(
            center=(DIMENSIONS[0] / 2, DIMENSIONS[1] / 2))


class Item(pygame.sprite.Sprite):
    def __init__(self, w, file, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            file).convert_alpha()
        self.rect = self.image.get_rect(
            center=(DIMENSIONS[0] / 2 + 8 - CELL_SIZE * 3 + w * (CELL_SIZE - 4) * 2, DIMENSIONS[1] - CELL_SIZE * 2))


class Button_C(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            'Sprites/cx8.png').convert_alpha()
        self.rect = self.image.get_rect(
            center=(CELL_SIZE * 2, CELL_SIZE * 2))


class Button_0(pygame.sprite.Sprite):
    def __init__(self, *group):
        super().__init__(*group)

        self.image = pygame.image.load(
            'Sprites/0x8.png').convert_alpha()
        self.rect = self.image.get_rect(
            center=(DIMENSIONS[0] - CELL_SIZE * 2, CELL_SIZE * 2))


class Block(pygame.sprite.Sprite):
    def __init__(self, x, y, file, a, b, *group):
        self.a = a
        self.b = b
        super().__init__(*group)
        self.image = file
        self.rect = self.image.get_rect(
            center=(x + CELL_SIZE / 2, y + CELL_SIZE / 2))
