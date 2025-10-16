from buffer.CaptainHook import CaptainHook
from launch.AppLauncher import AppLauncher
from launch import Loader

launcher = AppLauncher()

if __name__ == 'main':
    Loader.app_buffer = CaptainHook()
    launcher.launch()