"""
Game name: Back in Time
Project: Application Development and Emerging Technology
Professor: Gary Bato-ey

Frames: 30 fps
walking animation(character and enemy): 7 frames/images
characters size(character and enemy): 130x80 pixels

developers:
    1. Christian Vaydal
    2. Aeron Segobia
    3. Ethan Diego Lim

Date started: April 16, 2024
"""

import pygame
from character import *
from object import *
from create import Create
from camera import Camera
from Data.read import Read
from UI import UI
from loading import Loading
from timer import Timer

# IMPORT MAPS
# from Maps.map1 import TileMap as Map1 
from Maps import baseMap # MAP1 / BASE
from Maps import Map_2
from Maps import Map_3

# initialize pygame
pygame.init()

# screen
windowSize = {'width': 700, 'height': 500} # size of the display
window = pygame.display.set_mode((windowSize['width'], windowSize['height']))
pygame.display.set_caption('End Of Time')

# clock and FPS - frame per second
clock = pygame.time.Clock()
fps = 30 # 30 frames per second

# TImer
timer = Timer(fps)

# Program flow
flow = ['intro', 'main-menu', 'in-game', 'outro']
current = flow[0]

# loading and checking resources
load = Loading((windowSize['width'] - 500) / 2, (windowSize['height'] - 200), 500, 15)

# MAP
base = baseMap.TileMap(25, 0, 0)
map_2 = Map_2.TileMap(25, 0, 0)
map_3 = Map_3.TileMap(25, 0, 0)

# GUIs (not yet draw)
itemsGUI = UI((windowSize['width'] - 260) / 2, (windowSize['height'] - 70), 260, 60, 'itembar_4')

# pause button
pauseButton = UI((windowSize['width'] - 60), 10, 40, 40, 'pause_btn')

# player Icon and health bar
playerIcon = UI(10, 10, 90, 90, 'player_frame2')
# healthbar = UI(100, 10, 128, 32, 'life_bar4') # uncomment this later

listGUIs = [itemsGUI, pauseButton, playerIcon] # healthbar

# PLAYER
player = Player(((windowSize['width'] - 50) / 2), ((windowSize['height'] - 50) / 2), 50, 50)

# read object data from json file data
readData = Read('Data/data.json')
readData.read() # read all data
readData.strToTuple('Base') # make all string tuple in Map1 to tuple
readData.strToTuple('Map2')
readData.strToTuple('Enemies_m2')

# CREATIONS

# for loading screen / intro
title = [Object((windowSize['width'] - 200) / 2, (windowSize['height'] - 350) / 2, 200, 200, 'animated', 'title_2')]

# create objects for blocks and other objects - Map 1 / base
create_base = Create(window, player, readData.data['Base'])
create_base.create()

# create objects for blocks and other objects - Map 1 / base
create_map2 = Create(window, player, readData.data['Map2'])
create_map2.create()

# enemies for map 2
enemies_map2 = Create(window, player, readData.data['Enemies_m2'])
enemies_map2.create_enemies()

# camera
camera = Camera(player, windowSize)

# LIST of all objects in map 1 / Base
allObjects1 = create_base.listofObjects+[base]
allObjects2 = create_map2.listofObjects+[map_2]+enemies_map2.listEnemies

# create.listofObjects is a list of all objecst
# listenemies is a list of all enemies
# listOfMap is a list of map tiles

player.MapObjects = [create_base.mapObject, create_map2.mapObject]

# draw base map function
def draw_base():

    window.fill((54, 54, 54))

    # camera
    camera.move(allObjects1)

    # map for the base map
    base.drawMap(window)

    # draw object
    create_base.draw()

    # draw player
    player.draw(window, create_base.listofObjects[1:])
    player.navigate()

    for guis in listGUIs:
        guis.draw(window)

    pygame.display.flip()

# draw MAP 2 funtion
def draw_map2():
    window.fill((54, 54, 54))

    # camera for map 2
    camera.move(allObjects2)

    # draw map 2
    map_2.drawMap(window)

    # draw objects
    create_map2.draw()

    # enemies
    # enemies_map2.draw_enemy(create_map2.listofObjects[1:]) # uncomment later

    # draw player
    player.draw(window, create_map2.listofObjects[1:])
    player.navigate()

    for guis in listGUIs:
        guis.draw(window)

    pygame.display.flip()

def draw_map3():
    window.fill((54, 54, 54))

    map_3.drawMap(window)

    player.draw(window, [])

    camera.move([player,map_3])

    for gui in listGUIs:
        gui.draw(window)

    pygame.display.flip()

# opening scene function / credits and loading
def Opening():
    global current, title

    window.fill((54, 54, 54))

    # draw animated title
    title[0].draw(window)

    # slow down the loading animation
    load.draw(window)
    if timer.coolDown(5):
        check = load.checkResources()
        if check:
            if timer.coolDown(5):
                player.location = 'base'
                current = flow[2]
                del title # remove or delete this loaded image

    pygame.display.flip()

# for testing
fpsCollected = [] # collecting frames per second value

# main function
def main():
    run = True

    while run:

        # fps of the game
        clock.tick(fps)

        # check for events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        # draw the display
        # intro
        if current == flow[0]:
            Opening()
        # in-game
        elif current == flow[2]:
        # draw the display
            if player.location == 'base':
                draw_base()
            elif player.location == 'map2':
                draw_map2()
            elif player.location == 'map3': # not yet
                draw_map3()

        # for testing
        chechFPS(round(clock.get_fps(), 2))

    # quit program after the loop
    print('fps timeline:',fpsCollected)
    print('lowest:', min(fpsCollected), '\nHighest:', max(fpsCollected), '\nLocation:', player.location)
    pygame.quit()

# function for testing

# frame drops test
def chechFPS(frames):
    if frames not in fpsCollected and frames >= 1:
        fpsCollected.append(frames)

# main program
if __name__=='__main__':
    main()