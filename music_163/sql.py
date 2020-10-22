"""
一般 Python 用于连接 MySQL 的工具：pymysql
"""
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='asd123456',
                             db='wangyimusic',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


def create_tables():
    with connection.cursor() as cursor:
        sql = "DROP TABLE IF EXISTS comments"
        cursor.execute(sql)
        sql = "DROP TABLE IF EXISTS musics"
        cursor.execute(sql)
        sql = "DROP TABLE IF EXISTS artists"
        cursor.execute(sql)

        sql = '''
              CREATE TABLE comments(
              COMMENTS TEXT NOT NULL, 
              MUSIC_ID VARCHAR(100))ENGINE=InnoDB DEFAULT CHARSET=UTF8MB3'''
        cursor.execute(sql)

        sql = '''
              CREATE TABLE musics(
              MUSIC_ID VARCHAR(100) NOT NULL,
              MUSIC_NAME VARCHAR(100) NOT NULL,
              ARTIST_ID VARCHAR(100) NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB3'''
        cursor.execute(sql)

        sql = '''
              CREATE TABLE artists(
              ARTIST_ID VARCHAR(100) NOT NULL,
              ARTIST_NAME VARCHAR(100) NOT NULL)ENGINE=InnoDB DEFAULT CHARSET=UTF8MB3'''
        cursor.execute(sql)

# 保存评论
def insert_comments(music_id, comments):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `comments` (`MUSIC_ID`, `COMMENTS`) VALUES (%s, %s)"
        cursor.execute(sql, (music_id, comments))
    connection.commit()


# 保存音乐
def insert_music(music_id, music_name, ARTIST_ID):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `musics` (`MUSIC_ID`, `MUSIC_NAME`, `ARTIST_ID`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, music_name, album_id))
    connection.commit()


# 保存专辑
def insert_album(album_id, artist_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `albums` (`ALBUM_ID`, `ARTIST_ID`) VALUES (%s, %s)"
        cursor.execute(sql, (album_id, artist_id))
    connection.commit()


# 保存歌手
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


# 获取所有歌手的 ID
def get_all_artist():
    with connection.cursor() as cursor:
        sql = "SELECT `ARTIST_ID` FROM `artists` ORDER BY ARTIST_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有专辑的 ID
def get_all_album():
    with connection.cursor() as cursor:
        sql = "SELECT `ALBUM_ID` FROM `albums` ORDER BY ALBUM_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取所有音乐的 ID
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取前一半音乐的 ID
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取后一半音乐的 ID
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `MUSIC_ID` FROM `musics` ORDER BY MUSIC_ID LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()


if __name__ == "main":
    create_tables()
