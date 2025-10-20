import json
import os
from typing import Callable, Any


class SettingsController:

    def __init__(self):

        self.file_name = 'settings.json'
        self.settings_load_failed = False
        self.failed_notification_callback: Callable | None = None
        self.load_error = ''

    def get_file_dict_content(self) -> dict:

        try:
            file_read = open(self.file_name)
            content = file_read.read()
            json_content = json.loads(content)
            self.settings_load_failed = False
        except Exception as e:
            self.settings_load_failed = True
            json_content = self.get_default_settings()
            self.load_error = e

        return json_content

    def register_key(self, key: str, value: Any = None):

        json_content = self.get_file_dict_content()
        json_content[key] = value

        with open(self.file_name) as file:
            file.write(json.dumps(json_content, indent=2))

    def create_file_if_not_exists(self):
        if not os.path.exists(self.file_name):
            self.generate_default_config()

    def get_value(self, key_name: str):
        json_content = self.get_file_dict_content()
        if key_name in json_content:
            return json_content[key_name]

    def generate_default_config(self):
        with open(self.file_name, mode='w') as file:
            file.write(
                json.dumps(self.get_default_settings(), indent=2)
            )

    @staticmethod
    def get_default_settings() -> dict:
        return {
            "theme" : "dark",
            "language" : "english"
        }

    def notify_failed_on_load(self):
        self.failed_notification_callback(self.load_error)