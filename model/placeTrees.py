from trees import Tree, getTreeTypes
import cv2
species = getTreeTypes()

from nearbyPollution import nearbyPollution

def giveTreeLocationInPic(imagetextFilePath, imageFilePath):
    im = cv2.imread(imageFilePath)
    h, w, _ = im.shape
    # if (nearbyPollution(imageFilePath) < 3):
    #     return []
    lines = []
    with open(imagetextFilePath, 'r') as file:
        lines = file.readlines()
    newlines = []
    for line in lines:
        newlines.append(line.strip("\n"))
    newlines = [[float(x) for x in l.split(" ")] for l in newlines]
    
    # ok so each identified region is ready to be processed
    # [0] is type (0=building, 1=tree, 2=space),
    # [1] = centre x, [2] = centre y, [3]=width, [4]=height

    existingTrees = 0
    buildingsAround = 0
    possTrees= [] # list of lists, with each tree pos given by [x, y, type]
    cost = 0
    
    for region in newlines:
        
        if (region[0] == 0):
            buildingsAround += 1
        elif (region[0] == 1):
            existingTrees += 1
            
        else:
            print(region[0])
            for t in range(0, len(species)):
                if (species[t].rel_width < (region[3]/w) and species[t].rel_height < (region[4]/h)):
                    possTrees.append([region[1], region[2], species[t].name])
                    cost += species[t].cost
                    break
            
    if (existingTrees > len(possTrees)):
        return []

    print(f"Net benefit for {imageFilePath} is {buildingsAround * len(possTrees)} at a cost of approximately £{cost}.\nReturned the positions and types of the relevant recommended trees.")
    return [possTrees, cost, buildingsAround * len(possTrees)]

print(giveTreeLocationInPic("results.txt", "C:/Users/sebas/Downloads/Photos/IMG_20241019_121830025.jpg"))