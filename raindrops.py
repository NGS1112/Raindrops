"""
File: raindrops.py
Name: Nicholas Shinn
Description: Generates randomly placed raindrops within a pond, calculates the circumference of all drops and circles, returns value
"""
import turtle as t
import random as ran


def main():
	"""
	Description: Calls for input to be used as n, initializes the pond, and draws the raindrops as well as calculating the total circumference before closing the program
	"""
	n = int(input('Raindrops (1-100): '))
	raindropNumber(n)
	initialization()
	raindrops(n,ran.randint(1,15),0,0)
	t.done()

def initialization():
	"""
	Description: Draws the pond where the raindrops will be contained
	Pre-conditions: Turtle facing east, pen down
	Post-conditions: Turtle facing North, pen up
	"""
	t.speed(0)
	t.up()
	t.forward(275)
	t.left(90)
	t.down()
	t.fillcolor(0, 0.4, 0.73)
	t.begin_fill()
	t.forward(275)
	t.left(90)
	t.forward(550)
	t.left(90)
	t.forward(550)
	t.left(90)
	t.forward(550)
	t.left(90)
	t.forward(275)
	t.end_fill()
	t.up()
	t.home()
	t.left(90)

def raindrop(r):
	"""
	Description: Draws the raindrops in random locations within the pond using a random fill color for each, calls the ripples function
	:param r: Radius
	"""
	t.setpos(ran.randint(-185, 185), ran.randint(-185, 185))
	t.fillcolor(ran.random(), ran.random(), ran.random())
	t.backward(r)
	t.right(90)
	t.down()
	t.begin_fill()
	t.circle(r)
	t.end_fill()
	t.up()
	t.left(90)
	t.forward(r)
	ripples(N_RIPPLES(), r, 0, 0)

def MAX_RAINDROPS():
	"""
	Description: Sets the maximum number of raindrops
	"""
	return 100

def MINIMUM_RAINDROPS():
	"""
	Description: Sets the minimum number of raindrops
	"""
	return 1

def raindropNumber(n):
	"""
	Description: Validates that the provided number of raindrops fits within the maximum and minimum values allowed before returning the value as n
	:param n: Number of raindrops
	"""
	if n>MAX_RAINDROPS():
		print ('Number out of range')
	elif n<MINIMUM_RAINDROPS():
		print ('Number out of range')
	else:
		return n

def N_RIPPLES():
	"""
	Description: Sets the number of ripples per drop at 5
	"""
	return 5


def ripples(m, r, a, b):
	"""
	Description: Draws 5 ripples per raindrop, accumulating the circumference values per circle
	:param m: Iterations of ripples
	:param r: radius
	:param a: radius of last circle drawn
	:param b: total circumference
	"""
	if m == 0:
		return b
	else:
		y = a+r
		t.backward(y+r)
		t.right(90)
		t.down()
		t.circle(y+r)
		t.up()
		t.left(90)
		t.forward(y+r)
		ripples(m-1, r, a+r, b+2*3.14*r)

def raindrops(n, r, x, b):
	"""
	Description: Draws all the raindrops within the pond before returning the total circumference and prompting the user to close the window
	:param n: Iterations of raindrops
	:param r: Radius
	:param x: Running total of circumference
	:param b: Circumference of ripples
	"""
	if n == 0:
		print ('The total circumference of all ripples is '+str(x)+' units.')
		print ('Close the window to quit.')
	else:
		raindrop(ran.randint(1, 15))
		y = 2*3.14*r
		raindrops(n-1, ran.randint(1, 15), x+y+b, b)

main()
