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
print(blog_db_cursor)

sql = 'SHOW TABLES;'
print(blog_db_cursor.execute(sql))


sql = '''
CREATE TABLE user_info (
    USER_ID INT UNSIGNED NOT NULL AUTO_INCREMENT,
    USER_EMAIL VARCHAR(100) NOT NULL,
    BLOG_ID CHAR(4),
    PRIMARY KEY(USER_ID)
);
'''
blog_db_cursor.execute(sql)
db_conn.commit()

sql = 'SHOW TABLES;'
print(blog_db_cursor.execute(sql))