# faça um programa em python que abra e execute um arquivo.mp3
import pygame

pygame.init()

pygame.mixer.music.load('Desafio-021.mp3')
pygame.mixer.music.play()
pygame.event.wait()

