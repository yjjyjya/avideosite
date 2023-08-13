import traceback
import pymysql


class Database():
    def __init__(self):
        self.db = pymysql.connect(host='127.0.0.1', user='root', password='123456', port=3306)
        self.cursor = self.db.cursor()

    def reset(self):
        self.cursor.execute("""
            CREATE DATABASE IF NOT EXISTS Myvideo;
        """)
        self.cursor.execute("""
            USE Myvideo;
        """)
        self.cursor.execute("DROP TABLE IF EXISTS videoinfo;")
        statement = """
            CREATE TABLE `videoinfo` (
            `id` int NOT NULL PRIMARY KEY AUTO_INCREMENT,
            `type` varchar(255) NOT NULL,
            `videoname` varchar(255) NOT NULL,
            `date` varchar(255) NOT NULL,
            `picpath` varchar(255) NOT NULL,
            `videopath` varchar(255) NOT NULL)CHARSET=utf8;"""
        self.cursor.execute(statement)
        statement = """
            INSERT INTO `videoinfo` VALUES
            (default, '学习资源区', '杭州168元广式早茶自助,一笼接一笼香迷糊了!', '7-28', './static/picture/test.webp', 'None'),
            (default, '学习资源区', '瓦坎达放到现实，是什么样的存在？【司徒之脑洞】', '8-6', './static/picture/test.webp', 'None'),
            (default, '学习资源区', '我的目标是驱散所有黑暗~', '8-4', './static/picture/test.webp', 'None'),
            (default, '学习资源区', '张家界迷魂台', '直播', './static/picture/test.webp', 'https://gccncc.v.wscdns.com/gc/zjjmht_1/index.m3u8'),
            (default, '学习资源区', '张家界大峡谷', '直播', './static/picture/test.webp', 'https://gcalic.v.myalicdn.com/gc/hsxkssqdzrqj_1/index.m3u8'),
            (default, '学习资源区', '凤凰古城', '直播', './static/picture/test.webp', 'http://124.232.231.246:6610/000000001001/201600010006/index.m3u8'),
            (default, '动画区', '打工吧！魔王大人', '-', './static/picture/打工吧！魔王大人.webp', './static/video/20230811/0000_adc25796f822/index.m3u8'),
            (default, '动画区', '鬼灭之刃 刀匠村篇', '-', './static/picture/鬼灭之刃 刀匠村篇.webp', './static/video/20230811/0000_adc25796f822/index.m3u8'),
            (default, '动画区', '博人传', '-', './static/picture/博人传.webp', './static/video/20230811/0000_adc25796f822/index.m3u8'),
            (default, '动画区', '夏目友人帐', '-', './static/picture/夏目友人帐.webp', './static/video/20230811/0000_adc25796f822/index.m3u8'),
            (default, '动画区', '海绵宝宝', '-', './static/picture/海绵宝宝.webp', './static/video/20230811/0000_adc25796f822/index.m3u8');"""
        self.cursor.execute(statement)
        self.db.commit()

    def initialize(self):
        self.cursor.execute("""
            USE Myvideo;
        """)
        self.cursor.execute("""
            SELECT * FROM videoinfo;
        """)
        print(self.cursor.fetchall())
    
    def close(self):
        self.db.close()


if __name__ == '__main__':
    video_database = Database()
    video_database.reset()
    video_database.initialize()
    video_database.close()