#!/usr/bin/env python3

import sys
import pygame
import random
from pygame.locals import *

# window colors variables
W = 900
H = 600
#screen size
size = (W, H)
# player/bullet color - green
# attacker/bullet color - purple
green = [0, 250, 0]
purple = [186, 85, 211]
grey = [134, 136, 138]


class Attacker(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()
		self.image = pygame.Surface([30, 30])
		self.image.fill(color)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y += 4
		# when attacker reaches the bottom, repeat back to top
		if self.rect.y == 600:
			self.rect.y = 0


class Rocks(pygame.sprite.Sprite):
	def __init__(self, color):
		super().__init__()
		self.x = random.randint(15, 65)
		self.y = random.randint(15, 65)
		self.image = pygame.Surface([self.x, self.y])
		self.image.fill(color)
		self.rect = self.image.get_rect()
	def update(self):
		self.rect.y += 6
		# when rock reaches the bottom, repeat back to random spot btw 0, 200
		if self.rect.y == 600:
			self.rect.y = random.randint(1, 200)
				

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
		  self.rect.y -= 20

all_sprites_list = pygame.sprite.Group()
bullet_list = pygame.sprite.Group()
attacker_list = pygame.sprite.Group()
rocks_list = pygame.sprite.Group()

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

# loop for attackers 
		for attacker in range(4):
			attacker = Attacker(purple)
			attacker.rect.x = random.randint(0,900)
			all_sprites_list.add(attacker)
			attacker_list.add(attacker)						
#			all_sprites_list.update()
		
		for rocks in range(8):
			rocks = Rocks(grey)
			rocks.rect.x = random.randint(0,900)
			all_sprites_list.add(rocks)
			rocks_list.add(rocks)						
#			all_sprites_list.update()
		
	
	def check_input(self):
		keys = pygame.key.get_pressed()
		if keys[pygame.K_f]:
			#left move	
			self.player_top = [self.player_top[0]-15, 555]
			self.player_left = [self.player_left[0]-15, 580]
			self.player_right = [self.player_right[0]-15, 580]
		
		if keys[pygame.K_j]:
			#right move	
			self.player_top = [self.player_top[0]+15, 555]
			self.player_left = [self.player_left[0]+15, 580]
			self.player_right = [self.player_right[0]+15, 580]
	
		if keys[pygame.K_l]:
			print('working')

		if keys[pygame.K_s]:
			print('working')


	def run(self):
		running = True
		while running:
			self.display.blit(self.bg, (0,0))
			self.clock = pygame.time.Clock()
			self.check_input()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					running = False
					sys.exit()
				elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
					self.player_bullet = Bullet()
					self.player_bullet.rect.x = self.player_top[0]
					self.player_bullet.rect.y = self.player_top[1]
					all_sprites_list.add(self.player_bullet)
					bullet_list.add(self.player_bullet)

			all_sprites_list.update()
			all_sprites_list.draw(self.display)
			pygame.draw.polygon(self.display, green, (self.player_top, self.player_left, self.player_right))
			pygame.display.flip()
			pygame.display.update()
			self.clock.tick(40)

if __name__ == "__main__":
	Main().run()


