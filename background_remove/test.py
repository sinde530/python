# rembg module 사용 설명 github 참조 페이지
# https://github.com/danielgatis/rembg

# Code #1
# 개별 파일 열어 배경 제거하고 저장하기
from rembg import remove
from PIL import Image

def main():
    input_file = './t4.jpeg'
    output_file = './t4_output.png'
    input = Image.open(input_file)
    output = remove(input)
    output.save(output_file)


# Code #2
# 폴더내 여러개 파일 모두 배경 투명하게 처리하기
# from pathlib import Path
# from rembg import remove, new_session

# def main():
#     session = new_session()

#     for file in Path('./image').glob('*.png'):
#         input_path = str(file)
#         output_path = str(file.parent / (file.stem + "_out.png"))

#         with open(input_path, 'rb') as i:
#             with open(output_path, 'wb') as o:
#                 input = i.read()
#                 output = remove(input, session=session)
#                 o.write(output)


# main 함수 로딩부
if __name__ == '__main__':
    main()
