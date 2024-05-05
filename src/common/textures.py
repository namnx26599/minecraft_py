from ursina import *
from src.common.observable import Observable

app = Ursina()
class TextureMaterial(Observable):
    def __init__(self):
        super().__init__()
        self._material_selected_block = 'grass'
        self._block_textures = {
            'grass': load_texture('assets/textures/groundEarth.png'),
            'dirt': load_texture('assets/textures/groundMud.png'),
            'stone': load_texture('assets/textures/wallStone.png'),
            'bedrock': load_texture('assets/textures/stone07.png'),
            'snow': load_texture('assets/textures/snow.png')
        }

        self._image_texture = {
            'grass': load_texture('assets/textures/grass-image.png'),
            'stone': load_texture('assets/textures/stone-image.png'),
        }

    @property
    def material_selected_block(self):
        return self._material_selected_block
    
    @property
    def block_textures(self):
        return self._block_textures
    
    @property
    def image_texture(self):
        return self._image_texture

    @material_selected_block.setter
    def set_material_selected_block(self, new_selected_block):
        self._material_selected_block = new_selected_block
        self.notify_observers(new_selected_block)
    
    @material_selected_block.getter
    def get_selected_block(self):
        return self._material_selected_block

    