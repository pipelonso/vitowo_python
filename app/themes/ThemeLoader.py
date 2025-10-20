import os

class ThemeLoader:

    def __init__(self):
        self.selected_theme = 'dark'
        pass

    def get_theme_structure(self, theme: str):
        if os.path.exists('app/themes/' + theme + '.qss'):
            with open('app/themes/' + theme + '.qss') as file:
                qss = file.read()
                self.selected_theme = theme
                return qss
