import hashlib
import os
import datetime

# 生成指定位数的哈希摘要
def generate_digest(data, num_bits=256):
    sha_hash = hashlib.sha256()
    sha_hash.update(data)
    digest = sha_hash.hexdigest()
    return digest[:num_bits // 4]  # Convert bits to characters

# 创建索引文件
def create_index_file(new_folder_path, digests):
    index_content = "#EXTM3U\n"
    for i, digest in enumerate(digests, start=1):
        index_content += f"#EXTINF:10.0,\n{digest}\n"
    index_content += "#EXT-X-ENDLIST\n"
    index_file_path = os.path.join(new_folder_path, "index.m3u8")
    with open(index_file_path, "w") as index_file:
        index_file.write(index_content)

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

# 生成和保存TS文件
num_files = 3
ts_filenames = []
for i in range(num_files):
    folder_and_index = f"{new_folder_number:04d}_{current_date}"
    folder_and_index_hash = generate_digest(folder_and_index.encode("utf-8"), num_bits=12 * 4)

    ts_filename = os.path.join(new_folder_path, f"{folder_and_index_hash}_{i + 1:06d}.ts")
    ts_filenames.append(ts_filename)

    ts_data = f"This is the content of segment {i}".encode("utf-8")
    with open(ts_filename, "wb") as ts_file:
        ts_file.write(ts_data)

# # 生成和保存TS文件及其摘要
# num_files = 3
# digests = []
# for i in range(num_files):
#     ts_data = f"This is the content of segment {i}".encode("utf-8")
#     ts_digest = generate_digest(ts_data, num_bits=12 * 4)
#     ts_filename = ts_filenames[i]
#     generate_and_save_ts_file(new_folder_path, ts_data, ts_filename)
#     digests.append(ts_digest)

# 创建索引文件并保存
# create_index_file(new_folder_path, ts_digest)
create_index_file(new_folder_path, ts_filenames)

print("TS files created successfully in the", new_folder_path, "folder.")
