from ursina import *

class GameMenu(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            model='quad',
            scale=(0.5, 0.25),
            position=(0, 0),
            color=color.gray,
            enabled=False
        )
        self.exit_button = Button(
            parent=self,
            model='quad',
            scale=(0.75, 0.2),
            position=(0, -0.11),
            color=color.Color(160/255, 50/255, 50/255, 1),
            hover_color=color.rgba(160/255, 50/255, 50/255, 1),
            text='Exit',
            on_click=self.exit_game
        )
        self.continue_button = Button(
            parent=self,
            model='quad',
            scale=(0.75, 0.2),
            position=(0, 0.11),
            color=color.rgba(0, 100, 0, 1),
            hover_color=color.rgba(0, 50, 0, 1),
            text='Continue',
            on_click=self.continue_game
        )

    def exit_game(self):
        application.quit()

    def continue_game(self):
        mouse.locked = True
        self.enabled = False
        invoke(setattr, application, 'paused', False)