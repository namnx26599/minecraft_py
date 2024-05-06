from ursina import *
from src.ground.ground import Ground
from src.player.player import Player
from src.events.manipulate_blocks import ManipulateBlocks
from src.menu.game_menu import GameMenu
from src.player.material_picker import MaterialPicker
from src.player.inventory import Inventory

# Khởi tạo ứng dụng Usina
app = Ursina()
player = Player(position=(0,0,0))
ground = Ground()
inventory = Inventory()
material_picker = MaterialPicker()
manipulate_block = ManipulateBlocks(player=player, material_list=material_picker.material_list)
game_menu = GameMenu()

# Setup của sổ
Sky()
window.title = 'Minecraft' # Đặt tiêu đề cho cửa sổ
window.borderless = True              # Cửa sổ có viền
window.fullscreen = False              # Không hiển thị toàn màn hình
window.exit_button.visible = True      # Hiển thị nút thoát
window.fps_counter.enabled = True      # Hiển thị bộ đếm FPS
mouse.locked = True
window.fps_counter.enabled = True

def input(key):
    if key == 'escape':
        manipulate_block.enabled = False
        player.enabled = not player.enabled
        game_menu.enabled = not game_menu.enabled
        if game_menu.enabled:
            invoke(setattr, application, 'paused', True)
    if key == 'b':
        manipulate_block.enabled = False
        material_picker.enabled = not material_picker.enabled
        player.enabled = not player.enabled
        inventory.enabled = not inventory.enabled
    if key == 'f':
        player.gravity = 1 if player.gravity == 0 else 0
    if key == 'space' and player.gravity == 0:
        player.y +=2
    else:
        print(player.position)
        manipulate_block.interact(key)

def update():
    if held_keys['left mouse'] or held_keys['right mouse']:
        player.active()
    else:
        player.passive()

if __name__ == "__main__":
    for i in range(7):                                                  
        inventory.append(random.choice(('grass', 'snow', 'dirt', 'bedrock', 'stone')))
    app.run()