import pygame

class TileMap():
    def __init__(self, tilesize, x, y):
        pygame.init()
        self.tilesize = tilesize
        self.images = []
        self.x = x
        self.y = y
        self.name = 'map'
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/border_3.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/floor_2.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/border_1.png"), (self.tilesize, self.tilesize)))
        self.images.append(pygame.transform.scale(pygame.image.load("C:/Users/Admin/OneDrive/Documents/pygame_project/characters/objects/wall_1.png"), (self.tilesize, self.tilesize)))
        self.array = [[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,0,0],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,0,0],
[1,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,2,3,0,0,0],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,0,0,0],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,0,0,0],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,2,2,2,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,3,3,3],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,0,0,0],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,0,0,0],
[1,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,4,3,0,0,0],
[1,1,1,1,1,1,1,1,1,1,1,1,4,4,4,1,1,1,1,1,1,1,1,1,1,1,1,1,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,3,4,4,4,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
[0,0,0,0,0,0,0,0,0,0,0,3,3,3,3,3,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]]
    def drawMap(self, surface):
            for i,row in enumerate(self.array):
                for j,tile in enumerate(row):
                    if tile > 0:
                        surface.blit(self.images[tile - 1], (self.x + j * self.tilesize, self.y + i * self.tilesize))

    def move_x(self, direction):
        self.x += direction

    def move_y(self, direction):
        self.y += direction