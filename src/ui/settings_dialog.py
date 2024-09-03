from PySide6.QtWidgets import QDialog, QVBoxLayout, QLabel

class SettingsDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("환경설정")
        
        self.resize(400, 300)
        self.setup_ui()
        
        
    def setup_ui(self):
        layout = QVBoxLayout()
        
        label = QLabel("여기에 설정 항목이 표시됨")
        layout.addWidget(label)
        
        self.setLayout(layout)