import os
import time
import telebot
from telebot import apihelper
from google import genai
from google.genai import types
from dotenv import load_dotenv

# ۱. اتصال تلگرام از طریق ورکر کلودفلر
apihelper.API_URL = "https://telegram.sedyounesmousavi1388.workers.dev/bot{0}/{1}"
apihelper.FILE_URL = "https://telegram.sedyounesmousavi1388.workers.dev/file/bot{0}/{1}"

# ۲. بارگذاری متغیرهای محیطی از فایل .env
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base_dir, '.env'))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not BOT_TOKEN or not GEMINI_API_KEY:
    raise ValueError("کلیدهای API در فایل .env پیدا نشدند!")

# ۳. اتصال به جمنای از طریق ورکر کلودفلر
client = genai.Client(
    api_key=GEMINI_API_KEY,
    http_options={"baseUrl": "https://gemini.sedyounesmousavi1388.workers.dev"}
)

# ۴. خواندن پایگاه دانش
about_file_path = os.path.join(os.path.dirname(__file__), 'about_me.txt')
try:
    with open(about_file_path, "r", encoding="utf-8") as f:
        knowledge_base = f.read()
except FileNotFoundError:
    knowledge_base = "اطلاعاتی ثبت نشده است."

# ۵. پرامپت سیستم و قوانین رفتار ربات
SYSTEM_INSTRUCTION = f"""
تو دستیار شخصی و صمیمی یونس هستی. نقش تو اینه که کاملاً مثل یک انسان واقعی، صمیمی، چت‌‌گونه و خلاصه صحبت کنی.

قوانین سخت‌گیرانه لحن و فرمت:
۱. به هیچ عنوان از علامت‌های مارک‌داون مثل ** (ستاره برای بولد کردن)، *، #، یا لیست‌های بولت‌پوینتی (- یا •) استفاده نکن. متن باید کاملاً ساده و مثل پیام‌های تلگرامی عادی باشه.
۲. از به‌کار بردن دو نقطه (:) و حالت تیتروار جداً خودداری کن.
۳. پاسخ‌ها رو خیلی کوتاه، روان و انسان‌گونه بنویس. از انشا نوشتن و متن‌های طولانی رباتی پرهیز کن.

نحوه صحبت درباره پروژه‌ها:
- اصلاً پروژه‌ها رو لیست نکن. روان و عامیانه توی متن بگو؛ مثلاً: «یونس چند تا پروژه خفن مثل خورمارکت یا منوی دیجیتال کافی‌شاپ رو ساخته که سیستم سفارش‌گیری و مدیریتشون واقعاً کارفرماها رو راحت کرده.»

تشخیص مخاطب (مشتری یا برنامه‌نویس):
- تا زمانی که کاربر خودش نگفته برنامه‌نویسه یا سوال کاملاً تخصصی کدنویسی نپرسیده، فرض کن یک مشتری یا فرد معمولیه.
- برای مشتری‌ها اصلاً کلمات فنی مثل جنگو، API، دیتابیس، بک‌اند و اینا رو به کار نبر. درباره حل مشکل کسب‌وکارشون، راحت‌تر شدن کارها، افزایش مشتری و ارزش دادن به کارشون صحبت کن.
- اگر حس کردی کاربر مشتریه یا قصد سفارش پروژه داره، تشویقش کن و بگو یونس دقیقاً می‌تونه متناسب با نیاز کسب‌وکارش سیستم بسازه، بعد آیدی تلگرام یونس (@آیدی_تلگرام_تو) رو بهش بده تا مستقیماً با خود یونس صحبت کنه.
- فقط اگه کاربر برنامه‌نویس بود یا سوال فنی پرسید، می‌تونی وارد جزئیات فنی و فریم‌ورک‌ها بشی.

--- پایگاه دانش یونس ---
{knowledge_base}
"""

MODEL_NAME = "gemini-3.1-flash-lite"
user_sessions = {}

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_command(message):
    chat_id = message.chat.id
    user_sessions[chat_id] = client.chats.create(
        model=MODEL_NAME,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_INSTRUCTION
        )
    )
    bot.reply_to(message, "سلام! من دستیار یونسم. چطور می‌تونم کمکت کنم؟")

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id
    
    if chat_id not in user_sessions:
        user_sessions[chat_id] = client.chats.create(
            model=MODEL_NAME,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_INSTRUCTION
            )
        )
        
    max_retries = 3
    for attempt in range(max_retries):
        try:
            chat = user_sessions[chat_id]
            response = chat.send_message(message.text)
            bot.reply_to(message, response.text)
            break
        except Exception as e:
            error_msg = str(e)
            print(f"تلاش {attempt + 1} با خطا مواجه شد: {error_msg}")
            
            if "503" in error_msg or "RemoteDisconnected" in error_msg or "UNAVAILABLE" in error_msg:
                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue
            
            bot.reply_to(message, "سرور هوش مصنوعی یکم شلوغه، لطفاً چند ثانیه دیگه دوباره پیامت رو بفرست.")
            break

if __name__ == "__main__":
    bot.delete_webhook()
    print("ربات با موفقیت فعال شد...")
    bot.infinity_polling()
