import json
import os
from typing import Any

from app.Controllers.SettingsController import SettingsController


class LanguageController:

    def __init__(self):
        self.settings_controller = SettingsController()
        self.languages_file_path = 'resources/translate/languages.json'
        pass

    @staticmethod
    def translate(language: str, key: str, replace:dict=None) -> str | bool:
        lang_path = 'resources/translate/' + language + '/translations.json'
        if os.path.exists(lang_path):
            try:
                with open(lang_path) as file:
                    content = file.read()
                    json_content = json.loads(content)
                    if key in json_content:
                        text = json_content[key]
                        if replace is None:
                            return str(text)
                        else:
                            build_in_text = str(text)
                            for replace_key in replace:
                                if build_in_text.find('{{' + replace_key + '}}') > -1:
                                    build_in_text = build_in_text.replace(
                                        '{{' + replace_key + '}}', replace[replace_key]
                                    )
                            return build_in_text
                    else:
                        return ''
            except Exception as e:
                print('Language load error ' + str(e))
                return False
        else:
            print('Translation not found: ' + language)
            return False

    def get_language_list(self) -> list[str]:
        with open(self.languages_file_path) as file:
            languages_raw = file.read()
            return json.loads(languages_raw)["list"]

    def get_current_language(self):
        return self.settings_controller.get_value("language")
