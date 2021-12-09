import pymysql


db_conn = pymysql.connect(
    host='localhost',
    port=3306,
    user='hyem',
    passwd='helena',
    db='blog_db',
    charset='utf8'
)


blog_db_cursor = db_conn.cursor()
# print(blog_db_cursor)


# sql = '''
# CREATE TABLE user_info (
#     USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
#     USER_EMAIL VARCHAR(100) NOT NULL,
#     BLOG_ID CHAR(4),
#     PRIMARY KEY(USER_ID)
# );
# '''
# blog_db_cursor.execute(sql)
# db_conn.commit() # 데이터베이스를 변경하는 명령은 commit() 해주기 (영구적 반영)




# sql = 'DROP TABLE user_info;'
# blog_db_cursor.execute(sql)
# db_conn.commit()

# sql = 'SHOW TABLES;'
# print(blog_db_cursor.execute(sql))

# user_email = 'alrema96@naver.com'
# blog_id = 'A'

# sql = "INSERT INTO user_info (USER_EMAIL, BLOG_ID) VALUES ('%s', '%s')" % (str(user_email), str(blog_id))
# blog_db_cursor.execute(sql)
# db_conn.commit()

sql = "SELECT * FROM user_info"
blog_db_cursor.execute(sql)
results = blog_db_cursor.fetchall()
for result in results:
    print(result, type(result))

blog_db_cursor.close()