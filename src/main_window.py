from PySide6.QtWidgets import QMainWindow

from ui.main_window_ui import MainWindowUI
from handlers.main_window_handlers import MainWindowHandlers

class MainWindow(QMainWindow, MainWindowUI, MainWindowHandlers):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skin Temperature Data Selector for TSK Multi")
        
        self.resize(600, 400) # (width, height)
        
        self.setup_ui(self) # UI 설정
        self.connect_signals(self) # 이벤트 연결
        
    
    def add_file(self):
        super().add_file(self)
        
    
    def process_and_save_data(self):
        super().process_and_save_data(self)
        
    
    def delete_file(self):
        super().delete_file(self)
        
    
    def reset_file(self):
        super().reset_file(self)
        
    
    def update_reset_button_state(self):
        super().update_reset_button_state(self)
        
        
    def open_settings_dialog(self):
        super().open_settings_dialog(self)
