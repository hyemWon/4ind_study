# pickle 파일 열기
# 암호화 잘 되었는지 확인

import pickle
with open('/home/fourind/py36/YOLOX/archive_c/data.pkl', 'rb') as f:
    data = pickle.load(f)
print(data)

with open('/home/fourind/py36/YOLOX/archive/data.pkl', 'rb') as f:
    data = pickle.load(f)
# print(data)