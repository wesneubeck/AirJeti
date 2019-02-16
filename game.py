# TODO:
# key held down movement
# have random missles/gun_fire flow down the screen
# have contact with jet = death / game start over

import pygame
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

	class Attacker():
		def __init__(self):
			top = [450, 540]
			lpoint = [435, 575]
			rpoint = [465, 575]
			pygame.draw.polygon(display, player_green, [top, lpoint, rpoint], 3)

		def east_to_west():
			"""
			move east when n is pressed
				top = top[0]-5
				lpoint = lpoint[0]+-5
				rpoint = rpoint[0]+-5
			move west when v is pressed

			"""
			pass

	running = True
	while running:
		clock.tick(60)
		display.blit(bg, (0,0))
		Attacker()

		for event in pygame.event.get():
			keys = pygame.key.get_pressed()
			if event.type == pygame.QUIT:
				running = False

			if keys[pygame.K_v]:
				print("going left") #test
				pass
				#triangle left move	
			if keys[pygame.K_n]:
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


