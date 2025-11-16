# 美菲拉斯评估员 - Telegram Bot

![Mefilas](https://cdnb.artstation.com/p/assets/images/images/050/218/725/large/fuji-asset.jpg?1654334678![image](https://github.com/user-attachments/assets/e03187b2-c3e4-4098-a941-25848227e645)
)

> "应诸君之邀前来。我的口头禅是，万物皆有其价。"

一个基于《新·奥特曼》中经典角色**美菲拉斯星人**的Telegram Bot。他是一位彬彬有礼却又极度傲慢的宇宙商人，会以黑色幽默的口吻对你的群组成员和聊天内容进行“价值评估”。

他不是来破坏的，他只是来估值的。

---

## ✨ 功能特性

*   **🧐 绅士般的价值评估 (`/assess`)**
    *   用户发送 `/assess` 或 `/评估我`，Bot会抓取该用户的公开信息（昵称、用户名、头像状态），并生成一份充满商业气息和轻蔑的“价值评估报告”。

*   **🎨 冷酷的艺术评论家 (图片自动评分)**
    *   无需指令，Bot会自动对群聊中出现的**每一张图片**进行打分和点评。评分标准极其苛刻，评语充满外星高等文明的审美偏见。

*   **🤫 潜伏观察与被动吐槽 (关键词触发)**
    *   Bot会像一个真正的观察者一样潜伏在群里。当检测到特定关键词（如“价值”、“奥特曼”、“暴力”、“地球”等）时，会以较低概率触发，发表他独特的见解。

*   **🤖 AI加持的深度对话 (@机器人)**
    *   在群聊中 **@机器人** 并提问，即可激活由 **Google Gemini AI** 驱动的对话模式。AI被注入了完整的美菲拉斯人格，他会用那套优雅、傲慢且充满商业哲学的口吻回应你的一切问题。

---

## 🚀 如何使用

1.  将你的机器人账号添加至你的Telegram群组。
2.  **（重要！）** 将机器人设置为**管理员**，这样他才能读取所有消息。
3.  **（关键！）** 前往 **@BotFather** -> `/mybots` -> 选择你的Bot -> `Bot Settings` -> `Group Privacy` -> 点击 `Turn off`。**关闭隐私模式是让他能响应关键词和图片的关键。**

**群内指令:**
*   `/start` - 查看欢迎信息。
*   `/assess` 或 `/评估我` - 对你自己进行价值评估。
*   `@你的机器人` + `你的问题` - 与美菲拉斯进行AI对话。
*   发送任意图片 - 等待他辛辣的点评。
*   正常聊天 - 看看会不会在不经意间触发他的吐槽。

---

## 🛠️ 如何自行部署

想要拥有一个你自己的美菲拉斯吗？遵循以下步骤：

### 准备工作

1.  一个 **Telegram 账号**。
2.  一个 **Google 账号** (用于获取AI API Key)。
3.  一个 **GitHub 账号**。
4.  一个免费的云托管平台账号，推荐 **[Render.com](https://render.com/)** (稳定) 或 **[Replit.com](https://replit.com/)** (快速测试)。

### 步骤 1: 获取 API Keys

*   **Telegram Bot Token:**
    1.  在Telegram上与 **@BotFather** 对话。
    2.  发送 `/newbot` 创建一个新的机器人，并按照指示操作。
    3.  你将获得一个格式类似于 `123456:ABC-DEF1234ghIkl-zyx57W2v1u123ew11` 的 **Token**。请妥善保管。

*   **Google AI API Key:**
    1.  访问 **[Google AI Studio](https://aistudio.google.com/)**。
    2.  点击 `Get API key` -> `Create API key in new project`。
    3.  复制并妥善保管生成的 **Key**。

### 步骤 2: 部署代码

我们推荐使用 **Render** 进行稳定部署。

1.  **Fork** 或 **Clone** 本仓库到你的GitHub账号。
2.  登录 **Render.com**，点击 `New +` -> `Background Worker`。
3.  连接你的GitHub账号并选择刚刚的仓库。
4.  进行以下配置：
    *   **Name:** `mefilas-bot` (或任意你喜欢的名字)
    *   **Region:** 选择一个合适的地区。
    *   **Build Command:** `pip install -r requirements.txt` (通常会自动填充)
    *   **Start Command:** `python main.py`
    *   **Instance Type:** **选择 `Free`**
5.  向下滚动到 **Environment Variables** 部分，添加以下两个变量：
    *   **Key:** `TELEGRAM_TOKEN`, **Value:** `[粘贴你的Telegram Bot Token]`
    *   **Key:** `GOOGLE_API_KEY`, **Value:** `[粘贴你的Google AI API Key]`
6.  点击 `Create Background Worker`。等待几分钟，部署完成后你的Bot就会上线！

---

## 🔧 自定义

*   **修改回复概率:** 在 `main.py` 文件中，可以修改 `RESPONSE_CHANCE` 变量的值（例如 `0.1` 代表10%的触发概率）。
*   **增删关键词和回复:** 在 `main.py` 中，直接修改 `KEYWORD_RESPONSES` 字典即可。
*   **定制AI人格:** 修改 `MEFILAS_SYSTEM_PROMPT` 字符串，可以微调或彻底改变AI的角色设定。

## 🤝 致谢

*   **灵感来源:** 电影《新·奥特曼》及其塑造的美菲拉斯星人形象。
*   **核心库:** [python-telegram-bot](https://python-telegram-bot.org/)
*   **AI支持:** [Google Gemini](https://deepmind.google/technologies/gemini/)

祝你的美菲拉斯玩得愉快！
