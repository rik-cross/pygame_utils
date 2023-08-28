#
# pygamewrapper, by Rik Cross
#  -- homepage: github.com/rik-cross/pygamewrapper
#  -- MIT licenced, free to use, modify and distribute
#  -- run 'pip install pygamewrapper' to use
#
# Image credit - Cup Nooble
#  --  cupnooble.itch.io/sprout-lands-asset-pack
#

import pygame
import pygamewrapper
import os

#
# create a new game
#

class MyGame(pygamewrapper.Game):

    def init(self):
        # this code is optional and can be removed or replaced
        self.size = (640, 480)
        self.caption = 'Example Game'
        self.icon = pygame.image.load(os.path.join('images', 'character.png'))
        self.blue = 0

    def update(self):
        # this code is optional and can be removed or replaced
        # cycle a value between 0 and 255
        self.blue = (self.blue + 1) % 255

    def draw(self):
        # this code is optional and can be removed or replaced
        self.screen.fill('cornflowerblue')
        pygamewrapper.drawText(self.screen, 'pygamewrapper example game!', 25, 25, colour=(0, 0, self.blue))
        pygamewrapper.drawText(self.screen, 'Add code to init(), update() and draw() methods.', 25, 50)

#
# create a new game instance
#

myGame = MyGame()
myGame.run()