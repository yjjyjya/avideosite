import hashlib
import os
import datetime
import subprocess


# 生成指定位数的哈希摘要
def generate_digest(data, num_bits=256):
    sha_hash = hashlib.sha256()
    sha_hash.update(data)
    digest = sha_hash.hexdigest()
    return digest[:num_bits // 4]  # Convert bits to characters

# 生成和保存TS文件及其摘要
def generate_and_save_ts_file(ts_folder, ts_data, ts_filename):
    with open(ts_filename, "wb") as ts_file:
        ts_file.write(ts_data)
  
# 获取当前日期字符串
current_date = datetime.datetime.now().strftime("%Y%m%d")

# 计算日期的哈希值
date_hash = generate_digest(current_date.encode("utf-8"), num_bits=12 * 4)

# 创建日期子文件夹
date_folder = os.path.join(current_date)
os.makedirs(date_folder, exist_ok=True)

# 查找已经创建的文件夹，确定起始序号
existing_folders = [folder for folder in os.listdir(date_folder) if os.path.isdir(os.path.join(date_folder, folder))]
if existing_folders:
    last_folder_number = max(int(folder[:4]) for folder in existing_folders)
else:
    last_folder_number = -1

# 创建新的文件夹
new_folder_number = last_folder_number + 1
new_folder_name = f"{new_folder_number:04d}_{date_hash}"
new_folder_path = os.path.join(date_folder, new_folder_name)
os.makedirs(new_folder_path)

# 封装分割 MP4 文件为 TS 的函数
def split_mp4_to_ts(input_mp4, output_folder, segment_time = "10"):

    folder_and_index = f"{new_folder_number:04d}_{current_date}"
    folder_and_index_hash = generate_digest(folder_and_index.encode("utf-8"), num_bits=12 * 4)

    output_template = os.path.join(new_folder_path, f"{folder_and_index_hash}_%06d.ts")    #ts文件名的模板

    ffmpeg_command = [
        "ffmpeg",
        "-i", input_mp4,
        "-c:v", "copy",
        "-c:a", "copy",
        "-map", "0",
        "-f", "segment",
        "-segment_time", segment_time,  # 每个 TS 文件的时长（秒）
        "-segment_list", os.path.join(output_folder, "index.m3u8"),
        "-segment_list_type", "m3u8",
        output_template
    ]
    
    subprocess.run(ffmpeg_command)

# 执行分割 MP4 文件为 TS
# split_mp4_to_ts("c1.mp4", new_folder_path)
split_mp4_to_ts("D:\\jupyterproject\\linshao\\视频网站\\project_flask\\static\\video\\nahida.mp4", new_folder_path)

print("TS files created successfully in the", new_folder_path, "folder.")



# -i：指定输入文件（input_mp4）。
# -c:v：指定视频编解码器，在此处为"copy"，表示直接复制原始视频流。
# -c:a：指定音频编解码器，在此处为"copy"，表示直接复制原始音频流。
# -map：指定输入文件（0表示第一个输入文件）。
# -f：指定输出格式（segment表示切片文件）。
# -segment_time：指定每个TS文件的时长（以秒为单位）。
# -segment_list：指定生成的m3u8文件的路径和文件名。
# -segment_list_type：指定生成的m3u8文件的类型，此处为m3u8。
# output_template：指定生成的切片文件名的模板，使用%06d来表示每个TS文件的编号，输出的切片文件以此命名，并保存在new_folder_path文件夹中。