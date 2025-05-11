import random
import pygame
import cv2
import os 
from pygame.locals import *
import pygetwindow as gw

def play(filename):
    pygame.mixer.music.load("wav/" + filename)
    pygame.mixer.music.play()

pygame.init()
pygame.mixer.init()

where_options = ["w szafie", "w lodowce", "w piekarniku", "w kiblu"]    
where_message = "gdzie jest kurwa koko?\n Wybierz opcje:\n1 - za szafa\n2 - w lodowce\n3 - w piekarniku\n4 - w kiblu\n"

play("Koko.wav")
choice = input(where_message)
random_koko = random.randint(1,4)

while choice != str(random_koko):
    print("przejebales cwelu! Jeszcze raz")
    play("Koko.wav")
    choice = input(where_message)
    random_koko = random.randint(1,4)
    
print("Brawo, zgadłeś! Koko jest w ", where_options[random_koko-1])


filename = "img/" + str(random_koko) + ".png"
im = cv2.imread(filename)
height, width, channel = im.shape
screen = pygame.display.set_mode((width, height))

pygame.display.set_caption("Koko")
win = gw.getWindowsWithTitle("Koko")[0]
x, y  = 100, 100
win.moveTo(x, y)

image = pygame.image.load(filename)
screen.blit(image, (0, 0))

running = True
while running:
    pygame.event.pump()  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    pygame.display.flip()
    pygame.time.delay(10)
pygame.quit()