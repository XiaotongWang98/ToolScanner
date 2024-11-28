# ToolScanner

ToolScanner 是一个实用工具管理器，旨在帮助用户扫描系统中安装的小工具（可执行文件），并提供清晰的描述和搜索功能。该项目支持通过本地描述库对工具进行管理，同时允许用户隐藏不必要的工具条目。

------

## **功能**

- **工具扫描**：自动扫描指定目录中的所有 `.exe` 文件。
- **描述管理**：通过本地 JSON 文件记录工具的描述信息，并支持自动更新。
- **隐藏无用工具**：支持在描述库中标记隐藏不需要显示的工具。
- **模糊搜索**：通过关键字查找相关工具。
- **自动扩展**：扫描到的新工具会自动加入描述库，初始标记为“未知工具”。

------

## **项目结构**

```tex
ToolScanner/
│
├── build/                  # 打包过程中的中间文件，可忽略
├── scan_tool.py            # 源代码
├── tool_descriptions.json  # 本地工具描述库，管理工具描述和显示设置
├── ToolScanner.exe         # 打包后的可执行文件
├── ToolScanner.spec        # PyInstaller 配置文件
└── README.md               # 项目说明文档
```

------

## **安装和运行**

### **运行方式 1：直接运行可执行文件**

1. 双击 `ToolScanner.exe`。
2. 程序会扫描预定义的目录，并显示工具清单。

### **运行方式 2：通过 Python 脚本**

如果需要修改代码或扩展功能，可以直接运行源代码：

1. 确保本地安装了 Python 3.x 和相关依赖库。

2. 安装 `PyInstaller`（可选，用于打包）：

   ```bash
   pip install pyinstaller
   ```

3. 运行脚本：

   ```bash
   python scan_tool.py
   ```

------

## **目录配置**

工具扫描的默认目录为：

- `D:/tools`

你可以通过编辑 `scan_tool.py` 中的 `directories_to_scan` 修改扫描目录。

------

## **本地工具描述库**

工具描述信息存储在 `tool_descriptions.json` 文件中，结构如下：

```json
{
    "工具名称.exe": {
        "description": "工具的功能描述",
        "hidden": false
    }
}
```

### **字段说明**

- `description`：工具的功能描述，可手动更新。
- `hidden`：设置为 `true` 时，工具将不会显示在扫描结果中。

------

## **使用示例**

运行 `ToolScanner.exe` 后，程序输出如下：

```javascript
找到 3 个工具：

1. 工具名称: youtube-dl.exe
   描述信息: 在线视频下载工具
   安装路径: D:/常用工具/youtube-dl.exe

2. 工具名称: ShareX.exe
   描述信息: 屏幕捕获、分享和生产力工具
   安装路径: C:/Program Files/ShareX/ShareX.exe

3. 工具名称: ffmpeg.exe
   描述信息: 多媒体处理工具（视频转码、音频编辑）
   安装路径: C:/Program Files/FFmpeg/ffmpeg.exe
```

------

## **定制化**

1. 添加描述：
   - 编辑 `tool_descriptions.json`，为工具添加或更新描述信息。
2. 隐藏工具：
   - 将 `hidden` 设置为 `true`，程序扫描时将忽略该工具。
3. 更改扫描目录：
   - 修改 `scan_tool.py` 中的 `directories_to_scan` 列表。

------

## **未来扩展**

- **分类功能**：根据工具类型（如下载、开发、编辑）进行分类管理。
- **自动生成报告**：将扫描结果导出为 HTML 或 CSV 文件。
- **图形界面**：提供更直观的用户界面以增强用户体验。

------

## **打包脚本**

如果需要重新生成可执行文件，运行以下命令：

```bash
pyinstaller --onefile --name "ToolScanner" scan_tool.py
```

------

## **许可证**

本项目采用 MIT 开源许可证，详情请参阅 `LICENSE` 文件。