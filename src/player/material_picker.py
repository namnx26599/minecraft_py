from ursina import *
from src.common.textures import TextureMaterial

material = TextureMaterial()
class MaterialPicker(Entity):
    materials = ['brick', 'dirt', 'grass', 'stone', 'wood']
    # mini_block = Entity(
    #     parent=camera,
    #     model='assets/models/block_model',
    #     texture=material.get_block_textures().get(material.get_selected_block()),
    #     scale=0.2,
    #     position=(-0.35, -0.25, 0.5),
    #     rotation=(-15,-30, -5)
    # )
    def __init__(self):
        super().__init__()
        self.buttons = []

        # Tạo các nút cho mỗi vật liệu
        for i, material in enumerate(self.materials):
            button = Button(parent=camera.ui, text=material, scale=(0.2, 0.1), color=color.white, z=-0.1, position=(-0.35, -0.25 - i*0.15))
            button.on_click = Func(self.select_material, material)  # Xử lý sự kiện khi người dùng nhấp vào nút
            self.buttons.append(button)

    def select_material(self, material):
        print('Selected material:', material)