from ursina import *

app = Ursina()
class TextureMaterial:
    selected_block = 'grass'
    block_textures = {
        'grass': load_texture('assets/textures/groundEarth.png'),
        'dirt': load_texture('assets/textures/groundMud.png'),
        'stone': load_texture('assets/textures/wallStone.png'),
        'bedrock': load_texture('assets/textures/stone07.png'),
        'snow': load_texture('assets/textures/snow.png')
    }
    
    def __init__(self):
        pass

    def set_selected_block(self, value):
        self.selected_block = value
    
    def get_selected_block(self):
        return self.selected_block
    
    def get_block_textures(self):
        return self.block_textures
    