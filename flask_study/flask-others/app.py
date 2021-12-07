# 파이썬 로그 라이브러리
# 로깅 정보는 로그의 레벨에 따라서 출력을 제한 할 수 있다
# DEBUG > INFO > WARNING > ERROR > Critical

import logging

# 파일로 남기기 위해 filename='test.log' 파라미터, 어느 로그까지 남길 것인지를 level로 설정 가능
logging.basicConfig(filename='test2.log', level=logging.ERROR)

# 로그를 남길 부분에 로그 레벨에 맞추어 출력해주면 해당 내용이 파일에 들어감
logging.debug("debug")
logging.info("info")
logging.warning("warning")
logging.error("error")
logging.critical("critical")




