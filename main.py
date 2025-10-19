from buffer.CaptainHook import CaptainHook
from launch.AppLauncher import AppLauncher


app_buffer = CaptainHook()
launcher = AppLauncher(app_buffer)
launcher.launch()
