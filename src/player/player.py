from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
from src.common.textures import TextureMaterial

material = TextureMaterial()
class Player:
    player = FirstPersonController()

    mini_block = Entity(
        parent=camera,
        model='assets/models/block_model',
        texture=material.get_block_textures().get(material.get_selected_block()),
        scale=0.2,
        position=(0.35, -0.25, 0.5),
        rotation=(-15,-30, -5)
    )
    

    def __init__(self, position, speed = 5):
        self.player.speed = speed
        self.player.position = position

        