这是一个基于Python和Pygame实现的五子棋游戏，具有以下特点：

人机对战模式

智能AI对手

重新开始游戏功能

最后落子位置标记

胜负判定

功能特性
🎮 传统15×15五子棋棋盘

🤖 具备简单AI逻辑的电脑对手

🖱️ 鼠标点击操作

🔄 一键重新开始游戏

🏆 自动判定胜负

🎨 简洁美观的界面

运行要求
Python 3.6+

Pygame 2.0+

安装步骤
克隆仓库或下载源代码

复制
git clone https://github.com/yourusername/gomoku.git
cd gomoku
安装依赖

复制
pip install pygame numpy
运行游戏

复制
python main.py
游戏操作说明
鼠标点击棋盘放置白棋

电脑会自动下黑棋

点击"重新开始"按钮重置游戏

游戏会自动判定五子连珠情况

项目结构
复制
gomoku/

├── main.py          # 主程序入口

├── init.py          # 游戏初始化和常量定义

├── draw.py          # 绘制游戏界面

├── logic.py         # 游戏逻辑和AI实现

├── README.md        # 说明文档

└── requirements.txt # 依赖列表
开发者

南京邮电大学-鲁健

许可证

MIT License

未来计划

1.增加难度选择

2.添加双人对战模式

3.实现悔棋功能

4.添加音效和动画效果

5.支持保存和加载游戏

贡献指南
欢迎提交Issue和Pull Request！

