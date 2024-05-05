import itertools
from ursina import *
from src.blocks.block import Block
from perlin_noise import PerlinNoise
from src.common.frustum import Frustum

class Ground:
    def __init__(self, xCell=(-10, 10), zCell=(-10, 10)):
        self.xCell = xCell
        self.zCell = zCell
        self.min_height = -5
        self.height_map = {}
        self.noise = PerlinNoise(octaves=3, seed=random.randint(1, 10))
        self.cell_size = 0.02
        self.height_multiplier = 0.75
        self.drawGround()

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

                block_position = (x, y + self.min_height, z)
                block_list.append(Block(block_type=block_type, add_to_scene_entities=False).draw_block(position=block_position))
        ground_batch = Block(enabled=False)
        ground_batch.combine(block_list)
        ground_batch.enabled = True

    # def drawGround(self):
    #     self.generate_height_map()
    #     fov = 90  # FOV theo chiều ngang
    #     aspect_ratio = camera.aspect_ratio
    #     near_distance = 0.1  # Khoảng cách đến near plane
    #     far_distance = 1000  # Khoảng cách đến far plane
    #     frustum_planes = Frustum().calculate_frustum_planes(camera, fov, aspect_ratio, near_distance, far_distance)

    #     block_list = []
    #     for x, z in itertools.product(range(self.xCell[0], self.xCell[1]), range(self.zCell[0], self.zCell[1])):
    #         height = self.height_map[(x, z)]
    #         for y in range(height, self.min_height - 1, -1):
    #             if y == self.min_height:
    #                 block_type = 'bedrock'
    #             elif y == height:
    #                 block_type = 'grass'
    #             elif y > height - 3:
    #                 block_type = 'dirt'
    #             else:
    #                 block_type = 'stone'
    #             block_position = Vec3(x, y + self.min_height, z)
    #             # Kiểm tra xem block có nằm trong frustum không
    #             in_frustum = all(plane.is_in_front(block_position) for plane in frustum_planes.values())
    #             if in_frustum:
    #                 # Thêm block vào danh sách để vẽ
    #                 block_list.append(Block(block_type=block_type, add_to_scene_entities=False).draw_block(position=block_position))
    #     # Kết hợp và hiển thị các block
    #     ground_batch = Block(enabled=False)
    #     ground_batch.combine(block_list)
    #     ground_batch.enabled = True
