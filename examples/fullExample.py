#
# PygamePal, by Rik Cross
#  -- homepage: github.com/rik-cross/pygamepal
#  -- MIT licenced, free to use, modify and distribute
#  -- run 'pip install pygamepal' to use
#
# Instructions
#  -- WASD to move player
#  -- Enter to move to game scene
#  -- Esc to move to menu scene
# 
# Image credit - Cup Nooble
#  --  cupnooble.itch.io/sprout-lands-asset-pack
#

import pygame
import pygamepal
import os

#
# create sprite subclasses
#


class Player(pygamepal.Sprite):

    def init(self):
        
        #
        # player textures from spritesheet
        #

        # load a texture
        playerSpritesheet = pygame.image.load(os.path.join('images','character_spritesheet.png'))
        # split texture into a 2D list of sub-textures
        splitTextures = pygamepal.splitTexture(playerSpritesheet, 48, 48)
        
        #
        # create a player
        #

        self.size = (14, 16)
        self.position = (126 - 7, 128 - 8)
        self.collider = pygamepal.Collider(offset = (2, 12), size = (10, 4))

        self.spriteImage = pygamepal.SpriteImage()
        # states and images
        self.spriteImage.addTextures(
            splitTextures[0][0], splitTextures[0][1],
            state = 'idle',
            offset=(17, 16)
        )
        self.spriteImage.addTextures(
            splitTextures[1][1], splitTextures[1][2], splitTextures[1][1], splitTextures[1][3],
            state = 'up',
            animationDelay = 4,
            offset=(17, 16)
        )
        self.spriteImage.addTextures(
            splitTextures[0][1], splitTextures[0][2], splitTextures[0][1], splitTextures[0][3],
            state = 'down',
            animationDelay = 4,
            offset=(17, 16)
        )
        self.spriteImage.addTextures(
            splitTextures[2][1], splitTextures[2][2], splitTextures[2][1], splitTextures[2][3],
            state = 'left',
            animationDelay = 4,
            offset=(17, 16)
        )
        self.spriteImage.addTextures(
            splitTextures[3][1], splitTextures[3][2], splitTextures[3][1], splitTextures[3][3],
            state = 'right',
            animationDelay = 4,
            offset=(17, 16)
        )
        self.trigger = pygamepal.Trigger(ox = -5, oy = -5, w = 24, h = 26, sprite = self)
    
    def update(self):

        # WASD to move and change state
        if gameExample.input.isKeyDown(pygame.K_w):
            self.y -= 1
            self.spriteImage.setState('up')
        elif gameExample.input.isKeyDown(pygame.K_a):
            self.x -= 1
            self.spriteImage.setState('left')
        elif gameExample.input.isKeyDown(pygame.K_s):
            self.y += 1
            self.spriteImage.setState('down')
        elif gameExample.input.isKeyDown(pygame.K_d):
            self.x += 1
            self.spriteImage.setState('right')
        else:
            self.spriteImage.setState('idle')


#
# create scene subclasses
#

class MenuScene(pygamepal.Scene):
    
    def update(self):

        if self.game.input.isKeyPressed(pygame.K_RETURN):
            self.game.currentScene = gameScene
    
    def draw(self):

        pygamepal.drawText(self.overlaySurface, '[RETURN] to play, [Q] to quit', (20, 20), backgroundColor='black')

class GameScene(pygamepal.Scene):
    
    def zoomCamera(self, this, other, zoom):
        self.camera.zoom = zoom
    
    def setChestState(self, this, other, state):
        self.chest.spriteImage.setState(state)

    def init(self):
        
        #
        # add textures
        #

        self.map = pygame.image.load(os.path.join('images', 'map.png'))

        #
        # add sprites
        #

        # player

        self.player = Player()
        self.addSprite(self.player)

        # trees

        self.addSprite(
            pygamepal.Sprite(
                imageName = os.path.join('images', 'tree.png'),
                position = (40, 50),
                collider = pygamepal.Collider(offset = (6, 25), size = (12, 5))
            )
        )
        self.addSprite(
            pygamepal.Sprite(
                imageName = os.path.join('images', 'tree.png'),
                position = (70, 40),
                collider = pygamepal.Collider(offset = (6, 25), size = (12, 5))
            )
        )
        self.addSprite(
            pygamepal.Sprite(
                imageName = os.path.join('images', 'tree.png'),
                position = (20, 10),
                collider = pygamepal.Collider(offset = (6, 25), size = (12, 5))
            )
        )

        # chest

        # load a texture
        chestSpritesheet = pygame.image.load(os.path.join('images','chest_spritesheet.png'))
        # split texture into a 2D list of sub-textures
        splitTextures = pygamepal.splitTexture(chestSpritesheet, 48, 48)
        
        self.chest = pygamepal.Sprite(position = (175, 175), size = (16, 14))
        self.chest.collider = pygamepal.Collider(offset = (0, 8), size = (16, 6))
        self.chest.spriteImage = pygamepal.SpriteImage()
        self.chest.spriteImage.addTextures(splitTextures[0][0], offset = (16, 18), state = 'idle')
        self.chest.spriteImage.addTextures(splitTextures[0][0], splitTextures[0][1], splitTextures[0][2], splitTextures[0][3], offset = (16, 18), state = 'open', animationDelay = 4, loop = False)
        self.chest.spriteImage.addTextures(splitTextures[0][3], splitTextures[0][2], splitTextures[0][1], splitTextures[0][0], offset = (16, 18), state = 'close', animationDelay = 4, loop = False)
        self.chest.trigger = pygamepal.Trigger(ox = -5, oy = -5, w = 26, h = 24, sprite = self.chest,
            onEnter = lambda this, other, state='open': self.setChestState(this, other, state),
            onExit = lambda this, other, state='close': self.setChestState(this, other, state))
        self.addSprite(self.chest)

        #
        # customise the scene
        #

        self.backgroundColor = 'black'
        self.sortKey = self.sortByBottom

        #
        # customise the scene camera
        #
        
        self.camera.backgroundColor = 'black'
        self.camera.target = self.player.getCenter()
        self.camera.lazyFollow = 0.9
        self.camera.zoom = 4
        self.camera.lazyZoom = 0.9
        self.camera.clamp = True
        self.camera.clampRect = (0, 0, 256, 256)
        
        #
        # add triggers for the camera
        #

        self.forestTrigger = pygamepal.Trigger(10, 20, 100, 70,
            onEnter = lambda this, other, zoom = 6 : self.zoomCamera(this, other, zoom),
            onExit = lambda this, other, zoom = 4 : self.zoomCamera(this, other, zoom))

    def update(self):

        # [ESC] to return to menu scene
        if self.game.input.isKeyPressed(pygame.K_ESCAPE):
            self.game.currentScene = menuScene
        
        # update triggers
        self.forestTrigger.update()

        # camera tracks the player
        self.camera.target = self.player.getCenter()

    def draw(self):

        self.sceneSurface.blit(self.map, (0, 0))
        if pygamepal.Game.DEBUG:
            self.forestTrigger.draw(self.sceneSurface)
        pygamepal.drawText(self.overlaySurface, '[WASD] to move, [ESC] to return to main menu, [Q] to quit', (20, 20), backgroundColor='black')

#
# create game subclass
#

class GameExample(pygamepal.Game):

    def update(self):

        # press [q] qt any time to quit
        if self.input.isKeyPressed(pygame.K_q):
            self.quit()

#
# create game and scenes
#

# uncomment the line below to show debug info
#pygamepal.Game.DEBUG = True
gameExample = GameExample(size=(800, 600), caption = 'Full game example')
menuScene = MenuScene(gameExample)
gameScene = GameScene(gameExample)

#
# set up game and run
#

gameExample.currentScene = menuScene
gameExample.run()