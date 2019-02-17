#!/usr/bin/env python3


import pygame
from pygame.locals import *
import sys
#import random



def main():
	pygame.init()
	W = 900
	H = 600
	size = (W, H)
	player_green = (0, 255, 0)
	display = pygame.display.set_mode(size)
	bg = pygame.image.load("background.jpg")
	bg = pygame.transform.scale(bg, size)
	pygame.display.set_caption('Aviators')
	clock = pygame.time.Clock()


	class Attacker:
		def __init__(self):
			pygame.init()
			self.top = [450, 540] # keep y postion constant
			self.lpoint = [435, 575]
			self.rpoint = [465, 575]
			self.position = pygame.draw.polygon(display, player_green, [self.top, self.lpoint, self.rpoint], 3)

		def move_left(self):
			# when v pressed move west
				print("going left") #test
				#triangle left move	
				self.top = [(self.top[0]-5), 540]
				self.lpoint = [(self.lpoint[0]-5), 575]
				self.rpoint = [(self.rpoint[0]-5), 575]
				display.fill(bg, (0,0))

		def move_right(self):
			# when n pressed move east
				print("going right")
				self.top = [(self.top[0]+5), 540]
				self.lpoint = [(self.lpoint[0]+5), 575]
				self.rpoint = [(self.rpoint[0]+5), 575]
				display.fill(bg, (0,0))
		
			# when SPACE pressed fire
		def fire(self):
			if keys[pygame.K_SPACE]:
				print("fire")

	running = True
	while running:
		clock.tick(60)
		display.blit(bg, (0,0))
		Attacker()

		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
				sys.exit()

		keys = pygame.key.get_pressed()
		if keys[pygame.K_v]:
			pygame.display.update(Attacker(move_left()))
			print("going left") #test
			pass
			#triangle left move	
			
		if keys[pygame.K_n]:
			pygame.display.update(Attacker(move_right()))
			print("going right")
			pass
			#triangle right move	
	
		if keys[pygame.K_SPACE]:
			print("fire")
			pass
			#triangle right move	

		

		pygame.display.flip()
		pygame.display.update() 

pygame.quit()


if __name__ == "__main__":
	main()


