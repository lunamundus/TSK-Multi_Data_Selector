import os
import json
import ctypes

from PySide6.QtWidgets import QDialog, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QCheckBox, QMessageBox

class SettingsDialog(QDialog):
    SETTINGS_PATH = os.path.join(os.getcwd(), 'settings') # 프로그램 디렉토리에 settings 폴더 사용
    SETTINGS_FILE = os.path.join(SETTINGS_PATH, "settings.conf") # 확장자 없는 파일 사용
    
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("환경설정")
        
        self.resize(400, 300)
        self.setup_ui()
        self.load_settings() # 이전 설정 파일 불러오기
        self.hide_settings_folder() # 폴더 숨김 설정
        
        
    def setup_ui(self):
        # main layout
        settings_layout = QVBoxLayout()
        
        self.set_option_label_1 = QLabel("저장할 센서 번호 선택")
        settings_layout.addWidget(self.set_option_label_1)
        
        # sensor nodes information
        nodes = {
            'A1': ['A11', 'A12', 'A13', 'A14'],
            'A2': ['A21', 'A22', 'A23', 'A24'],
            'A3': ['A31', 'A32', 'A33', 'A34'],
            'A4': ['A41', 'A42', 'A43', 'A44'],
            'A5': ['A51', 'A52', 'A53', 'A54'],
            'B1': ['B11', 'B12', 'B13', 'B14'],
            'B2': ['B21', 'B22', 'B23', 'B24'],
            'B3': ['B31', 'B32', 'B33', 'B34'],
            'B4': ['B41', 'B42', 'B43', 'B44']
        }
        
        # create and add sensor layout
        sensor_layouts = self.create_sensor_layouts(nodes)
        for layout in sensor_layouts:
            settings_layout.addLayout(layout)
            
        # save and cancel button
        save_and_cancel_button_layout = QHBoxLayout()
        self.save_button = QPushButton("저장")
        self.save_button.setFixedHeight(30)
        self.save_button.clicked.connect(self.setting_save)
        self.cancel_button = QPushButton("취소")
        self.cancel_button.setFixedHeight(30)
        self.cancel_button.clicked.connect(self.reject)
        save_and_cancel_button_layout.addWidget(self.save_button)
        save_and_cancel_button_layout.addWidget(self.cancel_button)
        
        settings_layout.addLayout(save_and_cancel_button_layout)
            
        self.setLayout(settings_layout)
        
    
    def setting_save(self):
        settings = {
            checkbox.objectName(): checkbox.isChecked()
            for checkbox in self.findChildren(QCheckBox)
        }
        
        # 설정 파일 디렉토리 생성
        os.makedirs(self.SETTINGS_PATH, exist_ok=True)
        
        # JSON 파일로 저장
        with open(self.SETTINGS_FILE, "w") as f:
            json.dump(settings, f, indent=4)
            
        # 숨김 파일 속성 설정 (Windows 환경)
        if os.name == 'nt': # Windows에서만 적용
            ctypes.windll.kernel32.SetFileAttributesW(self.SETTINGS_FILE, 2) # FILE_ATTRIBUTE_HIDDEN
            
        QMessageBox().information(self, "정보", "설정이 저장되었습니다.")
        self.accept()
    
    
    def load_settings(self):
        try:
            with open(self.SETTINGS_FILE, "r") as f:
                settings = json.load(f)
                
            for name, checked in settings.items():
                checkbox = getattr(self, name, None)
                if checkbox:
                    checkbox.setChecked(checked)
        except FileNotFoundError:
            QMessageBox.warning(self, "경고", "설정 파일을 찾을 수 없습니다. 기본 설정을 사용합니다.")
    
    
    def hide_settings_folder(self):
        # 폴더 숨김 속성 설정 (windows 환경)
        if os.name == 'nt':
            ctypes.windll.kernel32.SetFileAttributesW(self.SETTINGS_PATH, 2)
    
    
    def create_sensor_layouts(self, nodes):
        """
        * INFO
        * 주어진 센서 노드 정보를 바탕으로 UI 레이아웃을 생성하여 반환
        """
        sensor_layouts = []
        current_layout = QHBoxLayout()
        
        for idx, (node_name, sensors) in enumerate(nodes.items()):
            node_layout = QVBoxLayout()
            node_label = QLabel(f"{node_name} 노드")
            node_layout.addWidget(node_label)
            
            # create checkbox each node
            for sensor in sensors:
                checkbox = QCheckBox(f"{sensor}")
                checkbox.setObjectName(f" {sensor}")
                node_layout.addWidget(checkbox)
                
                # set instant variable
                setattr(self, checkbox.objectName(), checkbox)
            
            # 레이아웃 추가 처리
            current_layout.addLayout(node_layout)
            if (idx + 1) % 3 == 0:
                sensor_layouts.append(current_layout)
                current_layout = QHBoxLayout()
                
        # add last line
        if current_layout.count() > 0:
            sensor_layouts.append(current_layout)
        
        return sensor_layouts