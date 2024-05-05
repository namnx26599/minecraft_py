from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from src.common.textures import TextureMaterial
from src.common.observable import Observer

material = TextureMaterial()
class Player(Observer, FirstPersonController):
    def __init__(self, position, speed=5):
        super().__init__()  # Gọi phương thức khởi tạo của lớp cha Observer
        speed = speed
        position = position
        self.hand_player = Entity(
            parent=camera,
            model='assets/models/block_model',
            texture = material.block_textures.get(material.get_selected_block),
            scale=0.15, position=(0.35, -0.25, 0.5), rotation=(-15, -30, -5))
    
    def active(self):
        self.hand_player.position = (0.32, -0.27)

    def passive(self):
        self.hand_player.position = (0.35, -0.25)

    def update_material(self, material_selected_block):
        material.set_material_selected_block = material_selected_block
        self.hand_player.texture = material.block_textures.get(material_selected_block)