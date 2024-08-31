from PySide6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QWidget, QListWidget, QFileDialog
from PySide6.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Skin Temperature Data Selector for TSK Multi")
        
        self.resize(800, 600) # (width, height)
        self.setup_ui()
        
    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # add file button
        add_file_button = QPushButton("파일 추가")
        add_file_button.clicked.connect(self.add_file)
        main_layout.addWidget(add_file_button)
        
        # file list widget
        self.file_list_widget = QListWidget()
        main_layout.addWidget(self.file_list_widget)
        
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)
    
    def add_file(self):
        # show file dialog
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "파일 선택", "", "All Files (*.*)")
        
        if file_path:
            self.file_list_widget.addItem(file_path)