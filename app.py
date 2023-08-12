from flask import Flask, render_template
import os
import pymysql


db = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456')
cursor = db.cursor()
# cur_path = os.path.dirname(__file__)
app = Flask(__name__, template_folder='./templates')


@app.route('/')
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

@app.route('/video')
def video_page():
    cursor.execute("""
        USE Myvideo;
    """)
    cursor.execute("""
        SELECT * FROM videoinfo;
    """)
    datalist = cursor.fetchall()
    return render_template('video.html', datalist=datalist)






if __name__ == '__main__':
    app.run(debug=True)



# 我们计划做一个视频网站。目前做好了简易的html，也将本地视频用ffmpeg做了segment，生成了一些ts文件和index文件。
# 想用flask和MySQL，该怎么做到前后端结合？怎么记录用户的上次的观看节点？请问后续工作还有那些？希望你能分点作答
# 1. 前后端结合：
# 首先，你可以使用Flask来处理前端和后端的请求和响应。在Flask中，你可以编写路由函数来处理不同的URL请求。
# 在前端，你可以使用HTML和CSS来设计页面布局和样式，并使用JavaScript来处理用户的交互行为和发送请求。
# 在后端，你可以使用Flask提供的模板引擎来渲染动态页面，并使用Flask提供的数据库扩展来连接和操作MySQL数据库。

# 2. 记录用户的上次观看节点：
# 为了记录用户的上次观看节点，你可以在数据库中创建一个名为"users"的表，用于存储用户的相关信息。该表可以包含用户的唯一标识符、用户名、密码等字段，以及一个额外的字段用于存储用户的上次观看节点。
# 当用户观看视频时，你可以使用JavaScript来发送请求，将用户当前观看的时间节点发送到服务器端。服务器端接收到请求后，可以更新数据库中对应用户的上次观看节点字段的值。
# 当用户再次打开该视频时，你可以使用Flask从数据库中获取用户的上次观看节点，并使用JavaScript来定位视频播放到该节点。

# 3. 后续工作：
# 除了实现前后端的结合和记录用户的上次观看节点外，你还可以考虑以下后续工作：
# - 视频上传和管理：设计一个用户上传视频的功能，以及后台管理系统来管理上传的视频文件。
# - 用户认证和权限管理：为用户提供注册和登录功能，并实现不同权限级别的用户访问控制。
# - 视频推荐：根据用户的观看历史记录和喜好，实现一个视频推荐系统，向用户推荐相关的视频。
# - 视频评论和分享：为用户提供评论和分享视频的功能，以增加用户的互动和社交性。
# - 视频搜索和标签分类：实现一个视频搜索功能，以及根据标签对视频进行分类和展示。
# - 异常处理和错误提示：在系统中加入适当的异常处理和错误提示机制，以提升用户体验和系统的稳定性。


# 参考资料
# https://blog.csdn.net/qq_36410795/article/details/107109514
# https://www.wuhancoder.com/blog/OtSxCkcztU.html





# 可以通过在index.html中设置不同的参数来标识不同的图片，然后在video.html中根据参数查询数据库获取对应的视频信息并进行播放。
# 首先，在index.html中的图片上设置不同的参数，例如可以添加一个data-video-id属性来表示视频的ID：
# <a href="video.html" data-video-id="1"><img src="image1.jpg"></a>
# <a href="video.html" data-video-id="2"><img src="image2.jpg"></a>
# <a href="video.html" data-video-id="3"><img src="image3.jpg"></a>
# 然后，在video.html中，使用JavaScript获取URL中的参数并发送到后端获取对应的视频信息：
# <script>
#   // 获取URL中的参数
#   function getParameterByName(name) {
#     var url = window.location.href;
#     name = name.replace(/[\[\]]/g, '\\$&');
#     var regex = new RegExp('[?&]' + name + '(=([^&#]*)|&|#|$)'),
#         results = regex.exec(url);
#     if (!results) return null;
#     if (!results[2]) return '';
#     return decodeURIComponent(results[2].replace(/\+/g, ' '));
#   }
#   // 获取视频ID参数
#   var videoId = getParameterByName('data-video-id');
#   // 发送视频ID到后端获取视频信息
#   // 可以使用Ajax请求，使用jQuery示例：
#   $.ajax({
#     url: '/get_video_info',
#     type: 'GET',
#     data: { videoId: videoId },
#     success: function(response) {
#       // 根据后端返回的视频信息进行播放操作
#       // ...
#     }
#   });
# </script>
# 在后端的Flask应用中，添加一个路由用于处理获取视频信息的请求：
# @app.route('/get_video_info', methods=['GET'])
# def get_video_info():
#     video_id = request.args.get('videoId')
#     # 根据video_id从数据库中查询视频信息
#     # ...
#     # 返回视频信息给前端
#     return jsonify(video_info)
# 在上述代码中，你需要根据自己的数据库结构和数据表设计来编写查询视频信息的代码。
# 最后，在Flask的路由中添加video.html的路由：
# @app.route('/video.html')
# def video():
#     return render_template('video.html')
# 这样，当用户点击index.html中的某个图片时，会跳转到video.html并带上对应的视频ID参数，video.html会根据参数发送请求到后端获取视频信息并进行播放。



# 视频网站中，点击一个视频进去后，链接会跟上一串id，那这时候html页面仅仅是视频资源不一样，其他都差不多
# 我认为不可能每一个视频都要去建一个html文件，请问具体怎么实现呢？
# flask怎么做到从一个html中用户点击的图片获取对应的id参数，然后利用这个参数再去render_template中给另一个html文件传入参数呢？