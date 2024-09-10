import sys
from PySide6.QtWidgets import QApplication
from PySide6.QtWidgets import QMainWindow, QVBoxLayout, QWidget, QListWidget, QFileDialog, QLabel, QPushButton, QStackedLayout
from PySide6.QtCore import Qt
# from handlers.qt_event_handlers import DragDropHandlers

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Skin Temperature Data Selector for TSK Multi")
        self.resize(600, 400)

        self.setup_ui()
        self.setAcceptDrops(True)
        # self.qt_event_handlers = DragDropHandlers(self.file_list_widget)

    def setup_ui(self):
        main_widget = QWidget()
        main_layout = QVBoxLayout()

        # 파일 추가 버튼
        add_file_button = QPushButton("파일 추가")
        add_file_button.clicked.connect(self.add_file)
        main_layout.addWidget(add_file_button)

        # 파일 리스트 위젯과 안내 레이블을 겹쳐서 배치할 스택 레이아웃
        stacked_layout = QStackedLayout()

        # 파일 리스트 위젯
        self.file_list_widget = QListWidget()
        self.file_list_widget.setAcceptDrops(True)
        stacked_layout.addWidget(self.file_list_widget)

        # 안내 레이블
        self.empty_list_label = QLabel("파일을 드래그앤드랍 하거나 파일 추가 버튼을 눌러 파일을 추가해주세요.")
        self.empty_list_label.setAlignment(Qt.AlignCenter)
        self.empty_list_label.setStyleSheet("color: gray; font-size: 16px;")
        stacked_layout.addWidget(self.empty_list_label)

        # 스택 레이아웃을 메인 레이아웃에 추가
        main_layout.addLayout(stacked_layout)
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

        # 아이템 변화 감지
        self.file_list_widget.model().rowsInserted.connect(self.update_empty_label)
        self.file_list_widget.model().rowsRemoved.connect(self.update_empty_label)

        # 초기 상태 업데이트
        self.update_empty_label()

    def add_file(self):
        file_dialog = QFileDialog()
        file_path, _ = file_dialog.getOpenFileName(self, "파일 선택", "", "All Files (*.*)")
        
        if file_path:
            self.file_list_widget.addItem(file_path)

    # def dragEnterEvent(self, event):
    #     self.qt_event_handlers.dragEnterEvent(event)

    # def dropEvent(self, event):
    #     self.qt_event_handlers.dropEvent(event)
    #     self.update_empty_label()

    def update_empty_label(self):
        # 리스트에 아이템이 없으면 안내 레이블을 보이게 하고, 아이템이 있으면 숨김
        if self.file_list_widget.count() == 0:
            self.empty_list_label.raise_()  # 레이블을 맨 위로 올림
            self.empty_list_label.setVisible(True)
        else:
            self.empty_list_label.setVisible(False)


def main():
    app = QApplication(sys.argv)
    
    window = MainWindow()
    window.show()
    
    sys.exit(app.exec())
    
if __name__ == "__main__":
    main()