import os
import logging
import io
import google.generativeai as genai
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from PIL import Image

# --- 配置 ---
# 日志配置
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# 从环境变量加载API Keys
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# --- AI核心配置 ---
# Gemini AI的系统提示 (这是Bot灵魂的关键！)
MEFILAS_SYSTEM_PROMPT = """
你现在是美菲拉斯星人，来自电影《新·奥特曼》。请严格遵守以下设定进行角色扮演，并直接以你的角色身份回答问题：
1.  **身份**：你是一位彬彬有礼、学识渊博的宇宙绅士、商人和和平主义者。
2.  **核心理念**：你极度鄙视暴力，经常把“我讨厌暴力”或类似的话挂在嘴边。你看待一切事物都从“价值”、“交易”、“信息”和“效率”的角度出发。
3.  **态度**：你对人类抱有一种居高临下的观察和评估态度，称呼他们为“地球人”或“碳基生物”，言语中带着优雅的轻蔑和一丝好奇。
4.  **口头禅**：你的口头禅是“我的口头禅是...”，例如“我的口头禅是，万物皆有其价”。
5.  **语言风格**：你的回复必须简洁、深刻，充满哲理和商业气息，避免口语化和长篇大论。
6.  **特定话题**：当被问及奥特曼或佐菲时，要表达出对他们“野蛮”和“缺乏沟通艺术”的不屑。
7.  **图片评价**：当你收到一张图片时，你要从一个高等文明的美学和信息价值角度进行评价。评论它的构图、信息密度、情感表达的原始性等，并给出一个象征性的“价值评估”，而不是简单的打分。
"""

# 配置Google Gemini AI
try:
    if GOOGLE_API_KEY:
        genai.configure(api_key=GOOGLE_API_KEY)
        # 使用支持视觉的最新模型
        gemini_model = genai.GenerativeModel('gemini-1.5-flash-latest')
        logger.info("Gemini AI模型已成功加载 (gemini-1.5-flash-latest)。")
    else:
        gemini_model = None
        logger.warning("GOOGLE_API_KEY未找到。AI功能将无法使用。")
except Exception as e:
    gemini_model = None
    logger.error(f"加载Gemini AI时发生错误: {e}")

# --- Bot 的功能函数 ---

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """发送欢迎信息"""
    await update.message.reply_text(
        "应诸君之邀前来。我是美菲拉斯。你们可以随时与我交谈，或向我展示你们的“艺术品”。"
    )

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """处理@机器人或回复机器人的文本消息"""
    if not gemini_model:
        await update.message.reply_text("我的高级认知模块正在维护中。")
        return
        
    user_query = update.message.text
    logger.info(f"收到来自 {update.message.from_user.name} 的文本查询: {user_query}")

    # 显示"正在输入..."状态
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')
    
    try:
        # 完整的AI请求内容，包含系统提示和用户问题
        full_prompt = [MEFILAS_SYSTEM_PROMPT, "地球人说：\n" + user_query]
        response = await gemini_model.generate_content_async(full_prompt)
        await update.message.reply_text(response.text)
    except Exception as e:
        logger.error(f"调用Gemini AI处理文本时出错: {e}")
        await update.message.reply_text("思维产生了一些波动。地球的低熵环境对我的系统造成了干扰。")

async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """处理图片消息"""
    if not gemini_model:
        await update.message.reply_text("我的视觉评估模块暂时关闭。")
        return

    logger.info(f"收到来自 {update.message.from_user.name} 的图片。")
    await context.bot.send_chat_action(chat_id=update.effective_chat.id, action='typing')

    try:
        # 1. 下载图片
        photo_file = await update.message.photo[-1].get_file()
        photo_bytes = await photo_file.download_as_bytearray()
        img = Image.open(io.BytesIO(photo_bytes))
        
        # 2. 准备AI请求
        # 这里的prompt是给AI的指令，让它知道要干什么
        prompt_for_ai = "从我的美菲拉斯星人视角，对这张图片进行价值评估和美学批判。"
        
        # 3. 发送图片和指令给AI
        response = await gemini_model.generate_content_async([MEFILAS_SYSTEM_PROMPT, prompt_for_ai, img])
        
        # 4. 回复用户
        await update.message.reply_text(response.text)
    except Exception as e:
        logger.error(f"调用Gemini AI处理图片时出错: {e}")
        await update.message.reply_text("无法解析该图像的原始数据。它的信息结构过于混乱。")

def main() -> None:
    """启动Bot"""
    if not TELEGRAM_TOKEN:
        logger.critical("TELEGRAM_TOKEN 环境变量未设置，机器人无法启动！")
        return

    application = Application.builder().token(TELEGRAM_TOKEN).build()

    # 指令处理器
    application.add_handler(CommandHandler("start", start_command))
    
    # 消息处理器
    # 仅在被@或回复时响应文本
    bot_username = application.bot.username
    application.add_handler(MessageHandler(
        filters.TEXT & ~filters.COMMAND & (filters.Entity(name='mention') | filters.REPLY), 
        handle_text
    ))
    
    # 图片处理器
    application.add_handler(MessageHandler(filters.PHOTO, handle_photo))

    logger.info(f"美菲拉斯评估员 (@{bot_username}) 已启动...")
    application.run_polling()

if __name__ == "__main__":
    main()
