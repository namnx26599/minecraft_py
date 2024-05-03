from ursina import *
from src.ground.ground import Ground
from src.player.player import Player
from src.events.manipulate_blocks import ManipulateBlocks
from src.menu.game_menu import GameMenu
from src.player.material_picker import MaterialPicker

# Khởi tạo ứng dụng Usina
app = Ursina()
player = Player(position=(0,0,0))
ground = Ground()
manipulate_block = ManipulateBlocks(player=player.player)
game_menu = GameMenu()

# Setup của sổ
Sky()
window.title = 'Demo' # Đặt tiêu đề cho cửa sổ
window.borderless = True              # Cửa sổ có viền
window.fullscreen = False              # Không hiển thị toàn màn hình
window.exit_button.visible = True      # Hiển thị nút thoát
window.fps_counter.enabled = True      # Hiển thị bộ đếm FPS
mouse.visible = False

ground.drawGround()
material_picker = MaterialPicker()

def input(key):
    if key == 'escape':
        game_menu.enabled = not game_menu.enabled
        mouse.locked = False
        if game_menu.enabled:
            invoke(setattr, application, 'paused', True)
            mouse.visible = True
        else:
            mouse.visible = False
    else:
        manipulate_block.interact(key)

if __name__ == "__main__":
    app.run()