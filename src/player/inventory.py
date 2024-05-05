from ursina import *
from src.common.textures import TextureMaterial
from src.blocks.block import Block

app = Ursina()

material = TextureMaterial()
class Inventory(Block):
    def __init__(self):
        super().__init__(
            parent = camera.ui,                                         
            model = 'quad',
            scale = (.5, .8),                                           
            origin = (-.5, .5),                                         
            position = (-.3,.4),                                        
            texture = 'white_cube',                                     
            texture_scale = (5,8),                                      
            color = color.rgba(45, 45, 45, 0.9),
            enabled=False                                          
            )
        self.item_parent = Block(parent=self, scale=(1/5,1/8), z=0)

    def find_free_spot(self):                                                      
        taken_spots = [(int(e.x), int(e.y)) for e in self.item_parent.children]
        for y in range(8):                                                         
            for x in range(5):                                                     
                if not (x,-y) in taken_spots:                                      
                    return (x,-y)

    def append(self, item):                                          
        material_item_box = Draggable(
            parent = self.item_parent,
            color = color.clear,
            origin = (-.5, .5),
            position = self.find_free_spot()
            )
        image_material = Block(
            parent = material_item_box,
            model = 'assets/models/block_model',
            texture = material.block_textures.get(item),
            color = color.white,
            z = -.5,
            scale = .5,
            origin = (-1.2, 1.1),
            rotation=(-15, -30, -5)
            )
        name = item.replace('_', ' ').title()
        material_item_box.tooltip = Tooltip(name)
        material_item_box.tooltip.background.color = color.hsv(0,0,0,.8)

        def drag():
            material_item_box.org_pos = (material_item_box.x, material_item_box.y)
            image_material.z = -1.5

        def drop():
            material_item_box.x = round(material_item_box.x)
            material_item_box.y = round(material_item_box.y)
            image_material.z = -.5
            '''if outside, return to original position'''
            if material_item_box.x < 0 or material_item_box.x >= 5 or material_item_box.y > 0 or material_item_box.y <= -8:
                material_item_box.position = material_item_box.org_pos
                return

            '''if the spot is taken, swap positions'''
            for c in self.item_parent.children:
                if c == material_item_box or not isinstance(c, Draggable):
                    continue

                if c.x == material_item_box.x and c.y == material_item_box.y:
                    c.position = material_item_box.org_pos

        material_item_box.drag = drag
        material_item_box.drop = drop
        
