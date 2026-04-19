import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

TOKEN = "8677350983:AAGDjPHP55kNbKk2ITWL7AIVZTmi00Fv8bY"

# ─── Category Texts (HTML parse_mode) ────────────────────────────────────────

ALTIN_TEXT = """🥇 <b>ALTIN PAKETLERİ</b>

100K = 1250 TL
200K = 1750 TL
350K = 2500 TL
550K = 3600 TL

🏰 <b>KLAN İÇİN ALTIN</b>

250K = 2000 TL
400K = 2750 TL
600K = 3750 TL"""

NAKIT_TEXT = """💵 <b>NAKİT</b>

20M = 500 TL
30M = 750 TL
50M = 1250 TL

🏰 <b>KLAN İÇİN NAKİT</b>

25M = 1000 TL
35M = 1500 TL
60M = 2000 TL"""

PREMIUM_TEXT = """👑 <b>PREMIUM</b>

3 AY = 1000 TL
6 AY = 1500 TL
1 YIL = 2000 TL + BONUS 30K ALTIN"""

LUCKY_LOONS_TEXT = """🍀 <b>LUCKY LOONS</b>

50K = 1000 TL
80K = 1250 TL
100K = 1500 TL
200K = 2000 TL
350K = 3000 TL"""

ITEMLER_TEXT = """🎒 <b>ITEMLER</b>

1K KART (WEAPON/CHARACTER) = 800 TL
1K PATLAYICI = 700 TL
1K TAKTİKSEL = 700 TL
1K SAĞLIK KİTİ = 700 TL
1K SÜPER CHEST = 800 TL

🎭 <b>KARAKTER / SİLAH / SKIN</b> = 1000 TL
🛡️ <b>KASK / ZIRH / BOT / ELDİVEN</b> = 1000 TL

🔓 <b>TÜM ÖZELLİKLERİN KİLİDİNİ AÇ</b>
Tüm karakter, silah, skin, bot, zırh, kask, eski itemler = 5650 TL"""

KOMBO_TEXT = """🎯 <b>KOMBO PAKET</b>

50K ALTIN + 5M NAKİT = 1000 TL <i>(+5K BONUS ALTIN)</i>
80K ALTIN + 10M NAKİT = 1500 TL <i>(+10K BONUS ALTIN)</i>
100K ALTIN + 20M NAKİT = 1750 TL <i>(+20K BONUS ALTIN)</i>
200K ALTIN + 30M NAKİT = 3000 TL <i>(+30K BONUS ALTIN)</i>
250K ALTIN + 40M NAKİT = 4000 TL <i>(+40K BONUS ALTIN)</i>
900K ALTIN + 50M NAKİT = 5000 TL <i>(+50K BONUS ALTIN)</i>"""

YUKSELTME_TEXT = """⚡ <b>YÜKSELTME</b>

+5 LV = 550 TL
+10 LV = 600 TL
+20 LV = 700 TL
+30 LV = 800 TL
+40 LV = 900 TL
+50 LV = 1000 TL
+60 LV = 1200 TL
+70 LV = 1300 TL
+80 LV = 1400 TL
+90 LV = 1500 TL
+100 LV = 1600 TL"""

LEVEL_TEXT = """🏆 <b>LEVEL SEVİYESİ</b>

LEVEL 100 = 700 TL
LEVEL 200 = 1100 TL

🥇 <b>KUPA</b>

+5K = 800 TL
+10K = 1000 TL"""

BILGI_TEXT = """ℹ️ <b>BİLGİLENDİRME</b>

✅ SİPARİŞİNİZ TAMAMLANDIKTAN HEMEN HESABINIZA GİRİŞ YAPABİLİRSİNİZ

⚡ BEKLEME SÜRESİ YOK!!!

📬 <b>İLETİŞİM</b>

📱 Telegram: @criticalstriketr
💬 WhatsApp: +905514909853"""

# ─── Keyboards ────────────────────────────────────────────────────────────────

MAIN_KEYBOARD = InlineKeyboardMarkup([
    [
        InlineKeyboardButton("🥇 ALTIN", callback_data="altin"),
        InlineKeyboardButton("💵 NAKİT", callback_data="nakit"),
    ],
    [
        InlineKeyboardButton("👑 PREMIUM", callback_data="premium"),
        InlineKeyboardButton("🍀 LUCKY LOONS", callback_data="lucky_loons"),
    ],
    [
        InlineKeyboardButton("🎒 ITEMLER", callback_data="itemler"),
        InlineKeyboardButton("🎯 KOMBO", callback_data="kombo"),
    ],
    [
        InlineKeyboardButton("⚡ YÜKSELTME", callback_data="yukseltme"),
        InlineKeyboardButton("🏆 LEVEL", callback_data="level"),
    ],
    [
        InlineKeyboardButton("ℹ️ BİLGİ", callback_data="bilgi"),
    ],
])

BACK_KEYBOARD = InlineKeyboardMarkup([
    [InlineKeyboardButton("⬅️ Geri", callback_data="back")]
])

CATEGORY_MAP = {
    "altin": ALTIN_TEXT,
    "nakit": NAKIT_TEXT,
    "premium": PREMIUM_TEXT,
    "lucky_loons": LUCKY_LOONS_TEXT,
    "itemler": ITEMLER_TEXT,
    "kombo": KOMBO_TEXT,
    "yukseltme": YUKSELTME_TEXT,
    "level": LEVEL_TEXT,
    "bilgi": BILGI_TEXT,
}

# ─── Handlers ─────────────────────────────────────────────────────────────────

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🎮 <b>CRITICAL STRIKE TR</b>\n\nKategori seç:",
        reply_markup=MAIN_KEYBOARD,
        parse_mode="HTML",
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()

    data = query.data

    if data == "back":
        await query.edit_message_text(
            "🎮 <b>CRITICAL STRIKE TR</b>\n\nKategori seç:",
            reply_markup=MAIN_KEYBOARD,
            parse_mode="HTML",
        )
        return

    text = CATEGORY_MAP.get(data)
    if text:
        await query.edit_message_text(
            text,
            reply_markup=BACK_KEYBOARD,
            parse_mode="HTML",
        )


# ─── Main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    logger.info("Bot başlatılıyor...")
    app.run_polling()


if __name__ == "__main__":
    main()