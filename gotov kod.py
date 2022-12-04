
import noise
import numpy as np
from PIL import Image
import random
import matplotlib.pyplot as plt

def yes_no(percent):
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
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < .20 and world[i][j] > 0:
                if biomes[i][j] < -0.8:
                    color_world[i][j] = jungle
                elif biomes[i][j] > -0.75 and biomes[i][j] < -0.6:
                    color_world[i][j] = savanna
                elif biomes[i][j] > -0.6 and biomes[i][j] < -0.4:
                    color_world[i][j] = desert
                elif biomes[i][j] > 0 and biomes[i][j] < 0.3:
                    color_world[i][j] = taiga
                elif biomes[i][j] > 0.3:
                    color_world[i][j] = tundra
    return(color_world)


def gradient_biomes(biomes):
    subtracter = 0
    for i in range(shape[0]):
        for j in range(shape[1]):
            biomes[i][j] = biomes[i][j] - subtracter
        subtracter = subtracter + 0.0005
    return(biomes)

def riverify(color_world, world):
    river = [67, 213, 232]
    directions = [ (0, -1), (1, 0), (0, 1), (-1, 0)]
    coordinates = []
    for i in range(shape[0]):
        for j in range(shape[1]):
            if world[i][j] < 0.35 and world[i][j] > 0.20:
                if yes_no(2) == True:
                    color_world[i][j] = river
                    coordinates.append([i, j])
    
    for coordinate in coordinates:
        i=coordinate[0]
        j=coordinate[1]
        c=0
        cursor = [i, j]
        the_elder_cursor = cursor
        the_elder_cursors_3 = []
        the_elder_cursors_3.append(the_elder_cursor)
        try:
            while world[cursor[0], cursor[1]] > 0 and c < 300:
                c=c+1
                lowest_value = 100000
                lowest_position = []
                for direction in directions:
                    dx, dy = direction
                    x = cursor[0]+dx
                    y = cursor[1]+dy
                    if world[x][y] <= lowest_value:
                        if [x, y] != the_elder_cursor:
                            if cursor not in the_elder_cursors_3:
                                lowest_value = world[x][y]
                                lowest_position = [x, y]
                            else:
                                random_position = random.choice([x for x in directions if x!= direction])
                                dx, dy = random_position
                                x = cursor[0]+dx
                                y = cursor[1]+dy
                                lowest_value = world[x][y]
                                lowest_position = [x, y]
                        else:
                            pass
                the_elder_cursor = cursor
                the_elder_cursors_3.append(the_elder_cursor)
                cursor = lowest_position  
                color_world[cursor[0], cursor[1]] = river
        except IndexError:
            pass

    return(color_world)
        
def gradient_world(world):
    adder = 0.0001
    subtracter = 0
    for i in reversed(range(int((shape[0]/2)))):
        for j in range(int(shape[1])):
            world[j][i] = world[j][i] - subtracter
        subtracter = subtracter + adder

    subtracter = 0
    for i in range(int((shape[0]/2)), shape[0]):
        for j in range(int(shape[1])):
            world[j][i] = world[j][i] - subtracter
        subtracter = subtracter + adder
    return(world)

def merge_create_maps(w_map):
    shape = (1024,1024)
    octaves = 12
    persistence = 0.5
    lacunarity = 2.0

    scale = 250
    seed = np.random.randint(0,100)
    world_3 = np.zeros(shape)
    for i in range(shape[0]):
        for j in range(shape[1]):
            world_3[i][j] = noise.pnoise2(i/scale, 
                                        j/scale, 
                                        octaves=octaves, 
                                        persistence=persistence, 
                                        lacunarity=lacunarity, 
                                        repeatx=1024, 
                                        repeaty=1024, 
                                        base=seed)
    for i in range(shape[0]):
        for j in range(shape[1]):
            w_map[i][j] = w_map[i][j] + world_3[i][j]

    return(w_map)

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
scale = 200
octaves = 70  # 12
persistence = 0.3  # 15
lacunarity = 2.0
seed = np.random.randint(0,100)  # 65
seed2 = np.random.randint(0,100)  # 91
print(seed, seed2)
world = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        world[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=seed)

biomes = np.zeros(shape)
for i in range(shape[0]):
    for j in range(shape[1]):
        biomes[i][j] = noise.pnoise2(i/scale, 
                                    j/scale, 
                                    octaves=octaves, 
                                    persistence=persistence, 
                                    lacunarity=lacunarity, 
                                    repeatx=1024, 
                                    repeaty=1024, 
                                    base=seed2)

show_heights(world)
show_heights(biomes)
#np.save("world.npy", world)
#np.save("biomes.npy", biomes)        

print(world)
show_heights(world)
show_heights(biomes)
biomes=gradient_biomes(biomes)
show_heights(biomes)
#world = merge_create_maps(world)   #slow, results aren't that good
#world = gradient_world(world)
color_world1 = add_color(world)
show_map(color_world1)
color_world2 = bionify(world, color_world1, biomes)
show_map(color_world2)
color_world3 = riverify(color_world2, world)
show_map(color_world3)