from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget

class MainWindowUI:
    def setup_ui(self, main_window):
         # 전체 레이아웃
        main_widget = QWidget()
        main_layout = QVBoxLayout()
        
        # add file & data processing button layout
        data_processing_button_layout = QHBoxLayout()
        
        # add file button
        main_window.add_file_button = QPushButton("파일 추가")
        # main_window.add_file_button.setFixedSize(300, 30)
        main_window.add_file_button.setFixedHeight(30)
        data_processing_button_layout.addWidget(main_window.add_file_button)
        
        # data processing button
        main_window.processing_data_button = QPushButton("파일 처리 및 저장")
        # main_window.processing_data_button.setFixedSize(300, 30)
        main_window.processing_data_button.setFixedHeight(30)
        data_processing_button_layout.addWidget(main_window.processing_data_button)
        
        main_layout.addLayout(data_processing_button_layout)
        
        # file list widget
        main_window.file_list_widget = QListWidget()
        main_layout.addWidget(main_window.file_list_widget)
        
        # file delete and reset button layout
        file_delete_button_layout = QHBoxLayout()
        
        # file delete button
        main_window.delete_file_button = QPushButton("파일 목록 삭제")
        # main_window.delete_file_button.setFixedSize(300, 30)
        main_window.delete_file_button.setFixedHeight(30)
        file_delete_button_layout.addWidget(main_window.delete_file_button)
        
        # reset button
        main_window.reset_file_button = QPushButton("초기화")
        # main_window.reset_button.setFixedSize(300, 30)
        main_window.reset_file_button.setFixedHeight(30)
        # main_window.reset_file_button.setEnabled(False)
        file_delete_button_layout.addWidget(main_window.reset_file_button)
        
        main_layout.addLayout(file_delete_button_layout)
        
        # settings button
        main_window.settings_button = QPushButton("환경설정")
        # main_window.settings_button.setFixedSize(600, 30)
        main_window.settings_button.setFixedHeight(30)
        main_layout.addWidget(main_window.settings_button)
        
        main_widget.setLayout(main_layout)
        main_window.setCentralWidget(main_widget)