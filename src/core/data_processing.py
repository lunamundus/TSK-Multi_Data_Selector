import os
import pandas as pd

def find_header_row(file_path):
    # 파일을 읽어 데이터의 헤더가 있는 행을 찾는 함수
    with open(file_path, 'r') as file:
        for i, line in enumerate(file):
            # 헤더를 찾기 위한 로직 구현
            # 헤더에 무조건 포함하고 있는 칼럼 이름으로 찾기 (ex. No, Date, Time)
            if "No" in line and " Date" in line and " Time" in line:
                return i
    return 0 # 헤더를 찾지 못하면 0 반환


def save_dataframe_to_excel(file_dir, file_name, selected_dataframe):
    # 데이터프레임을 엑셀 파일로 저장하는 함수
    try:
        output_file_path = os.path.join(file_dir, f"{file_name}_selected.xlsx")
        selected_dataframe.to_excel(output_file_path, index=False)
        return f"데이터가 성공적으로 저장되었습니다: {output_file_path}"
    except Exception as err:
        return f"저장 중 오류가 발생했습니다: {err}"


def data_processing(file_path):
    try:
        # 파일 존재 여부 확인
        if not os.path.exists(file_path):
            return f"ERROR 1: {file_path}에서 파일을 찾을 수 없습니다."

        header_row = find_header_row(file_path)
        skin_temp_dataframe = pd.read_csv(file_path, skiprows=header_row)
        
        # 파일 이름 추출
        file_name = os.path.splitext(os.path.basename(file_path))[0]
        file_dir = os.path.dirname(file_path)
        
        # 추출하고 싶은 칼럼 정의
        selected_columns = ["No", " Date", " Time",  # 날짜 및 시간
                            " A12", " A13", " A23",  # 가슴, 복부, 머리
                            " A31", " A32", " A33", " A34",  # 등
                            " A41", " A42", " A44",  # 오른손, 오른전완, 오른상완
                            " A51", " A52", " A53",  # 왼쪽전완, 왼손, 왼쪽상완
                            " B14", " B22", " B24",  # 오른허벅지, 오른발, 오른종아리
                            " B33", " B42", " B43", " Event"]  # 왼쪽허벅지, 왼발, 왼쪽종아리
        
        # 선택된 칼럼 추출
        selected_skin_temp_dataframe = skin_temp_dataframe[selected_columns]
        
        return file_name, file_dir, selected_skin_temp_dataframe

    except Exception as err:
        return f"데이터 처리 과정에서 오류가 발생했습니다: {err}"