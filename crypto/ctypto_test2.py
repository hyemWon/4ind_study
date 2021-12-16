# AES 대칭키 암호
# 파이썬에서 AES를 사용하기 위해서 pycrypto 모듈을 설치
# 사용전 SHA 해시를 사용해 초기화 벡터와 키를 sha로 해싱 후 키로 사용할 것
# 해시는 파이썬 자체 라이브러리 hashlib이 있으나 pycrypto를 이용해서 사용할 것

# 해시
# 빠른 검색을 위해 사용되었다. 계산의 역상이 어렵기 때문에 암호 및 보안에도 이용되다.
# 주로 MD, SHA 계열이 있고, SHA는 버전에 따라서 알고리즘이 다른 경우가 있다.
# 암호로 사용되지 않는 해시도 있다.
# MD5의 경우 이미 해시가 풀려 암호학적으로 이용하기에는 안전하지 않은 해시이다.
# 대부분 느려도 안전한 SHA를 사용하며 이회 다양한 해시 알고리즘이 사용된다.
# 본 예제에서는 SHA256 사용

# from Crypto.Hash import SHA256
# from Crypto.Cipher import AES

# hash = SHA256.new() # sha256 해시 객체 생성

# data = ''
# hash.update(data)  # 해시 데이터 적용
# hash_value = hash.digest() # 해시값(hash value) 반환

# AES.new(key, mode, iv) 
# key : key 값 AES는 128 192 256의 키 길이를 사용할 수 있다.
# mode : 암호 mode, 기본 값이 ECB 모드이다.
# iv : 초기화 벡터를 입력하는 인수 ECB모드와 CTR모드는 사용되지 않는다.

# struct 모듈
# pack, unpack, calcsize 등의 기능 있음.
# 정수, 실수, 문자열을 encode한 것을 bytes 객체로 변환하거나, 반대로 bytes 객체에서 이것을 빼낸다.
# bytes 객체로 변환하려면 서식 지정 문자와 변환할 값은 pack함수에 넘기면 된다.


from Crypto.Hash import SAH256
from Crypto.Cipher import AES
from os import path
from struct import pach, unpack, calcsize


