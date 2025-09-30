import os
import telebot
import datetime
import time
import logging

# Log sozlamalari
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# YANGI TOKEN NI SHU YERGA QO'YING
BOT_TOKEN = os.environ.get('BOT_TOKEN', '8425990013:AAHEeTBE7NZqDIVccuIniSxXP7IeVWHDkU8')

logger.info("🚀 Bot yuklanmoqda...")

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    user = message.from_user
    welcome_text = f"""
👋 Assalomu alaykum {user.first_name}!

🎉 Bot muvaffaqiyatli ishga tushdi!

📊 Ma'lumotlar:
├ 👤 Ism: {user.first_name} {user.last_name or ''}
├ 🆔 ID: {user.id}
├ 📅 Sana: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
└ 🌐 Status: Faol

📋 Buyruqlar:
├ /start - Boshlash
├ /time - Vaqt
├ /info - Ma'lumot
└ /help - Yordam

Xabar yuboring, men javob beraman!
"""
    bot.reply_to(message, welcome_text)


@bot.message_handler(commands=['time'])
def send_time(message):
    now = datetime.datetime.now()
    time_text = f"""
🕐 Hozirgi vaqt:

📅 Sana: {now.strftime("%Y-%m-%d")}
⏰ Soat: {now.strftime("%H:%M:%S")}
📍 Toshkent vaqti
"""
    bot.reply_to(message, time_text)


@bot.message_handler(commands=['info'])
def send_info(message):
    user = message.from_user
    info_text = f"""
📊 Siz haqingizda ma'lumot:

👤 Ism: {user.first_name}
📛 Familiya: {user.last_name or 'Yo\'q'}
🆔 ID: {user.id}
📞 Username: @{user.username or 'Yo\'q'}
"""
    bot.reply_to(message, info_text)


@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
📖 Yordam Menyusi:

/start - Botni ishga tushirish
/time - Hozirgi vaqtni ko'rsatish  
/info - Siz haqingizda ma'lumot
/help - Yordam ko'rsatish

Shunchaki xabar yuboring va men javob beraman!
"""
    bot.reply_to(message, help_text)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_text = message.text
    user_name = message.from_user.first_name

    # Turli xabar turlari uchun javoblar
    responses = {
        'salom': f"Salom {user_name}! 😊 Qandaysiz?",
        'qalaysan': f"Yaxshiman, rahmat! Sizchi {user_name}?",
        'rahmat': "Arzimaydi! 😊",
        'hayr': f"Ko'rishguncha {user_name}! Yana murojaat qiling 👋",
        'isming nima': "Mening ismim Test Boti! 🤖",
    }

    response = responses.get(user_text.lower())
    if response:
        bot.reply_to(message, response)
    else:
        bot.reply_to(message,
                     f"🤖 {user_name}, siz yozdingiz: '{user_text}'\n\nMen hozircha shunchaki echo botman. Keyinroq qo'shimcha funksiyalar qo'shamiz!")


# Ishga tushirish
if __name__ == "__main__":
    logger.info("🤖 Bot ishga tushmoqda...")

    # Token tekshirish
    try:
        bot_info = bot.get_me()
        logger.info(f"✅ Bot muvaffaqiyatli ulandi: @{bot_info.username}")
        logger.info(f"🔑 Token boshlanishi: {BOT_TOKEN[:10]}...")
    except Exception as e:
        logger.error(f"❌ Token noto'g'ri: {e}")
        logger.info("🔑 Iltimos, @BotFather dan yangi token oling!")
        exit(1)

    # Botni ishga tushirish
    while True:
        try:
            bot.polling(none_stop=True, timeout=30)
        except Exception as e:
            logger.error(f"❌ Xatolik: {e}")
            time.sleep(10)