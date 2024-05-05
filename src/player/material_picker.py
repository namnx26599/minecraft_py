from ursina import *
from src.common.textures import TextureMaterial
from src.blocks.block import Block

material = TextureMaterial()
class MaterialPicker(Block):
    material_list = ['grass', 'stone', 'dirt', 'bedrock', 'snow',]
    def __init__(self, **kwargs):
        super().__init__(
            parent = camera.ui,                                         
            model = 'quad',
            scale = (.5, .06),                                           
            origin = (-.5, .5),                                         
            position = (-.3,-.4),                                        
            texture = 'white_cube',                                     
            texture_scale = (9,1),                                      
            color = color.rgba(64, 64, 64, 0.7),
            enabled=True                                          
            )
        self.item_parent = Entity(parent=self, scale=(1/9,1), z=0)

        for i in range(9):
            self.append(self.get_material_block(i))

    def get_material_block(self, i):
        if i < len(self.material_list):
            return self.material_list[i]
        else:
            return ''
        
    def find_free_spot(self):                                                      
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        for x in range(9):
            if not (x, 0) in taken_spots:
                return (x, 0)

    def append(self, item):
        material_item_box = Entity(
            parent = self.item_parent,
            origin = (-1, 1),
            position = self.find_free_spot(),
            model = 'assets/models/block_model',
            texture = material.block_textures.get(item),
            scale = (0.6, 0.6, 0.6),
            rotation=(-15, -30, -5),
            z=-1
        )
        if item == '':
            material_item_box.color = color.clear
