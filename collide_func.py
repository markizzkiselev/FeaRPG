from config import *


def collide(mob, player=None, w=0, h=0):
    if not player:
        if mob.rect.right + w > DIMENSIONS[0] / 2 - CELL_SIZE / 2 and \
                mob.rect.left + w < DIMENSIONS[0] / 2 + CELL_SIZE / 2 and \
                mob.rect.bottom + h > DIMENSIONS[1] / 2 - CELL_SIZE / 2 and \
                mob.rect.top + h < DIMENSIONS[1] / 2 + CELL_SIZE / 2:
            return True
        return False
    if mob.rect.right + w > player.rect.left and \
            mob.rect.left + w < player.rect.right and \
            mob.rect.bottom + h > player.rect.top and \
            mob.rect.top + h < player.rect.bottom:
        return True
    return False


def collide_1(mob, player=None, w=0, h=0):
    if not player:
        if mob.rect.right + w >= DIMENSIONS[0] / 2 - CELL_SIZE / 2 and \
                mob.rect.left + w <= DIMENSIONS[0] / 2 + CELL_SIZE / 2 and \
                mob.rect.bottom + h >= DIMENSIONS[1] / 2 - CELL_SIZE / 2 and \
                mob.rect.top + h <= DIMENSIONS[1] / 2 + CELL_SIZE / 2:
            return True
        return False
    if mob.rect.right + w >= player.rect.left and \
            mob.rect.left + w <= player.rect.right and \
            mob.rect.bottom + h >= player.rect.top and \
            mob.rect.top + h <= player.rect.bottom:
        return True
    return False
