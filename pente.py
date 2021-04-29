import pygame
import tkinter as tk
import squares as sq
import gameSetup as setup

BG_BLUE = (66, 218, 245)
BOARD_AREA_COLOR = (242, 215, 167)
BOARD_BORDER = (15, 15, 15)
SCORE_B_COLOR = (255, 255, 255)
SCORE_B_BORDER = (0, 0, 255)

root = tk.Tk()
S_WIDTH = root.winfo_screenwidth()
S_HEIGHT = root.winfo_screenheight() - 50
print("the screen size is: ", S_WIDTH, S_HEIGHT)

setup = setup.penteSetup(S_WIDTH, S_HEIGHT)
print(setup)

pygame.init()
screen = pygame.display.set_mode((setup.getFinalW(),setup.getFinalH()), pygame.RESIZABLE)
pygame.display.set_caption("Pynte")
game = True

def drawGameAreas():
	pygame.draw.rect(screen, BOARD_AREA_COLOR, setup.getBoardParams())
	drawGameSquares()
	pygame.draw.rect(screen, BOARD_BORDER, setup.getBoardParams(), 2)
	pygame.draw.rect(screen, SCORE_B_COLOR, setup.getScoreBParams())
	pygame.draw.rect(screen, SCORE_B_BORDER, setup.getScoreBParams(), 2)

#TODO add squares to array or something
def drawGameSquares():
	for i in range(19):
		for j in range(19):
			temp_square = sq.Square(int(i * (setup.getBoardSizeSide() / 19) + setup.getSpacerValue()), int(j * (setup.getBoardSizeSide() / 19) + setup.getSpacerValue()), int(setup.getBoardSizeSide() / 19))
			drawSquare(temp_square, screen)

def drawSquare(s, screen):
	squareParams = s.getDrawParams()
	squareX,squareY,squareW,squareH = squareParams
	squareColor = s.getBGColor()
	squareLC = s.getLineColor()
	pygame.draw.rect(screen, squareColor, squareParams)
	pygame.draw.line(screen, squareLC, (squareX + squareW / 2, squareY), (squareX + squareW / 2, squareY + squareH), 1)
	pygame.draw.line(screen, squareLC, (squareX, squareY + squareH / 2), (squareX + squareW, squareY + squareH / 2), 1)

while game:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			game = False
			print("peace", end=" ")
		if event.type == pygame.MOUSEBUTTONUP:
			pos = pygame.mouse.get_pos()
			print(pos)
		if event.type == pygame.VIDEORESIZE:
			w, h = pygame.display.get_surface().get_size()
			setup.updateSetup(w, h)
			screen = pygame.display.set_mode((setup.getFinalW(), setup.getFinalH()), pygame.RESIZABLE)
	screen.fill(BG_BLUE)
	drawGameAreas()
	pygame.display.flip()
print("out!")
pygame.quit()