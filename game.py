#!/usr/bin/env python3

import sys
import pygame
from pygame.locals import *
#import random

# window
W = 900
H = 600
size = (W, H)
# player/bullet color - green
green = [0, 250, 0]
bullet_w = 2
bullet_h = 12

"""
class Attacker(pygame.sprite.Sprite):
	def __init__(self):
"""		



class Bullet(pygame.sprite.Sprite):
	 """ This class represents the bullet . """
	 def __init__(self):
		  # Call the parent class (Sprite) constructor
		  super().__init__()
		  self.image = pygame.Surface([4, 10])
		  self.image.fill(green)
		  self.rect = self.image.get_rect()

	 def update(self):
		  """ Move the bullet. """
		  self.rect.y -= 8

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()

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
		self.player_top = [450, 555]
		self.player_left = [435, 580]
		self.player_right = [465, 580]
		self.player = pygame.draw.polygon(self.display, green, (self.player_top, self.player_left, self.player_right), 3)


	def check_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_f]:
			#left move	
			self.player_top = [self.player_top[0]-5, 555]
			self.player_left = [self.player_left[0]-5, 580]
			self.player_right = [self.player_right[0]-5, 580]
		
		if keys[pygame.K_j]:
			#right move	
			self.player_top = [self.player_top[0]+5, 555]
			self.player_left = [self.player_left[0]+5, 580]
			self.player_right = [self.player_right[0]+5, 580]
	
		if keys[pygame.K_l]:
			print('working')

		if keys[pygame.K_s]:
			print('working')


	def run(self):
		running = True
		while running:
			self.display.blit(self.bg, (0,0))
			self.check_input()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					sys.exit()

				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.bullet = Bullet()
					self.bullet.rect.x = self.player_top[0]
					self.bullet.rect.y = self.player_top[1]
					all_sprites_list.add(self.bullet)
					bullet_list.add(self.bullet)

			all_sprites_list.update()
			all_sprites_list.draw(self.display)
			pygame.draw.polygon(self.display, green, (self.player_top, self.player_left, self.player_right))
			pygame.display.flip()
			pygame.display.update()
			self.clock.tick(80)

if __name__ == "__main__":
	Main().run()


