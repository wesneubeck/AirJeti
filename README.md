AirJeti
day = 1
*My 100 day challenge*
first pygame repo
learning as I go

*
Completed // further basic set up // player n(right) v(left) button working
Next // set up movement of attacker east and west
*


set up the game:  
background = constant 
images will be simple

	attacker()
		triangle
		moves east to west
		facing() = rotate range(160degrees):
		shooting left to right = facing()
		green
	enemy()
		rotating squares	
		moves north to south
		shooting left to right- range(45degrees)
		purple
	rocks()
		circles(astroid)
		moves north to south
		no shooting
		grey

	fire() = spacebar
	reload() = return

Actions:
	north to south = random(x.axis), falls() on y.axis
	east to west = 
		east = keys[n]
		west = keys[v]
	fire() = 
		direction = where attacker.facing()
	fire() towards 'player'

	'rocks' falls() from random.x down y.axis
	rocks.size = random.value(boundry) #so it can't be too big


functions

	fire():
	bullets = dots(green)
	fires 3 bullets in the direction 'player' pointing

	reload():
	wait 3 seconds to fire again
	
	falls() = y.axis(0 --> 600)
	falls.speed = random.value(boundry)

