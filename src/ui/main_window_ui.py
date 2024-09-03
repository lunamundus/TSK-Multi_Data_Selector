from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget

class MainWindowUI:
    def setup_ui(self, main_window):
         # 전체 레이아웃
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # button layout
        data_processing_button_layout = QHBoxLayout()
        
        # add file button
        main_window.add_file_button = QPushButton("파일 추가")
        main_window.add_file_button.setFixedSize(250, 30)
        data_processing_button_layout.addWidget(main_window.add_file_button)
        
        # processing data button
        main_window.processing_data_button = QPushButton("파일 처리 및 저장")
        main_window.processing_data_button.setFixedSize(250, 30)
        data_processing_button_layout.addWidget(main_window.processing_data_button)
        
        main_layout.addLayout(data_processing_button_layout)
        
        # file list widget
        main_window.file_list_widget = QListWidget()
        main_layout.addWidget(main_window.file_list_widget)
        
        # settings button
        main_window.settings_button = QPushButton("환경설정")
        main_window.settings_button.setFixedSize(500, 30)
        main_layout.addWidget(main_window.settings_button)
        
        main_widget.setLayout(main_layout)
        main_window.setCentralWidget(main_widget)