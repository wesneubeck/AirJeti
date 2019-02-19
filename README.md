AirJeti, day = 4, *My 100 day challenge* 

*
built the bullet and firing functions
working on: enemy/attacker
	moves down the screen, firing every 5 seconds
	random position on the screen 
	4 attackers each screen
		one killed, one appears on the top
		one reaches y = 0, one appears on the top 
*



1 main class
background = constant 

attacker()
	triangle
	moves left to right on x axis
		speed
	facing() = rotate range(160degrees), shooting left to right
	green

enemy()
	rotating squares	
	moves up to down on y axis at constant speed
		speed = random.value(set_range) 
	rotation, shooting left to right- range(45degrees)
	purple

rocks()
	circles(astroid)
	moves north to south
		speed = random.value(set_range)
	no shooting
	rocks.size = random.value(boundry) #so it can't be too big
	grey

score() = number of enemy killed

check input from keyboard
fire() = spacebar
	bullets = dots(green)
	**fires in the direction 'player' pointing

reload() = return count
	wait 3 seconds to fire again
	killed() = bullets fired hit enemy

movement()
	

