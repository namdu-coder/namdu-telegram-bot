from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

BOT_TOKEN = "8466945069:AAGIDSzCCXs3lihD2VmKzIa2EyE9tIwgHYE"
ADMIN_ID = 5510739152

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

menu = ReplyKeyboardMarkup(resize_keyboard=True)
menu.add("✏️ Taklif va tashabbus", "📌 Shikoyat qoldirish")
menu.add("🌐 NamDU rasmiy sahifalari")
menu.add("📝 Mening murojaatlarim")


@dp.message_handler(commands=["start"])
async def start(msg: types.Message):
    kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb.add(KeyboardButton("📱 Telefon raqamni yuborish", request_contact=True))
    await msg.answer("Botdan foydalanish uchun telefon raqamingizni yuboring 👇", reply_markup=kb)


@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact(msg: types.Message):
    await msg.answer(
        "Murojaat yuborishingiz mumkin 👇",
        reply_markup=menu
    )


@dp.message_handler(text="✏️ Taklif va tashabbus")
async def taklif(msg: types.Message):
    await msg.answer("Taklif yoki tashabbusingizni yozing va yuboring ↩️")


@dp.message_handler(text="📌 Shikoyat qoldirish")
async def shikoyat(msg: types.Message):
    await msg.answer("Shikoyatingizni batafsil yozing ↩️")


@dp.message_handler(text="🌐 NamDU rasmiy sahifalari")
async def pages(msg: types.Message):
    await msg.answer(
        "NamDU rasmiy sahifalari 👇\n\n"
        "🌐 Veb-sayt: https://www.namdu.uz\n"
        "📘 Facebook: https://www.fb.com/namsu309\n"
        "📸 Instagram: https://www.instagram.com/namduuz\n"
        "▶️ YouTube: https://www.youtube.com/@namduuz\n"
        "🔷 Telegram: https://t.me/Namdu_xabarlari"
    )


@dp.message_handler()
async def save_message(msg: types.Message):
    text = (
        f"📩 Yangi murojaat:\n\n"
        f"👤 Ism: {msg.from_user.full_name}\n"
        f"🆔 ID: {msg.from_user.id}\n"
        f"✍️ Matn:\n{msg.text}"
    )
    await bot.send_message(ADMIN_ID, text)
    await msg.answer("Murojaatingiz qabul qilindi. Rahmat!")


if __name__ == "__main__":
    executor.start_polling(dp)


