from PIL import Image
import os

# 設定來源與目標資料夾路徑
input_folder = 'path/to/your/jfif_folder'     # 請替換成你的 JFIF 資料夾路徑
output_folder = 'path/to/your/output_folder'    # 請替換成你希望存放轉換後檔案的資料夾

# 如果目標資料夾不存在，就建立它
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# 遍歷來源資料夾中的所有檔案
for filename in os.listdir(input_folder):
    if filename.lower().endswith('.jfif'):
        input_path = os.path.join(input_folder, filename)
        output_filename = os.path.splitext(filename)[0] + '.png'  # 更改檔案副檔名為 .png
        output_path = os.path.join(output_folder, output_filename)
        try:
            # 開啟 JFIF 檔案並轉存為 PNG
            with Image.open(input_path) as img:
                img.save(output_path, 'PNG')
            print(f"成功轉換: {filename} --> {output_filename}")
        except Exception as e:
            print(f"轉換檔案 {filename} 時發生錯誤: {e}")
