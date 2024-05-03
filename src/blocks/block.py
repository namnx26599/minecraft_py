from ursina import *
from src.common.textures import TextureMaterial

app = Ursina()
material = TextureMaterial()
class Block(Entity):
    def __init__(self, position=(0,0,0), block_type='bedrock', parent=None):
        super().__init__(
            position=position,
            model='assets/models/block_model',
            texture=material.get_block_textures().get(block_type),
            scale=1,
            origin_y=-0.5,
            collider='box',
            parent=parent)
        self.block_type = block_type
        material.set_selected_block(block_type)