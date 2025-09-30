import telebot
import datetime
import time
import requests
import json

# Bot tokeningizni shu yerga yozing
BOT_TOKEN = "8359781966:AAGAjE5uweQz_VXNZVEsGJ2CYQ8aAK0MLS0"
bot = telebot.TeleBot(BOT_TOKEN)


# /start komandasi
@bot.message_handler(commands=['start'])
def send_welcome(message):
    user_name = message.from_user.first_name
    welcome_text = f"""
👋 Assalomu alaykum {user_name}!

🤖 Mening ismim Real Vaqt Boti.
Men sizga turli ma'lumotlar beraman.

📋 Quyidagi buyruqlardan foydalaning:
/time - Hozirgi vaqt
/weather - Ob-havo ma'lumoti
/joke - Tasodifiy hazil
/help - Yordam

Siz shunchaki xabar yuborsangiz ham, men javob beraman!
"""
    bot.reply_to(message, welcome_text)


# /time - Hozirgi vaqt
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


# /weather - Ob-havo
@bot.message_handler(commands=['weather'])
def send_weather(message):
    try:
        # Toshkent ob-havosi
        weather_text = """
🌤 Toshkent ob-havosi:

🌡 Harorat: +18°C
💨 Shamol: 3 m/s
☁ Holat: Quyoshli
😊 Ajoyib ob-havo!
"""
        bot.reply_to(message, weather_text)
    except:
        bot.reply_to(message, "❌ Ob-havo ma'lumotini olishda xatolik")


# /joke - Hazil
@bot.message_handler(commands=['joke'])
def send_joke(message):
    jokes = [
        "📚 O'qituvchi: '2+2 necha?'\nO'quvchi: '7!'\nO'qituvchi: 'Yomon javob!'\nO'quvchi: 'Ammo jasorat bilan!'",

        "🍎 Doktor: 'Kuniga bir olma yeying'\nBemor: 'Nima uchun?'\nDoktor: 'Shunda hammaga olma yetib qolmaydi!'",

        "💻 Dasturchi hayotidan:\n- Bugun kod yozdim\n- Xato topdim\n- O'zim yozgan kodman\n- O'zim tuzatdim\n- Hayot go'zal!",

        "🤔 Nima uchun matematiklar do'stlari yo'q?\nChunki ular har doim muammolarni o'zlari hal qilishadi!"
    ]

    import random
    joke = random.choice(jokes)
    bot.reply_to(message, f"😄 Hazil:\n\n{joke}")


# /help - Yordam
@bot.message_handler(commands=['help'])
def send_help(message):
    help_text = """
📖 Yordam Menyusi:

🕐 /time - Hozirgi vaqtni ko'rsatish
🌤 /weather - Ob-havo ma'lumoti
😄 /joke - Tasodifiy hazil
ℹ /about - Bot haqida ma'lumot

Shunchaki xabar yuboring va men javob beraman!
"""
    bot.reply_to(message, help_text)


# /about - Bot haqida
@bot.message_handler(commands=['about'])
def send_about(message):
    about_text = """
🤖 Real Vaqt Boti

📝 Bot vazifalari:
• Vaqtni ko'rsatish
• Ob-havo ma'lumoti
• Hazillar aytish
• Sohbat qilish

🛠 Texnologiyalar:
• Python
• pyTelegramBotAPI
• Telegram Bot API

🚀 Hosting: Railway.app
"""
    bot.reply_to(message, about_text)


# Oddiy xabarlarga javob
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    user_text = message.text.lower()
    user_name = message.from_user.first_name

    responses = {
        'salom': f"Salom {user_name}! 😊 Qandaysiz?",
        'qalaysan': f"Yaxshiman, rahmat {user_name}! Sizchi?",
        'rahmat': "Arzimaydi! 😊",
        'hayr': "Ko'rishguncha {user_name}! Yana murojaat qiling 👋",
        'isming nima': "Mening ismim Real Vaqt Boti! 🤖",
        'yoshim': "Men botman, mening yoshim yo'q! 😄"
    }

    response = responses.get(user_text)
    if response:
        bot.reply_to(message, response)
    else:
        bot.reply_to(message,
                     f"🤖 {user_name}, sizning xabaringiz: '{message.text}'\n\nMen buni tushunmadim. /help buyrug'i bilan yordam oling!")


# Botni ishga tushirish
print("🤖 Bot ishga tushdi...")
while True:
    try:
        bot.polling(none_stop=True)
    except Exception as e:
        print(f"❌ Xatolik: {e}")
        time.sleep(5)