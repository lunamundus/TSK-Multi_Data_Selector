from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton, QVBoxLayout, QHBoxLayout, QStackedLayout, QWidget, QListWidget, QLabel

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
        # file_list_stacked_layout = QStackedLayout()
        main_window.file_list_widget = QListWidget()
        main_window.file_list_widget.setAcceptDrops(True)
        main_layout.addWidget(main_window.file_list_widget)
        # file_list_stacked_layout.addWidget(main_window.file_list_widget)
        # main_window.empty_list_label = QLabel("➕ 파일을 마우스로 끌어 오세요.(.csv 파일만 가능)")
        # main_window.empty_list_label.setAlignment(Qt.AlignCenter)
        # main_window.empty_list_label.setStyleSheet("color: gray; font-size: 12px;")
        # file_list_stacked_layout.addWidget(main_window.empty_list_label)
        # main_window.file_list_stacked_layout.setCurrentWidget(main_window.empty_list_label)
        # main_layout.addLayout(main_window.file_list_stacked_layout)
        
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
        main_window.reset_file_button.setEnabled(False)
        file_delete_button_layout.addWidget(main_window.reset_file_button)
        
        main_layout.addLayout(file_delete_button_layout)
        
        # settings button
        main_window.settings_button = QPushButton("환경설정")
        # main_window.settings_button.setFixedSize(600, 30)
        main_window.settings_button.setFixedHeight(30)
        main_layout.addWidget(main_window.settings_button)
        
        main_widget.setLayout(main_layout)
        main_window.setCentralWidget(main_widget)