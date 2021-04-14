import pygame
from squares import Square as s

s_width,s_height = 960,540

screen = pygame.display.set_mode((s_width,s_height))

game = True

s.__init__(s,100,100,100)
squareX,squareY,squareW,squareH = s.getDrawParams(s)
squareParams = squareX,squareY,squareW,squareH
squareColor = s.getBGColor(s)
squareLC = s.getLineColor(s)

pygame.draw.rect(screen, squareColor, squareParams)
pygame.display.flip()

while game:
# 	screen.fill('forestgreen')
# 	screen.fill('dimgrey',((s_width/4,0),(s_width/2,s_height)))
	 	pygame.display.flip()