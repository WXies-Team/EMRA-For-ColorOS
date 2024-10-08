import os  # 引入 OS 模块，用于操作文件和目录
import glob  # 引入 glob 模块，用于搜索文件夹中的文件
import platform # 引入 platform 模块，用于读取设备信息
import shutil  # 导入 shutil 模块，用于复制、移动、删除文件和目录

# 获取当前脚本文件所在目录的绝对路径
src_dir = os.path.abspath(__file__)

# 在当前脚本文件所在目录下创建一个名为"output_apk"的子目录
dst_dir = os.path.join(src_dir, "output_apk")

# 在当前目录下搜索所有以".zip"为后缀的文件，并返回它们的文件路径
zip_files = glob.glob("*.zip")

# 在当前目录下搜索所有 "build.prop" 文件，并返回文件路径
for root, _, files in os.walk("."):
    if "build.prop" in files:
        src_path = os.path.join(root, "build.prop")
        dest_path = "./build.prop"
        
        if os.path.abspath(src_path) != os.path.abspath(dest_path):
            shutil.copy(src_path, dest_path)
        break

# 创建名为"output_apk"的目录（如果它不存在）
output_dir = "output_apk"

update_apk_folder = "update_apk"

update_apk_name_folder = "update_name_apk"

if not os.path.exists(update_apk_folder):
    os.makedirs(update_apk_folder)

if not os.path.exists(update_apk_name_folder):
    os.makedirs(update_apk_name_folder)

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# 获取名为"output_apk"目录中所有以".apk"为后缀的文件列表
apk_files = [f for f in os.listdir(output_dir) if f.endswith(".apk")]

# 外部工具路径
tools_path_mapping = {
                      ("Windows", "AMD64"): "./tools/Windows/AMD64/",
                      ("Linux", "x86_64"): "./tools/Linux/x86_64/",
                      ("Linux", "arm64"): "./tools/Linux/arm64/",
                      ("Darwin", "x86_64"): "./tools/Darwin/x86_64/",
                      ("Darwin", "arm64"): "./tools/Darwin/arm64/"
                     }
tools_path = tools_path_mapping.get((platform.system(), platform.machine()))

# 定义了两个字符串常量，分别用于指定排除 APK 的文件路径和 APK 版本号和名称的 JSON 文件路径
EXCLUDE_APK_PATH = "exclude_apk.txt"
APK_VERSION = "app_version.json"
APK_CODE = "app_code.json"
APK_APP_NAME = "app_name.json"
# 定义一个临时字典，用于存储版本名相同但版本号有所变更的 APK
APK_CODE_NAME = "app_code_name.json"

# 相关分区
partitions = [
              "my_product", 
              "my_stock", 
              "my_bigball", 
              "my_heytap", 
              "system_ext"
             ]
for image in partitions:
    pass     

# 需要删除的文件夹
files_to_delete = [
                   "payload.bin", 
                   "my_product.img", 
                   "my_stock.img", 
                   "my_bigball.img", 
                   "my_heytap.img", 
                   "system_ext.img", 
                   "app_code_name.json"
                  ]
folders_to_delete = [
                     "output_apk", 
                     "update_apk", 
                     "update_name_apk", 
                     "config", 
                     "my_heytap", 
                     "my_product", 
                     "my_stock", 
                     "system_ext", 
                     "my_bigball"
                    ]

# 获取信息
properties = {
              "ro.product.system.model": "设备名",
              "ro.build.oem.projects": "设备项目",
              "ro.vivo.os.build.display.id": "OS版本",
              "ro.system.build.version.release": "安卓版本",
              "ro.build.display.id": "软件版本号",
              "ro.build.date": "编译时间",
              "ro.build.version.security_patch": "安全补丁",
              "ro.vivo.device.type": "设备类型",
              "ro.system.build.id": "基线",
              "ro.system.build.fingerprint": "指纹",
              "ro.product.locale": "设备区域",
              "Build.BRAND": "设备平台","ro.vivo.hardware.version": "硬件版本"
             }
