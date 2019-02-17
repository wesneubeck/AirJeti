AirJeti, day = 3, *My 100 day challenge* 

*
It took me this fucking long to create this simple framework for the game.
No experience at all.  Good or Bad?
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
	fires 3 bullets in the direction 'player' pointing

reload() = return count
	wait 3 seconds to fire again
	killed() = bullets fired hit enemy

movement()
	

