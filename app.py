from flask import Flask, render_template
import os
import pymysql


db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456')
cursor = db.cursor()
# cur_path = os.path.dirname(__file__)
app = Flask(
    __name__,
    template_folder='./templates',
    static_folder='static',
    static_url_path='/static',
)


@app.route('/index')
def home():
    cursor.execute("""
        USE Myvideo;
    """)
    cursor.execute("""
        SELECT * FROM videoinfo;
    """)
    datalist = cursor.fetchall()
    # print(datalist)
    return render_template('index.html', datalist=datalist)

@app.route('/video/<int:video_id>')
def video_page(video_id):
    cursor.execute("""
        USE Myvideo;
    """)
    cursor.execute(f"""
        SELECT * FROM videoinfo
        WHERE id={video_id};
    """)
    videodata = cursor.fetchall()
    # print(videodata)
    return render_template('video_detail.html', videodata=videodata)






if __name__ == '__main__':
    app.run(debug=True)


# 参考资料
# https://blog.csdn.net/qq_36410795/article/details/107109514
# https://www.wuhancoder.com/blog/OtSxCkcztU.html