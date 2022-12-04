
from PIL import Image
import numpy as np
import random
import matplotlib.pyplot as plt

def yes_no(percent):
    #finkcija za naumični True ili False odgovor
    return random.randrange(10000) < percent

def add_color(world):
    color_world = np.zeros(world.shape+(3,))
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < 0:
                color_world[i][j] = blue
            elif world[i][j] < 0.05:
                color_world[i][j] = beach
            elif world[i][j] < .20:
                color_world[i][j] = green
            elif world[i][j] < 0.27:
                color_world[i][j] = mountain
            elif world[i][j] < 0.35:
                color_world[i][j] = big_mountain
            elif world[i][j] < 0.5:
                color_world[i][j] = snow
            elif world[i][j] < 1.0:
                color_world[i][j] = ice
    return color_world


def bionify(world, color_world, biomes):
    #kod ovdje, na principu dodavanja boja
    return(color_world)


def gradient_biomes(biomes):
    #na heightmap primjeni gradijent od juga prema sjeveru
    #ovdje ide kod
    return(biomes)

def riverify(color_world, world):
    river = [67, 213, 232]
    directions = [ (0, -1), (1, 0), (0, 1), (-1, 0)]
    coordinates = []
    #kod za nasumično odabiranje početne pozicije rijeke
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < 0.35 and world[i][j] > 0.20:
                if yes_no(2) == True:
                    color_world[i][j] = river
                    coordinates.append([i, j])
    
    for coordinate in coordinates:
        i=coordinate[0]
        j=coordinate[1]
        #algoritam za ucrtavanje rijeka ovdje

    return(color_world)

def show_map(map):
    a = np.asarray(map.astype(np.uint8))
    im = Image.fromarray(a)
    plt.imshow(im)
    plt.show()
    plt.clf()

def show_heights(heights):
    a = np.asarray(heights)
    plt.imshow(a/255, cmap="Greys_r")
    plt.show()
    plt.clf()

blue = [65,105,225]
green = [34,139,34]
beach = [238, 214, 175]
snow = [191, 190, 189]
ice = [76, 141, 245]
big_mountain = [139, 137, 137]
mountain = [115, 111, 106]

jungle = [125, 252, 20]
savanna = [194, 161, 52]
tundra = [40, 79, 75]
desert = [250, 220, 72]
taiga = [14, 115, 52]

shape = (1024,1024)
world = np.load("world.npy")
biomes = np.load("biomes.npy")

show_heights(world)
show_heights(biomes)

biomes=gradient_biomes(biomes)
show_heights(biomes)

color_world1 = add_color(world)
show_map(color_world1)

#color_world2 = bionify(world, color_world1, biomes)
#show_map(color_world2)

#color_world3 = riverify(color_world2, world)
#show_map(color_world3)
