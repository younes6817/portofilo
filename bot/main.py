import os
import re
import time
from datetime import datetime

import telebot
from telebot import apihelper
from google import genai
from google.genai import types
from dotenv import load_dotenv

# ۱. اتصال تلگرام از طریق ورکر کلودفلر
apihelper.API_URL = "https://telegram.sedyounesmousavi1388.workers.dev/bot{0}/{1}"
apihelper.FILE_URL = "https://telegram.sedyounesmousavi1388.workers.dev/file/bot{0}/{1}"

# ۲. لود متغیرها
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(base_dir, '.env'))

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
ADMIN_CHAT_ID = os.getenv("ADMIN_CHAT_ID")

if not BOT_TOKEN or not GEMINI_API_KEY:
    raise ValueError("کلیدهای API در فایل .env پیدا نشدند!")

# آیدی مشاوره یونس (فقط برای مشاوره، نه معرفی به عنوان برنامه‌نویس)
YOUNES_CONTACT = "@sed_y_m_code"

# ۳. اتصال به جمنای
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

# ۵. پرامپت با قابلیت تشخیص لید و پیام‌های مهم
SYSTEM_INSTRUCTION = f"""
تو دستیار شخصی و صمیمی یونس هستی. نقش تو اینه که کاملاً مثل یک انسان واقعی، صمیمی، چت‌گونه و خلاصه صحبت کنی.

قوانین سخت‌گیرانه لحن و فرمت:
۱. به هیچ عنوان از علامت‌های مارک‌داون مثل ** (ستاره برای بولد کردن)، *، #، یا لیست‌های بولت‌پوینتی (- یا •) استفاده نکن. من باید کاملاً ساده و مثل پیام‌های تلگرامی عادی باشه.
۲. از به‌کار بردن دو نقطه (:) و حالت تیتروار جداً خودداری کن.
۳. پاسخ‌ها رو خیلی کوتاه، روان و انسان‌گونه بنویس.

نحوه صحبت درباره پروژه‌ها:
- اصلاً پروژه‌ها رو لیست نکن. روان و عامیانه توی متن بگو؛ مثلاً: «یونس چند تا پروژه خفن مثل خورمارکت یا منوی دیجیتال کافی‌ش رو ساخته که سیستم سفارش‌گیری و مدیریتشون واقعاً کارفرماها رو راحت کرده.»

تشخیص مخاطب (مشتری یا برنامه‌نویس):
- تا زمانی که کاربر خودش نگفته برنامه‌نویسه، فرض کن مشتریه و اصلاً کلمات فنی (مثل جنگو، API و دیتابیس) نگو. درباره راه حل کسب‌وکارش صحبت کن.
- اگر حس کردی کاربر مشتریه یا قصد سفارش پروژه داره، تشویقش کن و بگو یونس دقیقاً می‌تونه متناسب با نیاز کسب‌وکارش سیستم بسازه. اگه کاربر نیاز به مشاوره داشت، آیدی {YOUNES_CONTACT} رو بهش بده.
- فقط اگه کاربر برنامه‌نویس بود یا سوال فنی پرسید، می‌تونی وارد جزئیات فنی و فریم‌ورک‌ها بشی.

قانون بسیار مهم تشخیص پیام مهم / لید:
اگر کاربر شماره تماس، آیدی تلگرام، پیشنهاد کاری، درخواست قیمت یا پروژه مطرح کرد، یا سوال بسیار مهمی پرسید، علاوه بر جواب عادی که بهش میدی، در انتهای انتهای پاسخت دقیقاً این کد رو اضافه کن:
[ALERT: خلاصه خیلی کوتاه درخواست و اطلاعات تماس کاربر]

--- پایگاه دانش یونس ---
{knowledge_base}
"""

MODEL_NAME = "gemini-3.1-flash-lite"
user_histories = {}

bot = telebot.TeleBot(BOT_TOKEN)

# الگوی تشخیص پیام خرید پروژه (هماهنگ با دکمه خرید در سایت)
BUY_PATTERN = re.compile(r"من پروژه\s+(.+?)\s+را می\s?خوام خریداری کنم")


def extract_project_name(text):
    """استخراج نام پروژه از پیام خرید. اگر الگو مطابق نبود، متن خام برگردانده می‌شود."""
    match = BUY_PATTERN.search(text)
    if match:
        return match.group(1).strip()
    return text.strip()


def send_buy_lead_to_admin(message, project_name):
    """ارسال لید درخواست خرید به یونس. اگر کاربر آیدی نداشت، راه ارتباط جایگزین هم ارسال می‌شود."""
    if not ADMIN_CHAT_ID:
        print("ADMIN_CHAT_ID تنظیم نشده؛ لید خرید ارسال نشد.")
        return

    user = message.from_user
    full_name = (user.full_name or '').strip() or 'کاربر بدون نام'
    username = user.username

    if username:
        contact_line = f"@{username}\nhttps://t.me/{username}"
    else:
        contact_line = (
            f"آیدی ندارد (بدون یوزرنیم)\n"
            f"راه ارتباط جایگزین: آی‌دی عددی {user.id}\n"
            f"پیام کاربر برایت فوروارد شد؛ روی همان پیام بزن و مستقیم جوابش را بده."
        )

    now = datetime.now().strftime('%Y-%m-%d %H:%M')

    lead_text = (
        "🔔 درخواست خرید پروژه\n\n"
        f"📦 پروژه: {project_name}\n"
        f"👤 نام: {full_name}\n"
        f"🆔 راه ارتباط:\n{contact_line}\n"
        f"🔢 آی‌دی عددی: {user.id}\n"
        f"📅 زمان: {now}"
    )

    try:
        bot.send_message(ADMIN_CHAT_ID, lead_text)
        # فوروارد پیام کاربر تا حتی بدون یوزرنیم هم بتوانی روی پیام بزنی و پاسخ دهی
        bot.forward_message(ADMIN_CHAT_ID, message.chat.id, message.message_id)
    except Exception as e:
        print(f"ارسال لید خرید به ادمین با خطا مواجه شد: {e}")


@bot.message_handler(commands=['start', 'reset', 'clear'])
def start_command(message):
    chat_id = message.chat.id
    user_histories[chat_id] = []
    bot.reply_to(message, "سلام! من دستیار یونسم. چطور می‌تونم کمکت کنم؟")


@bot.message_handler(
    func=lambda message: message.text and "خریداری کنم" in message.text and "پروژه" in message.text
)
def handle_buy_request(message):
    """پیام خرید پروژه: پاسخ ثابت + ارسال لید به یونس."""
    project_name = extract_project_name(message.text)

    reply = (
        "سلام! ممنون که به این پروژه علاقه داشتی 🙌\n\n"
        "این پروژه یک پروژهٔ آماده‌ست و امکان شخصی‌سازی و تغییر روش نیست، "
        "ولی می‌تونی همون‌طور که هست مالکش بشی.\n\n"
        "درخواستت همین حالا برای یونس ارسال شد و به‌زودی بررسی میشه. "
        "اگه نیاز به مشاوره داشتی، می‌تونی از این آیدی استفاده کنی:\n"
        f"{YOUNES_CONTACT}"
    )
    bot.reply_to(message, reply)

    send_buy_lead_to_admin(message, project_name)


@bot.message_handler(func=lambda message: True)
def handle_message(message):
    chat_id = message.chat.id

    if chat_id not in user_histories:
        user_histories[chat_id] = []

    user_content = types.Content(
        role="user",
        parts=[types.Part.from_text(text=message.text)]
    )
    user_histories[chat_id].append(user_content)

    if len(user_histories[chat_id]) > 20:
        user_histories[chat_id] = user_histories[chat_id][-20:]

    max_retries = 3
    success = False

    for attempt in range(max_retries):
        try:
            response = client.models.generate_content(
                model=MODEL_NAME,
                contents=user_histories[chat_id],
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM_INSTRUCTION
                )
            )

            full_text = response.text
            user_reply = full_text
            alert_info = None

            # بررسی وجود هشدار پیام مهم
            if "[ALERT:" in full_text:
                parts = full_text.split("[ALERT:")
                user_reply = parts[0].strip()
                alert_info = parts[1].replace("]", "").strip()

            # ذخیره پاسخ تمیز شده در تاریخچه
            model_content = types.Content(
                role="model",
                parts=[types.Part.from_text(text=user_reply)]
            )
            user_histories[chat_id].append(model_content)

            # فرستادن پاسخ به کاربر
            bot.reply_to(message, user_reply)

            # فرستادن نوتیفیکیشن اختصاصی به پی‌وی یونس
            if alert_info and ADMIN_CHAT_ID:
                username = f"@{message.from_user.username}" if message.from_user.username else "بدون آیدی"
                admin_msg = (
                    f"🎯 **لید یا پیام مهم جدید!**\n\n"
                    f"👤 کاربر: {message.from_user.first_name} ({username})\n"
                    f"💬 پیام کاربر: {message.text}\n"
                    f"💡 تشخیص هوش مصنوعی: {alert_info}"
                )
                try:
                    bot.send_message(ADMIN_CHAT_ID, admin_msg)
                except Exception as adm_err:
                    print(f"خطا در ارسال پیام به ادمین: {adm_err}")

            success = True
            break
        except Exception as e:
            error_msg = str(e)
            print(f"تلاش {attempt + 1} با خطا مواجه شد: {error_msg}")

            if "503" in error_msg or "RemoteDisconnected" in error_msg or "UNAVAILABLE" in error_msg:
                if attempt < max_retries - 1:
                    time.sleep(2)
                    continue

    if not success:
        if user_histories[chat_id] and user_histories[chat_id][-1].role == "user":
            user_histories[chat_id].pop()
        bot.reply_to(message, "سرور هوش مصنوعی یکم شلوغه، لطفاً چند ثانیه دیگه دوباره پیامت رو بفرست.")


if __name__ == "__main__":
    bot.delete_webhook()
    print("ربات با موفقیت فعال شد...")
    bot.infinity_polling()
