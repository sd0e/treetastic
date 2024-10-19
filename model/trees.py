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
             0.05,
             0.05,
             "big",
            30000),
        Tree("Silver birch",
             0.0,
             0.04,
             "mid",
            20000),
        Tree("Rowan",
             0.03,
             0.03,
             "small",
            10000),
        Tree("Hawthorn",
             0.02,
             0.02,
             "tiny",
            5000),
    ]

def doStuff():
    print(getTreeTypes()[0])