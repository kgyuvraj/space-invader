# import pygame, sys, random
#
#
# class Mygame():
#     def main(self):
#         # initial speed
#         Xspeed = 10
#         Yspeed = 10
#         livesinit = 5
#
#         paddlespeed = 30
#         points = 0
#         bgcolor = 0, 0, 0  # black
#         size = width, height = 500, 500
#
#         #initializing the pygame engine
#         pygame.init()
#         screen = pygame.display.set_mode(size)
#
#         #creating game objects
#         paddle = pygame.image.load('board.png')
#         paddlerect = paddle.get_rect()
#
#         paddle = pygame.image.load('ball.png')
#         paddlerect = paddle.get_rect()
#
#         sound = pygame.mixer.sound('laser.wav')
#         sound.set_volume(10)
#
#         bg = pygame.image.load('bg.jpg')
