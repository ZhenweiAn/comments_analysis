我们的代码爬取了网易云音乐评论和作家作品，使用词云和情感分析做了分析

环境配置:
    pyltp
    pymysql
    paddlehub
    beautifulsoup
    requests
    selenium
       
代码运行：
    首先进入music_163爬取评论代码：
        执行sql.py创建数据库
        执行artists.py爬取歌手
        执行music_by_artist.py 爬取歌曲
        执行comments_by_music.py 爬取评论
    进入literature爬取作家作品:
        执行jinyong.py,zhangailing.py
    进行分析
    执行cut_test.py 切词
    执行word_cloud.py生成词云
    执行sentiment.py进行情感分析