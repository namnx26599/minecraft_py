from ursina import *
from src.common.textures import TextureMaterial

app = Ursina()
material = TextureMaterial()
class Block(Entity):
    block_type = 'grass'
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        if 'block_type' in kwargs:
            self.block_type = kwargs['block_type']
    
    def draw_block(self, position=(0, 0, 0), enabled=True):
        entity = Entity(
            position=position,
            model='assets/models/block_model',
            texture=material.block_textures.get(self.block_type),
            scale=1,
            origin_y=-0.5,
            collider='box',
            enabled=enabled
        )
        entity.block_type = self.block_type
        material.set_material_selected_block = self.block_type