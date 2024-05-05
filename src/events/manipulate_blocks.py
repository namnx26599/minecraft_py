from ursina import *
from src.blocks.block import Block
from src.common.textures import TextureMaterial

material = TextureMaterial()
class ManipulateBlocks:
    def __init__(self, player, material_list = [], distance_manipulate = 5):
        self.player = player
        self.distance_manipulate = distance_manipulate
        self.material_list = material_list
        material.add_observer(player)

    def interact(self, key):
        if key == '1':
            self.update_material(self.material_list[0])
        if key == '2':
            self.update_material(self.material_list[1])
        if key == '3':
            self.update_material(self.material_list[2])
        if key == '4':
            self.update_material(self.material_list[3])
        if key == '5':
            self.update_material(self.material_list[4])
        self.add_block(key)
        self.delete_block(key)
    
    def update_material(self, new_material):
        material.set_material_selected_block = new_material
    
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
                block = Block(block_type=material.material_selected_block).draw_block(hit_info.entity.position + hit_info.normal)
    
    def delete_block(self, key):
        '''
        ** Xóa khối tới vị trí cammera chỉ định
        destroy(): Hàm xóa entity 
        mouse.hovered_entity: Vị trí block đã tạo
        '''
        if key == 'right mouse down' and mouse.hovered_entity and self.player and mouse.hovered_entity:
            distance_to_entity = distance(self.player.position, mouse.hovered_entity.position)
            if distance_to_entity <= self.distance_manipulate and not mouse.hovered_entity.block_type == 'bedrock':
                destroy(mouse.hovered_entity)