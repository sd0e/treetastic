class Tree:
    def __init__(self, name, rel_width, rel_height, size, cost):
        self.name = name
        self.rel_width = rel_width
        self.rel_height = rel_height
        self.size = size
        self.cost = cost
    def __repr__(self):
        return f"{self.name} || {self.rel_width} x {self.rel_height} || {self.size}"
    def __str__(self):
        return f"{self.name} || {self.rel_width} x {self.rel_height} || {self.size}"


def getTreeTypes():
    return [
        Tree("Paper birch",
             0.2,
             0.3,
             "big",
            30000),
        Tree("Silver birch",
             0.3,
             0.2,
             "mid",
            20000),
        Tree("Rowan",
             0.15,
             0.1,
             "small",
            10000),
        Tree("Hawthorn",
             0.1,
             0.1,
             "tiny",
            5000),
    ]

def doStuff():
    print(getTreeTypes()[0])