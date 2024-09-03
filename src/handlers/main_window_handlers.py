from PySide6.QtWidgets import QFileDialog, QMessageBox

from ui.settings_dialog import SettingsDialog
from core.data_processing import data_processing, save_dataframe_to_excel

class MainWindowHandlers:
    def connect_signals(self, main_window):
        main_window.add_file_button.clicked.connect(self.add_file)
        main_window.processing_data_button.clicked.connect(self.process_and_save_data)
        main_window.settings_button.clicked.connect(self.open_settings_dialog)
        main_window.delete_file_button.clicked.connect(self.delete_file)
        main_window.reset_file_button.clicked.connect(self.reset_file)
        
        
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
            QMessageBox.warning(main_window, "경고", "처리할 파일을 선택해주세요.")
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
        QMessageBox.information(main_window, "결과", save_result)
    
    
    def delete_file(self, main_window):
        # delete file
        selected_items = main_window.file_list_widget.selectedItems()
        
        if not selected_items:
            QMessageBox.warning(main_window, "경고", "삭제할 파일을 선택해주세요.")
            return
        
        for item in selected_items:
            main_window.file_list_widget.takeItem(main_window.file_list_widget.row(item))

        QMessageBox.information(main_window, "정보", "선택된 파일이 삭제되었습니다.")
    
    
    """
    TODO: reset_file 메서드만 왜 main_window가 아닌 self로 file_list_widget을 가져와야 오류가 발생지 않는지 알아내기...!
    - 모든 ui는 main_window에서 생성됨
    - main_window.widget의 형태로 가져왔는데, reset_file 메서드에서만 이렇게 작동하지 않음
    - reset_file 메서드에서는 self.widget 형태로 가져와야 작동함 (하지만.. 여기 class에는 file_list_widget이 없는걸..?)
    """
    def reset_file(self, main_window):
        # reset file list
        if self.file_list_widget.count() > 0:
            self.file_list_widget.clear()
            QMessageBox.information(self, "정보", "파일 목록이 초기화되었습니다.")
        else:
            QMessageBox.warning(self, "경고", "추가된 파일이 없습니다.")
        
    
    """
    TODO: reset_file 메서드 문제 해결 후, update_reset_button_state 메서드 만들기
    """
    # def update_reset_button_state(self, main_window):
    #     # update reset button state
    #     if main_window.file_list_widget.count() > 0:
    #         main_window.reset_file_button.setEnabled(True)
    #     else:
    #         main_window.reset_file_button.setEnabled(False)
    
    
    def open_settings_dialog(self, main_window):
        # open settings dialog
        settings_dialog = SettingsDialog(main_window)
        settings_dialog.exec()