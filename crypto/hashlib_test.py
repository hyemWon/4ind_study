# hashlib 모듈은 md5, sha256 등의 알고리즘으로 문자열을 해싱할때 사용하는 모듈이다.
# 입력한 비밀번호를 txt 파일에 저장하는 프로그램
# 비밀번호는 유추 및 복호화가 불가능한 sha256방식으로 해싱하여 저장한다.
# 이미 저장된 비밀번호 파일이 있을 경우에 기존 비밀번호를 입력받아 비밀번호가 일치할 경우에만 새로운 비밀번호를 저장

# import hashlib
#
# m = hashlib.sha256()
# # 문자열 해싱 - update에 전달하는 문자열은 바이트 문자열
# m.update('Life is too short'.encode('utf-8')) # 유니코드 문자열 > UTF-8 형식의 바이트 문자열로 변환
# # 해싱할 문자열을 추가하고 싶으면 update 함수를 추가로 호출
# m.update(', you need python.'.encode('utf-8'))
#
# # 해싱된 문자열 얻기
# print(m.digest()) # 해싱된 바이트 문자열 리턴
# print(m.hexdigest()) # 바이트 문자열을 16진수로 변환한 문자열 리턴
# # 해싱한 문자열을 원래의 문자열로 복수할 수 있는 방법은 없다.
# # 해싱은 단방향 암호화 알고리즘이기 때문이다.




import hashlib
import os

def check_passwd():
    if os.path.exists('passwd.txt'):
        before_passwd = input('기존 비밀번호를 입력하세요: ')
        m = hashlib.sha256()
        m.update(before_passwd.encode('utf-8'))
        with open('passwd.txt','r') as f:
            return m.hexdigest() == f.read()
    else:
        return True

if check_passwd():
    passwd = input('새로운 비밀번호를 입력하세요: ')
    with open('passwd.txt', 'r') as f:
        m = hashlib.sha256()
        m.update(passwd.encode('utf-8'))
        f.write(m.hexdigest())
else:
    print('비밀번호가 일치하지 않습니다.')
    
