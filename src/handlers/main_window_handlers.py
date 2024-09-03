from PySide6.QtWidgets import QFileDialog, QMessageBox

from ui.settings_dialog import SettingsDialog
from core.data_processing import data_processing, save_dataframe_to_excel

class MainWindowHandlers:
    def connect_signals(self, main_window):
        main_window.add_file_button.clicked.connect(main_window.add_file)
        main_window.processing_data_button.clicked.connect(main_window.process_and_save_data)
        main_window.settings_button.clicked.connect(main_window.open_settings_dialog)
        
        
    def add_file(self, main_window):
        # show file dialog
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(main_window, "파일 선택", "", "All Files (*.*)")
        
        if file_path:
            main_window.file_list_widget.addItem(file_path)
            
    
    def process_and_save_data(self, main_window):
        # 선택된 파일 확인
        selected_items = main_window.file_list_widget.selectedItems()
        
        if not selected_items:
            QMessageBox.warning(self, "경고", "처리할 파일을 선택해주세요.")
            return
            
        file_path = selected_items[0].text()
        
        # 데이터 처리 함수 호출
        result = data_processing(file_path=file_path)
        if isinstance(result, str):
            QMessageBox.critical(main_window, "오류", result)
            return
        
        file_name, file_dir, selected_skin_temp_dataframe = result
        
        # 데이터프레임을 엑셀로 저장
        save_result = save_dataframe_to_excel(file_dir=file_dir, file_name=file_name, selected_dataframe=selected_skin_temp_dataframe)
        QMessageBox.information(self, "결과", save_result)
        
    
    def open_settings_dialog(self, main_window):
        # open settings dialog
        settings_dialog = SettingsDialog(main_window)
        settings_dialog.exec()