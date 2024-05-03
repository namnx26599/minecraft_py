from ursina import *
from src.blocks.block import Block
from src.common.textures import TextureMaterial

material = TextureMaterial()
class ManipulateBlocks:
    def __init__(self, player, distance_manipulate = 4):
        self.player = player
        self.distance_manipulate = distance_manipulate

    def interact(self, key):
        self.add_block(key)
        self.delete_block(key)
    
    def add_block(self, key):
        '''
        ** Thêm khối tới vị trí cammera chỉ định
        raycast(): Hàm kiểm tra xem đối tượng player có và chạm với bất kì đối tượng nào khác hay không
        camera.world_position: Vị trí player
        camera.forward: Điểm chạm
        distance: Khoảng cách có thể chạm
        '''
        if key == 'left mouse down':
            hit_info = raycast(origin=camera.world_position, direction=camera.forward, distance=self.distance_manipulate)
            if hit_info.hit:
                # hit_info.entity.position + hit_info.normal: Vị trí được chọn
                print(hit_info.entity.position + hit_info.normal)
                block = Block(hit_info.entity.position + hit_info.normal, material.selected_block)
    
    def delete_block(self, key):
        '''
        ** Xóa khối tới vị trí cammera chỉ định
        destroy(): Hàm xóa entity 
        mouse.hovered_entity: Vị trí block đã tạo
        '''
        if key == 'right mouse down' and mouse.hovered_entity and self.player:
            distance_to_entity = distance(self.player.position, mouse.hovered_entity.position)
            print(distance_to_entity)
            if distance_to_entity <= (self.distance_manipulate - 2) and not mouse.hovered_entity.block_type == 'bedrock':
                destroy(mouse.hovered_entity)