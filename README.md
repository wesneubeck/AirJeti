# AirJeti, day = 6, *My 100 day challenge* 

### what I've completed
	-	attacker repeat when reachs bottom
	-  added rocks/speed
### what I'm working on
	-  rocks repeat at random y value btw 1, 200/ only goes 2 times through/ WHY???

## game states:
	new game = start of game
		init game = starts when RETURN is pressed 
	running = while loop
	game over = when lives = 0
		screen goes white, says "Game Over" in red
	level complete = all of enemy killed

## elements:
	- player
		green 
	- attacker
		purple
	- rocks
		grey
	- bullets	
		player color
		attacker color 

## movement:
	player = east to west
	enemey = random x.axis, north to south
	bullet = [[player: position facing, south to north], 
				[attacker: position facing, north to south]]

## create scoreboard
#### keep track of:
	- attacker_count = 20
	- score_count = # of attacker killed 
		if	pygame.sprite.collide_rect(player bullet, attacker): #boolen
			score_count +=1	
			attacker_count -=1

	- time = 1 min clock, countdown

	- health = number of times attacker hits player with bullets or rocks
		if	pygame.sprite.collide_rect(attacker bullet, player):
			health -=1
		if	pygame.sprite.collide_rect(rocks, player):
			health -=1
			if health < 1:
				game state = new game
		
	- lives = starts with 3, lives-1 when health reaches 0 in game
	


