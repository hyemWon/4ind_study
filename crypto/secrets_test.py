# secretes 모듈은 난수를 생성할 때 사용하는 모듈
# 16진수 문자로 구성된 32자리의 난수 문자열 생성

import secrets

# secrets.token_hex(nbytes) : 바이트 수 (1바이트는 2개의 16진수 문자열로 변환)
key = secrets.token_hex(16) # 32자리 난수 문자열
print(key)



