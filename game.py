#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *
#import random

# window
W = 900
H = 600
size = (W, H)
# player color - green
green = [0, 250, 0]

class Main:
	def __init__(self):
		pygame.init()
		self.clock = pygame.time.Clock()
		self.display = pygame.display.set_mode(size)
		pygame.display.set_caption('Aviators')
# background image
		self.bg = pygame.image.load("background.jpg")
		self.bg = pygame.transform.scale(self.bg, size)
		self.init_game()
	
	def init_game(self):
		self.attacker_top = [450, 555]
		self.attacker_left = [435, 580]
		self.attacker_right = [465, 580]
		self.attacker = pygame.draw.polygon(self.display, green, (self.attacker_top, self.attacker_left, self.attacker_right), 3)

	def check_input(self):
		keys = pygame.key.get_pressed()

		if keys[pygame.K_v]:
			#left move	
			self.attacker_top = [self.attacker_top[0]-5, 555]
			self.attacker_left = [self.attacker_left[0]-5, 580]
			self.attacker_right = [self.attacker_right[0]-5, 580]
		
		if keys[pygame.K_n]:
			#right move	
			self.attacker_top = [self.attacker_top[0]+5, 555]
			self.attacker_left = [self.attacker_left[0]+5, 580]
			self.attacker_right = [self.attacker_right[0]+5, 580]
	
		if keys[pygame.K_SPACE]:
			print("fire")
			#fire

	def run(self):
		running = True
		while running:
			self.clock.tick(60)
			self.display.blit(self.bg, (0,0))
			self.check_input()
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					sys.exit()

			pygame.draw.polygon(self.display, green, (self.attacker_top, self.attacker_left, self.attacker_right))
#([450, 555], [435, 580], [465, 580]), 3)
			pygame.display.flip()
			pygame.display.update()

if __name__ == "__main__":
	Main().run()


