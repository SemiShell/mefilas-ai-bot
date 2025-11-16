# 美菲拉斯评估员 - Telegram Bot

![Mefilas](https://cdnb.artstation.com/p/assets/images/images/050/218/725/large/fuji-asset.jpg)

> "应诸君之邀前来。我的口头禅是，万物皆有其价。"

一个基于《新·奥特曼》中经典角色**美菲拉斯星人**的Telegram Bot。他是一位彬彬有礼却又极度傲慢的宇宙商人，会以黑色幽默的口吻对你的群组成员和聊天内容进行“价值评估”。

他不是来破坏的，他只是来估值的。

---

## ✨ 功能特性

*   **🧐 绅士般的价值评估 (`/assess`)**
    *   用户发送 `/assess` 或 `/评估我`，Bot会抓取该用户的公开信息（昵称、用户名、头像状态），并生成一份充满商业气息和轻蔑的“价值评估报告”。

*   **🎨 冷酷的艺术评论家 (图片自动评分)**
    *   无需指令，Bot会自动对群聊中出现的**每一张图片**进行打分和点评。评分标准极其苛- 刻，评语充满外星高等文明的审美偏见。

*   **🤫 潜伏观察与被动吐槽 (关键词触发)**
    *   Bot会像一个真正的观察者一样潜伏在群里。当检测到特定关键词（如“价值”、“奥特曼”、“暴力”、“地球”等）时，会以较低概率触发，发表他独特的见解。

*   **🤖 AI加持的深度对话 (@机器人)**
    *   在群聊中 **@机器人** 并提问，即可激活由 **Google Gemini AI** 驱动的对话模式。AI被注入了完整的美菲拉斯人格，他会用那套优雅、傲慢且充满商业哲学的口吻回应你的一切问题。

---

## 🚀 部署指南

你可以选择两种方式部署此Bot：**使用Docker（推荐）**或**手动部署**。

### 🐳 部署方式一：使用Docker（推荐）

这是最简单、最快捷的部署方式，推荐在任何支持Docker的服务器（如Ubuntu, CentOS等）上使用。

#### 步骤 1: 准备服务器

首先，在你的服务器上安装 `Git`, `Docker` 和 `Docker Compose`。

```bash
# 以Ubuntu为例
sudo apt update && sudo apt upgrade -y
sudo apt install git docker.io docker-compose-plugin -y

# （可选但推荐）将当前用户添加到docker组，以避免每次都输入sudo
# 注意：执行后需要重新登录SSH才能生效
sudo usermod -aG docker $USER
```

#### 步骤 2: 克隆仓库并配置

```bash
# 克隆本仓库
git clone https://github.com/SemiShell/mefilas-ai-bot.git

# 进入项目目录
cd mefilas-ai-bot

# 创建并编辑环境配置文件
nano .env
```

在打开的编辑器中，粘贴你的API密钥，格式如下：

```ini
TELEGRAM_TOKEN=123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11
GOOGLE_API_KEY=AIzaSyB...your...google...api...key...
```
按 `Ctrl+X`, `Y`, `Enter` 保存并退出。

#### 步骤 3: 一键启动！

在项目根目录下，执行以下命令：

```bash
docker compose up -d
```
Docker Compose会自动构建镜像并在后台启动容器。第一次启动会需要一些时间来下载和构建。

**恭喜，你的Bot已成功部署！**

#### 管理你的Docker Bot

*   **查看实时日志:** `docker compose logs -f`
*   **停止Bot:** `docker compose down`
*   **重启Bot:** `docker compose restart`
*   **更新代码后部署:**
    ```bash
    git pull # 拉取最新代码
    docker compose up -d --build # 重新构建并启动
    ```

---

### 🛠️ 部署方式二：手动部署 (适用于Ubuntu 24.04)

如果你不想使用Docker，可以按照传统方式进行部署。

#### 步骤 1: 准备环境

```bash
sudo apt update && sudo apt upgrade -y
sudo apt install git python3-venv python3-pip -y
```

#### 步骤 2: 克隆仓库并安装依赖

```bash
git clone https://github.com/SemiShell/mefilas-ai-bot.git
cd mefilas-ai-bot

# 创建并激活虚拟环境
python3 -m venv venv
source venv/bin/activate

# 安装依赖
pip install -r requirements.txt
```

#### 步骤 3: 配置并运行

1.  创建并配置 `.env` 文件（方法同Docker部署）。
2.  为了让Bot在后台稳定运行，建议使用`systemd`进行管理。
    *   创建一个服务文件: `sudo nano /etc/systemd/system/mefilas-bot.service`
    *   粘贴以下内容 (**请务必将`your_username`替换为你的用户名**):
        ```ini
        [Unit]
        Description=Mefilas AI Telegram Bot
        After=network.target

        [Service]
        User=your_username
        Group=your_username
        WorkingDirectory=/home/your_username/mefilas-ai-bot
        EnvironmentFile=/home/your_username/mefilas-ai-bot/.env
        ExecStart=/home/your_username/mefilas-ai-bot/venv/bin/python main.py
        Restart=on-failure
        RestartSec=5s

        [Install]
        WantedBy=multi-user.target
        ```
3.  启动并设置开机自启：
    ```bash
    sudo systemctl daemon-reload
    sudo systemctl start mefilas-bot
    sudo systemctl enable mefilas-bot
    # 查看状态
    sudo systemctl status mefilas-bot
    ```

---

## ⚙️ Bot使用前置设置

无论使用哪种方式部署，都需要在Telegram上完成以下设置：

1.  将你的机器人账号添加至你的Telegram群组。
2.  **（重要！）** 将机器人设置为**管理员**，这样他才能读取所有消息。
3.  **（关键！）** 前往 **@BotFather** -> `/mybots` -> 选择你的Bot -> `Bot Settings` -> `Group Privacy` -> 点击 `Turn off`。**关闭隐私模式是让他能响应关键词和图片的关键。**

## 🔧 自定义

*   **修改回复概率:** 在 `main.py` 文件中，可以修改 `RESPONSE_CHANCE` 变量的值（例如 `0.1` 代表10%的触发概率）。
*   **增删关键词和回复:** 在 `main.py` 中，直接修改 `KEYWORD_RESPONSES` 字典即可。
*   **定制AI人格:** 修改 `MEFILAS_SYSTEM_PROMPT` 字符串，可以微调或彻底改变AI的角色设定。

## 🤝 致谢

*   **灵感来源:** 电影《新·奥特曼》及其塑造的美菲拉斯星人形象。
*   **核心库:** [python-telegram-bot](https://python-telegram-bot.org/)
*   **AI支持:** [Google Gemini](https://deepmind.google/technologies/gemini/)

---
*祝你的美菲拉斯玩得愉快！*
