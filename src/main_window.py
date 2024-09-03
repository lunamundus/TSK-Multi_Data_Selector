from PySide6.QtWidgets import QMainWindow

from ui.main_window_ui import MainWindowUI
from handlers.main_window_handlers import MainWindowHandlers

class MainWindow(QMainWindow, MainWindowUI, MainWindowHandlers):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skin Temperature Data Selector for TSK Multi")
        
        self.resize(500, 300) # (width, height)
        
        self.setup_ui(self) # UI 설정
        self.connect_signals(self) # 이벤트 연결
        
    
    def add_file(self):
        super().add_file(self)
        
    
    def process_and_save_data(self):
        super().process_and_save_data(self)
        
        
    def open_settings_dialog(self):
        super().open_settings_dialog(self)
        

# from PySide6.QtWidgets import QMainWindow, QDialog, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QListWidget, QFileDialog, QMessageBox, QLabel
# from PySide6.QtCore import Qt

# from src.core.data_processing import data_processing, save_dataframe_to_excel

# class SettingsDialog(QDialog):
#     def __init__(self, parent=None):
#         super().__init__(parent)
        
#         self.setWindowTitle("환경설정")
        
#         self.resize(400, 300)
#         self.setup_ui()
        
        
#     def setup_ui(self):
#         layout = QVBoxLayout()
        
#         label = QLabel("여기에 설정 항목이 표시됨")
#         layout.addWidget(label)
        
#         self.setLayout(layout)


# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
        
#         self.setWindowTitle("Skin Temperature Data Selector for TSK Multi")
        
#         self.resize(500, 300) # (width, height)
#         self.setup_ui()
        
        
#     def setup_ui(self):
#         # 전체 레이아웃
#         main_widget = QWidget()
#         main_layout = QVBoxLayout()
        
#         # 버튼 레이아웃
#         data_processing_button_layout = QHBoxLayout()
        
#         # add file button
#         add_file_button = QPushButton("파일 추가")
#         add_file_button.setFixedSize(250, 30)
#         add_file_button.clicked.connect(self.add_file)
#         data_processing_button_layout.addWidget(add_file_button)
        
#         # processing data button
#         processing_data_button = QPushButton("파일 처리 및 저장")
#         processing_data_button.setFixedSize(250, 30)
#         processing_data_button.clicked.connect(self.process_and_save_data)
#         data_processing_button_layout.addWidget(processing_data_button)
        
#         main_layout.addLayout(data_processing_button_layout)
        
#         # file list widget
#         self.file_list_widget = QListWidget()
#         main_layout.addWidget(self.file_list_widget)
        
#         # settings button
#         settings_button = QPushButton("환경설정")
#         settings_button.setFixedSize(500, 30)
#         settings_button.clicked.connect(self.open_settings_dialog)
#         main_layout.addWidget(settings_button)
        
#         main_widget.setLayout(main_layout)
#         self.setCentralWidget(main_widget)
    
    
#     def add_file(self):
#         # show file dialog
#         file_dialog = QFileDialog()
#         file_path, _ = file_dialog.getOpenFileName(self, "파일 선택", "", "All Files (*.*)")
        
#         if file_path:
#             self.file_list_widget.addItem(file_path)
            
    
#     def process_and_save_data(self):
#         # 선택된 파일 확인
#         selected_items = self.file_list_widget.selectedItems()
        
#         if not selected_items:
#             QMessageBox.warning(self, "경고", "처리할 파일을 선택해주세요.")
#             return
            
#         file_path = selected_items[0].text()
        
#         # 데이터 처리 함수 호출
#         result = data_processing(file_path=file_path)
#         if isinstance(result, str):
#             QMessageBox.critical(self, "오류", result)
#             return
        
#         file_name, file_dir, selected_skin_temp_dataframe = result
        
#         # 데이터프레임을 엑셀로 저장
#         save_result = save_dataframe_to_excel(file_dir=file_dir, file_name=file_name, selected_dataframe=selected_skin_temp_dataframe)
        
#         QMessageBox.information(self, "결과", save_result)
        
    
#     def open_settings_dialog(self):
#         # open settings dialog
#         settings_dialog = SettingsDialog(self)
#         settings_dialog.exec()