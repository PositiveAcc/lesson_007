# -*- coding: utf-8 -*-
from random import randint

import simple_draw as sd

FLAKE_LENGTH = 15

sd.resolution = (800, 600)


# Шаг 1: Реализовать падение снежинки через класс. Внести в методы:
#  - создание снежинки с нужными параметрами
#  - отработку изменений координат
#  - отрисовку


class Snowflake:
    def __init__(self, x, y, length):
        if x is None:
            self.x = randint(length, sd.resolution[0])
        else:
            self.x = x
        self.y = y
        self.length = length

    def draw(self):
        point = sd.get_point(self.x, self.y)
        sd.snowflake(center=point, length=self.length)
        sd.finish_drawing()

    def can_fall(self):
        return self.y > self.length

    def move(self):
        if self.can_fall():
            self.x += randint(-1, 3)
            self.y -= randint(1, 9)

    def clear_previous_picture(self):
        if self.can_fall():
            sd.start_drawing()
            point = sd.get_point(self.x, self.y)
            sd.snowflake(center=point, length=self.length, color=sd.background_color)

# flake = Snowflake(None, y=sd.resolution[1]+15, length=15)
#
# while True:
#     flake.clear_previous_picture()
#     flake.move()
#     flake.draw()
#     if not flake.can_fall():
#         break
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


def get_flakes(count):
    result = []
    for i in range(count):
        result.append(Snowflake(None, y=sd.resolution[1]+FLAKE_LENGTH, length=FLAKE_LENGTH))
    return result


def get_fallen_flakes(flakes):
    count = 0
    for flake in flakes:
        if not flake.can_fall():
            count += 1
    return count

def append_flakes(count):
    flakes.extend(get_flakes(count))

# шаг 2: создать снегопад - список объектов Снежинка в отдельном списке, обработку примерно так:
flakes = get_flakes(count=1)  # создать список снежинок
while True:
    for flake in flakes:
        flake.clear_previous_picture()
        flake.move()
        flake.draw()
    fallen_flakes = get_fallen_flakes(flakes=flakes)  # подчитать сколько снежинок уже упало
    if fallen_flakes:
        append_flakes(count=fallen_flakes)  # добавить еще сверху
    sd.sleep(0.1)
    if sd.user_want_exit():
        break

sd.pause()
