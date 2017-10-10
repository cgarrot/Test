import pygame
from pygame.locals import *
from random import randint

NX = 16
NY = 16

SIZE = 32

WIDTH = NX * SIZE
HEIGHT = NY * SIZE

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREY = (128, 128, 128)
RED = (128, 0, 0)
GREEN = (0, 128, 0)

DOWN = (0, +1)
UP = (0, -1)
LEFT = (-1, 0)
RIGHT = (+1, 0)

FPS_CAP = 10

def main():
	pygame.init()
	screen = pygame.display.set_mode((WIDTH, HEIGHT))
	clock = pygame.time.Clock()
	mainloop(screen, clock)

def mainloop(screen, clock):
	global orientation, over
	running = True
	reset()
	while running:
		clock.tick(FPS_CAP)
		for event in pygame.event.get():
			if event.type == QUIT:
				running = False
			if event.type == KEYDOWN:
				if event.key == K_r:
					reset()
				if event.key == K_UP:
					if orientation != DOWN:
						orientation = UP
				if event.key == K_DOWN:
					if orientation != UP:
						orientation = DOWN
				if event.key == K_LEFT:
					if orientation != RIGHT:
						orientation = LEFT
				if event.key == K_RIGHT:
					if orientation != LEFT:
						orientation = RIGHT
		if not over:
			uptade()
		render(screen)
		pygame.display.update()
	pygame.quit()

def uptade():
	global bonus, snake_size, snake_parts, orientation, over, score
	x, y = snake_parts[-1]
	x += orientation[0]
	y += orientation[1]
	new_part = (x,y)	
	if new_part in snake_parts:
		over = True
	if not 0 <= x < NX:
		over = True
	if not 0 <= y < NY:
		over = True
	if new_part == bonus:
		snake_size += 1
		score += 1
		new_bonus()
	if over:
		print('GAME OVER !')
		print('Your score is : ', score)
		print('Press R to restart !')
	snake_parts.append(new_part)
	if not over:
		if len(snake_parts) > snake_size:
			del snake_parts[0]

def render(screen):
	global bonus, snake_parts
	screen.fill(GREY)
	draw_cell(screen, bonus, RED)
	for part in snake_parts:
		draw_cell(screen, part, GREEN)

def draw_cell(screen, cell, color):
	pygame.draw.rect(screen, color, (cell[0] * SIZE, cell[1] * SIZE, SIZE, SIZE))

def new_bonus():
	global bonus
	x = randint(0, NX - 1)
	y = randint(0, NY - 1)
	bonus = (x, y)
	print('new bonus at:', bonus)

def reset():
	global snake_parts, snake_size, orientation, over, score
	new_bonus()
	snake_parts = [(0, 0)]
	score = 0
	snake_size = 1
	orientation = DOWN
	over = False

if __name__ == '__main__':
	main()