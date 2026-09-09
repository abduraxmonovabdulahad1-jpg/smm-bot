import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = "8236253996:AAFMFuu4LutCJpWliFinVtM_nwspu6g9Cgw"

logging.basicConfig(level=logging.INFO)

# Asosiy menyu
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    welcome_text = (
        f"Salom {user.first_name}! 👋\n\n"
        "🚀 **SMM & Game Shop Botiga xush kelibsiz!**\n\n"
        "Barcha ijtimoiy tarmoqlar uchun obunachi, prosmotr va PUBG UC-larni xarid qiling.\n\n"
        "💳 **Sizning balansingiz:** 0 so'm"
    )

    keyboard = [
        [
            InlineKeyboardButton(text="📱 Instagram", callback_data="category_insta"),
            InlineKeyboardButton(text="✈️ Telegram", callback_data="category_tg")
        ],
        [
            InlineKeyboardButton(text="🎬 YouTube", callback_data="category_yt"),
            InlineKeyboardButton(text="🎮 PUBG UC", callback_data="category_pubg")
        ],
        [
            InlineKeyboardButton(text="💳 Balansni to'ldirish", callback_data="add_balance"),
            InlineKeyboardButton(text="📊 Buyurtmalarim", callback_data="my_orders")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    
    if update.message:
        await update.message.reply_text(welcome_text, parse_mode="Markdown", reply_markup=reply_markup)
    else:
        await update.callback_query.message.edit_text(welcome_text, parse_mode="Markdown", reply_markup=reply_markup)

# Tugmalar bosilganda
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # --- KATEGORIYALAR ---
    if query.data == "category_insta":
        insta_text = (
            "📱 **Instagram Xizmatlari**\n\n"
            "• Obunachilar — 1,000 ta / 12,000 so'm\n"
            "• Layklar — 1,000 ta / 4,000 so'm\n"
            "• Prosmotr — 1,000 ta / 2,000 so'm\n\n"
            "Kerakli xizmatni tanlang:"
        )
        keyboard = [
            [InlineKeyboardButton(text="👤 Obunachi sotib olish", callback_data="buy_insta_followers")],
            [InlineKeyboardButton(text="❤️ Layk sotib olish", callback_data="buy_insta_likes")],
            [InlineKeyboardButton(text="👁️ Prosmotr sotib olish", callback_data="buy_insta_views")],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]
        ]
        await query.message.edit_text(insta_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "category_tg":
        tg_text = (
            "✈️ **Telegram Xizmatlari**\n\n"
            "• Kanal Obunachilari — 1,000 ta / 15,000 so'm\n"
            "• Post Prosmotr — 1,000 ta / 1,000 so'm\n"
            "• Reaksiyalar — 1,000 ta / 3,000 so'm\n\n"
            "Kerakli xizmatni tanlang:"
        )
        keyboard = [
            [InlineKeyboardButton(text="👥 Obunachi xarid qilish", callback_data="buy_tg_sub")],
            [InlineKeyboardButton(text="👁️ Prosmotr xarid qilish", callback_data="buy_tg_views")],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]
        ]
        await query.message.edit_text(tg_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "category_yt":
        yt_text = (
            "🎬 **YouTube Xizmatlari**\n\n"
            "• Obunachilar — 1,000 ta / 45,000 so'm\n"
            "• Prosmotr — 1,000 ta / 18,000 so'm\n"
            "• Layklar — 1,000 ta / 10,000 so'm\n\n"
            "Kerakli xizmatni tanlang:"
        )
        keyboard = [
            [InlineKeyboardButton(text="🔔 Obunachi xarid qilish", callback_data="buy_yt_sub")],
            [InlineKeyboardButton(text="▶️ Prosmotr xarid qilish", callback_data="buy_yt_views")],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]
        ]
        await query.message.edit_text(yt_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "category_pubg":
        pubg_text = (
            "🎮 **PUBG Mobile UC Xarid Qilish**\n\n"
            "Kerakli UC paketini tanlang:\n\n"
            "• 60 UC — 15,000 so'm\n"
            "• 325 UC — 65,000 so'm\n"
            "• 660 UC — 125,000 so'm\n"
            "• 1800 UC — 330,000 so'm"
        )
        keyboard = [
            [InlineKeyboardButton(text="🛒 Buyurtma berish", callback_data="buy_uc")],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]
        ]
        await query.message.edit_text(pubg_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    # --- BUYURTMA TUGMALARI JAVOBLARI ---
    elif query.data in ["buy_insta_followers", "buy_insta_likes", "buy_insta_views", 
                        "buy_tg_sub", "buy_tg_views", 
                        "buy_yt_sub", "buy_yt_views", "buy_uc"]:
        order_text = (
            "⚠️ **Balans yetarli emas!**\n\n"
            "Xizmatdan foydalanish uchun avval balansingizni to'ldiring.\n\n"
            "💳 Hisobni to'ldirish bo'limiga o'ting."
        )
        keyboard = [
            [InlineKeyboardButton(text="💳 Balansni to'ldirish", callback_data="add_balance")],
            [InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]
        ]
        await query.message.edit_text(order_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    # --- BALANS VA BUYURTMALAR ---
    elif query.data == "add_balance":
        pay_text = (
            "💳 **Balansni to'ldirish**\n\n"
            "To'lovni amalga oshiring va chekni adminga yuboring:\n"
            "💳 Karta: `4466 1369 5188 2431` (Abduraxmonov Abdulahad)\n\n"
            "To'lov qilgach, chekni administratorga yuboring. Balans 5 daqiqada to'ldiriladi."
        )
        keyboard = [[InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]]
        await query.message.edit_text(pay_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "my_orders":
        orders_text = "📊 **Sizning buyurtmalaringiz:**\n\nHozircha sizda faol buyurtmalar yo'q."
        keyboard = [[InlineKeyboardButton(text="🔙 Orqaga", callback_data="back_to_main")]]
        await query.message.edit_text(orders_text, parse_mode="Markdown", reply_markup=InlineKeyboardMarkup(keyboard))

    elif query.data == "back_to_main":
        await start(update, context)

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    
    print("Bot muvaffaqiyatli ishga tushdi!")
    app.run_polling()