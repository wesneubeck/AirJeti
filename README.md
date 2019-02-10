 AirJeti
day = 0
*My 100 day challenge*
first pygame repo
learning as I go

*
Completed // basic set up
Next // create player class, move player East / West
*


set up the game:  
	background = constant (

	images will be simple
		triangle for 'player'
			green with purple fill
		triangle for 'enemy'
			red with black fill
		circles for rocks
			black with dark grey fill

		'player' stays on y axis - moves East / West with keydown 
		EAST = right = n
		WEST = left = v
		fire() = spacebar
		reload()

		'enemy' stays on random(x.axis), falls() on y.axis
		fire() = random.y.axis
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

