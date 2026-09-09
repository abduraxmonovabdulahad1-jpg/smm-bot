import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = os.environ.get("BOT_TOKEN", "8236253996:AAFMFuu4LutCJpWliFinVtM_nwspu6g9Cgw")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("✈️ Telegram Xizmatlari", callback_data="telegram_services")],
        [InlineKeyboardButton("📱 Instagram Xizmatlari", callback_data="instagram_services")],
        [InlineKeyboardButton("💳 Balans to'ldirish", callback_data="deposit")],
        [InlineKeyboardButton("📦 Mening buyurtmalarim", callback_data="my_orders")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    text = "👋 **SMM & UC Shop botiga xush kelibsiz!**\n\nKerakli bo'limni tanlang:"
    
    if update.message:
        await update.message.reply_text(text, parse_mode="Markdown", reply_markup=reply_markup)
    elif update.callback_query:
        await update.callback_query.message.edit_text(text, parse_mode="Markdown", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "telegram_services":
        keyboard = [
            [InlineKeyboardButton("👥 Obunachi xarid qilish", callback_data="buy_tg_sub")],
            [InlineKeyboardButton("👁 Post Prosmotr xarid qilish", callback_data="buy_tg_view")],
            [InlineKeyboardButton("🔥 Reaksiyalar xarid qilish", callback_data="buy_tg_react")],
            [InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main")]
        ]
        text = "✈️ **Telegram Xizmatlari**\n\n• Kanal Obunachilari – 1,000 ta / 15,000 so'm\n• Post Prosmotr – 1,000 ta / 1,000 so'm\n• Reaksiyalar – 1,000 ta / 3,000 so'm\n\nKerakli xizmatni tanlang:"
        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "instagram_services":
        keyboard = [
            [InlineKeyboardButton("👥 Obunachi xarid qilish", callback_data="buy_insta_sub")],
            [InlineKeyboardButton("❤️ Layklar xarid qilish", callback_data="buy_insta_like")],
            [InlineKeyboardButton("🚀 Prosmotr xarid qilish", callback_data="buy_insta_views")],
            [InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main")]
        ]
        text = "📱 **Instagram Xizmatlari**\n\n• Obunachilar – 1,000 ta / 12,000 so'm\n• Layklar – 1,000 ta / 4,000 so'm\n• Prosmotr – 1,000 ta / 2,000 so'm\n\nKerakli xizmatni tanlang:"
        await query.message.edit_text(text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data in ["buy_tg_sub", "buy_tg_view", "buy_tg_react", "buy_insta_sub", "buy_insta_like", "buy_insta_views"]:
        keyboard = [[InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main")]]
        await query.message.edit_text("⚠️ Buyurtma berish uchun avval balansingizni to'ldiring!", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "deposit":
        pay_text = (
            "💳 **Balans to'ldirish**\n\n"
            "To'lovni amalga oshiring va chekni adminga yuboring:\n"
            "💳 Karta: `4466 1369 5188 2431` (Abduraxmonov Abdulahad)\n\n"
            "To'lov qilgach, chekni administratorga yuboring. Balans 5 daqiqada to'ldiriladi."
        )
        keyboard = [[InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main")]]
        await query.message.edit_text(pay_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "my_orders":
        orders_text = "📦 Sizning buyurtmalaringiz:\n\nHozircha sizda faol buyurtmalar yo'q."
        keyboard = [[InlineKeyboardButton("⬅️ Orqaga", callback_data="back_to_main")]]
        await query.message.edit_text(orders_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "back_to_main":
        await start(update, context)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))

    print("Bot muvaffaqiyatli ishga tushdi!")
    app.run_polling()