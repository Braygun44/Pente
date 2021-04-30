import pygame
import tkinter as tk
import squares as sq
import gameSetup as setup

background_color = (66, 218, 245)
game_board_background_color = (242, 215, 167)
game_board_border_color = (15, 15, 15)
scoreboard_background_color = (255, 255, 255)
scoreboard_border_color = (0, 0, 255)

root = tk.Tk()
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight() - 50
print("the screen size is: ", screen_width, screen_height)

setup = setup.penteSetup(screen_width, screen_height)
print(setup)

pygame.init()
screen = pygame.display.set_mode((setup.getFinalW(),setup.getFinalH()), pygame.RESIZABLE)
pygame.display.set_caption("Pynte")
game = True

def drawGameAreas():
	pygame.draw.rect(screen, game_board_background_color, setup.getBoardParams())
	drawGameSquares()
	pygame.draw.rect(screen, game_board_border_color, setup.getBoardParams(), 2)
	pygame.draw.rect(screen, scoreboard_background_color, setup.getScoreBParams())
	pygame.draw.rect(screen, scoreboard_border_color, setup.getScoreBParams(), 2)

def drawGameSquares():
	global squares_array
	squares_array = []
	for i in range(19):
		for j in range(19):
			temp_square = sq.Square(int(i * (setup.getBoardSizeSide() / 19) + setup.getSpacerValue()), int(j * (setup.getBoardSizeSide() / 19) + setup.getSpacerValue()), int(setup.getBoardSizeSide() / 19))
			temp_square.setPos(i, j)
			squares_array.append(temp_square)
			drawSquare(temp_square, screen)

def drawSquare(s, screen):
	squareParams = s.getDrawParams()
	square_x,square_y,square_w,square_h = squareParams
	square_color = s.getBGColor()
	square_lc = s.getLineColor()
	pygame.draw.rect(screen, square_color, squareParams)
	pygame.draw.line(screen, square_lc, (square_x + square_w / 2, square_y), (square_x + square_w / 2, square_y + square_h), 1)
	pygame.draw.line(screen, square_lc, (square_x, square_y + square_h / 2), (square_x + square_w, square_y + square_h / 2), 1)

while game:
	screen.fill(background_color)
	drawGameAreas()
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = False
			print("peace", end=" ")
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			print(pos)
			for squ in squares_array:
				if squ.isInside(pos):
					print(squ.getPos())
		if event.type == pygame.VIDEORESIZE:
			w,h = pygame.display.get_surface().get_size()
			setup.updateSetup(w, h)
			screen = pygame.display.set_mode((setup.getFinalW(), setup.getFinalH()), pygame.RESIZABLE)

	pygame.display.flip()
print("out!")
pygame.quit()