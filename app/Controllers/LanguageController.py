import json

from app.Controllers.SettingsController import SettingsController


class LanguageController:

    def __init__(self):
        self.settings_controller = SettingsController()
        self.languages_file_path = 'resources/translate/languages.json'
        pass

    @staticmethod
    def translate(language: str, key: str, replace:dict=None):
        # TODO: hacer que se pueda remplazar valores en las traducciones enviando un dict y la sintaxis para remplazar sea {{variable}}
        pass

    def get_language_list(self):
        with open(self.languages_file_path) as file:
            languages_raw = file.read()
            return json.loads(languages_raw)["list"]

    def get_current_language(self):
        return self.settings_controller.get_value("language")
