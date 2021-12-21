import zipfile
from zipfile import *
import os
import glob

# extractall(압축해제할 파일명, 압축해제할 경로)
# file_path = '/home/fourind/py36/YOLOX/result'
# zip_file = zipfile.ZipFile('/home/fourind/py36/YOLOX/yolox_s.pth') # 압축해제 할 폴더
# zip_file.extractall(file_path) # 해제 경로


# import shutil
# shutil.make_archive('/home/fourind/py36/YOLOX/result', 'pth', '/home/fourind/py36/YOLOX/result')


# 디렉터리 위치 변경
# os.chdir('/home/fourind/py36/YOLOX/result')
# with zipfile.ZipFile('../result.pth', 'w') as f:
#     for fname in glob.glob('archive/*'):
#         f.write(fname)

os.chdir('/home/fourind/py36/YOLOX')

zip_file = zipfile.ZipFile('result1.pth', 'r')
# print(zip_file.extract('archive/data.pkl'))
# zip_file.close()
# print(zip_file)









# with zipfile.ZipFile('result.pth', 'a') as f:
#     f.write('requirements.txt')

