import pygame

# create a default 'system' font
pygame.font.init()
sysFont = pygame.font.SysFont(None, 24)

def drawText(screen, text,
             position = [0, 0],
             font = None,
             antialias = True,
             color = 'white', background = None,
             centerX = False, centerY = False):
    
    # use the default 'system' font if none specified
    if font is None:
        font = sysFont

    # create text surface
    textSurface = font.render(text, antialias, color, background)

    # center
    if centerX == True:
        position = (position[0] - textSurface.get_rect().width // 2, position[1])
    if centerY == True:
        position = (position[0], position[1] - textSurface.get_rect().height // 2)

    # draw text to screen
    screen.blit(textSurface, position)