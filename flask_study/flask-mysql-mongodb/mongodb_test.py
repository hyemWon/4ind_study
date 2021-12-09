# mongoDB는 3가지로 구성된다 (Database, Collection, Document)
# Database : 컬렉션의 물리적 컨테이너. 하나의 데이터베이스에는 보통 여러개의 컬렉션을 가지고 있다.
# Collection : document의 그룹 (table과 개념이 유사)
# Document : 하나의 키(key)와 값(value)의 집합

import pymongo

username = ''
password = ''
ip_address = 'localhost'
# connection = pymongo.MongoClient()
# connection = pymongo.MongoClient('mongodb://%s:%s@%s' % (username, password, ip_address))
connection = pymongo.MongoClient('mongodb://%s' % (ip_address))
blog_session_db = connection.blog_session_db # db 가져오기
blog_ab = blog_session_db.blog_ab # collection


# mongodb를 한번 연결하면 해당 객체를 사용해서 CRUD 실행 가능
# 하지만 실제로는 mongodb가 다양한 원인으로 다운되거나 연결이 해제되는 경우가 있다. 이 경우 CRUD 에러남
# 그래서 연결된 객체가 아직 mongodb에 연결이 되어있는지 체크하는 방법 필요

# connection이 살아있느지 체크하는 별도의 명령어가 없다.
print(connection.admin.command('ismaster')) # mongodb 관련 정보 출력
print(connection.server_info()) 

# blog_ab.insert_one({'emailid': 'alrema96@naver.com'})

print(blog_ab.find_one({'emailid': 'alrema96@naver.com'}))

# print(blog_ab.delete_one({'emailid': 'alrema96@naver.com'}))

# print(blog_ab.find_one({'emailid': 'alrema96@naver.com'}))

blog_logs = blog_ab.find()
for log in blog_logs:
    print(log)