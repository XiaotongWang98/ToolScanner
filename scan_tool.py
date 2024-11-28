import os
import fnmatch
import json

DESCRIPTION_FILE = "tool_descriptions.json"

def load_descriptions():
    """加载本地工具描述库"""
    if os.path.exists(DESCRIPTION_FILE):
        with open(DESCRIPTION_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    return {}

def save_descriptions(descriptions):
    """保存工具描述库"""
    with open(DESCRIPTION_FILE, "w", encoding="utf-8") as file:
        json.dump(descriptions, file, indent=4, ensure_ascii=False)

def get_file_info(file_name, descriptions):
    """
    获取工具描述信息
    :param file_name: 工具名称
    :param descriptions: 本地描述库
    :return: 描述信息和是否隐藏
    """
    tool_info = descriptions.get(file_name, {"description": "未知工具", "hidden": False})
    return tool_info.get("description", "未知工具"), tool_info.get("hidden", False)

def scan_tools(directories, descriptions, search_keyword=None):
    """
    扫描指定目录下的工具，支持模糊搜索，并与描述库匹配。
    :param directories: 要扫描的目录列表
    :param descriptions: 本地描述库
    :param search_keyword: 搜索关键字，模糊匹配
    :return: 工具清单
    """
    tool_list = []
    for directory in directories:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if fnmatch.fnmatch(file, "*.exe"):  # 搜索可执行文件
                    file_path = os.path.join(root, file)
                    description, hidden = get_file_info(file, descriptions)
                    if hidden:
                        continue  # 跳过隐藏工具
                    if search_keyword is None or search_keyword.lower() in file.lower():
                        tool_list.append({"name": file, "path": file_path, "description": description})
                        # 如果是未知工具，更新描述库
                        if file not in descriptions:
                            descriptions[file] = {"description": "未知工具", "hidden": False}
    return tool_list

def display_tools(tool_list):
    """
    显示工具清单
    """
    if not tool_list:
        print("没有找到符合条件的工具。")
    else:
        print(f"找到 {len(tool_list)} 个工具：\n")
        for idx, tool in enumerate(tool_list, 1):
            print(f"{idx}. 工具名称: {tool['name']}")
            print(f"   描述信息: {tool['description']}")
            print(f"   安装路径: {tool['path']}\n")

# 加载描述库
descriptions = load_descriptions()

# 指定要扫描的目录
directories_to_scan = [
    "D:/tools"
]

# 用户输入搜索关键字
search_keyword = input("请输入关键字（回车跳过）：").strip()

# 扫描并显示结果
print("\n正在扫描目录，请稍候...")
tools = scan_tools(directories_to_scan, descriptions, search_keyword)
display_tools(tools)

# 保存更新后的描述库
save_descriptions(descriptions)
input("按回车键退出...")
