import itertools
from ursina import *
from src.blocks.block import Block
from perlin_noise import PerlinNoise

class Ground:
    ground_batch = Entity(enabled=False)
    def __init__(self, xCell=(-10, 10), zCell=(-10, 10)):
        self.xCell = xCell
        self.zCell = zCell
        self.min_height = -5
        self.height_map = {}
        self.noise = PerlinNoise(octaves=3, seed=random.randint(1, 10))
        self.cell_size = 0.02
        self.height_multiplier = 0.75
        self.generate_height_map()

    def generate_height_map(self):
        for x, z in itertools.product(range(self.xCell[0], self.xCell[1]), range(self.zCell[0], self.zCell[1])):
            height = self.noise([x * self.cell_size, z * self.cell_size])
            self.height_map[(x, z)] = math.floor(height * self.height_multiplier)

    def drawGround(self):
        self.generate_height_map()
        block_list = []
        for x, z in itertools.product(range(self.xCell[0], self.xCell[1]), range(self.zCell[0], self.zCell[1])):
            height = self.height_map[(x, z)]
            for y in range(height, self.min_height - 1, -1):
                if y == self.min_height:
                    block_type = 'bedrock'
                elif y == height:
                    block_type = 'grass'
                elif y > height - 3:
                    block_type = 'dirt'
                else:
                    block_type = 'stone'

                block_list.append(Block(position=(x, y + self.min_height, z), block_type=block_type))
        self.ground_batch.enabled = True
        self.ground_batch.combine(block_list)