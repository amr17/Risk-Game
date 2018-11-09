import random
from . import Data, Node

class Game:
    def __init__(self, country, agentOne, agentTwo):
        #Players TBC
        self.country = country
        self.MapData = Data.EgyptCities if country=="Egypt" else Data.UsaCities
        self.cities = []
        self.constructGraph()
        self.placeArmies()
        self.populateNeighbours()

    def constructGraph(self):
        for i in range(len(self.MapData)):
            owner = "Blue" if random.getrandbits(1)==1 else "Red"
            node = Node.Node(i, owner)
            self.cities.append(node)

    def placeArmies(self):
        for city in self.cities:
            city.armies = random.randint(1, 5)

    def populateNeighbours(self):
        for city in self.cities:
            for neighbour in self.MapData[city.id]:
                city.neighbours.append(self.cities[neighbour])

    def toRender(self):
        for city in self.cities:
            yield { "color":city.owner, "armies":city.armies }