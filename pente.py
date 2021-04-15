import pygame
import tkinter as tk
import squares as sq
import gameSetup as setup

root = tk.Tk()
S_WIDTH = root.winfo_screenwidth()
S_HEIGHT = root.winfo_screenheight() - 50
print("the screen size is: ", S_WIDTH, S_HEIGHT)

setup = setup.penteSetup(S_WIDTH, S_HEIGHT)
print(setup)

pygame.init()
screen = pygame.display.set_mode((S_WIDTH,S_HEIGHT))
pygame.display.set_caption("Let's Play Pente!!!!")
game = True

firstSquare = sq.Square(100, 100, 100)

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
			print("peace")
	drawSquare(firstSquare, screen)
	pygame.display.flip()
print("out!")
pygame.quit()