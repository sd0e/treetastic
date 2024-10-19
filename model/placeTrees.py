from trees import Tree, getTreeTypes
species = trees.getTreeTypes()

from nearbyPollution import nearbyPollution

def giveTreeLocationInPic(imagetextFilePath, imageFilePath):
    if (nearbyPollution < 3):
        return []
    lines = []
    with open(imagetextFile, 'r') as file:
        lines = file.readlines()
    newlines = []
    for line in lines:
        newlines.append(line.strip("\n"))
    newlines = [[float(x) for x in l.split(" ")] for l in newlines]
    
    # ok so each identified region is ready to be processed
    # [0] is type (0=building, 1=tree, 2=space),
    # [1] = centre x, [2] = centre y, [3]=width, [4]=height

    existingTrees, buildingsAround = 0
    possTrees= [] # list of lists, with each tree pos given by [x, y, type]
    cost = 0
    
    for region in newlines:
        if (region[0] == 0):
            buildingsAround += 1
        elif (region[0] == 1):
            existingTrees += 1
        else:
            for t in range(len(species)-1, -1):
                if (species[t].width < region.width and species[t].height < region.height):
                    possTrees.append([region[1], region[2], species[t].name])
                    cost += species[t].cost
                    break
            
    if (existingTrees > len(possTrees)):
        return []

    print(f"Net benefit for {imageFilePath} is {buildingsAround * len(possTrees)} at a cost of approximately £{cost}.\nReturned the positions and types of the relevant recommended trees.")
    return [possTrees, cost, buildingsAround * len(possTrees)]
