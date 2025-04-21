from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Selamat datang di bot TerebiNoona\n\n"
"Berikut daftar channel by TerebiNoona\n"
"1. [Channel 18+](https://t.me/+e6whMC4GCuI5NWQ1) (channel utama)\n"
"2. [PASSION](https://t.me/+6UUWWH6QB6E1YzZl)\n"
"3. [Eternal Covenant](https://t.me/+FN3jPeOm7g41N2E9)\n"
"4. [Channel Shonen ai](https://t.me/+iHvn3LfkY3c4MGM1)\n"
"    => Hunter's gonna lay low\n"
"    => Honbul\n"
"    => To the fans not to me\n"
"    => 3 setengah\n"
"    => Nevermind darling\n\n"
"Jika ingin berkomunikasi dengan TerebiNoona, silahkan balas pesan ini",
parse_mode="markdown"
    )

app = Application.builder().token("6712410435:AAGmawfwIYrpLZuE4J3Me54BXVG9SkVTfME").build()
app.add_handler(CommandHandler("start", start))
app.run_polling()