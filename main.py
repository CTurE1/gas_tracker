from telegram import Bot, Update
from telegram.ext import CommandHandler, CallbackContext, Updater
import httpx

TOKEN = 'Your_token'
INFURA_URL = 'https://mainnet.infura.io/v3/Your_id'


def get_gas_price(update: Update, context: CallbackContext) -> None:
    response = httpx.post(INFURA_URL, json={
        "jsonrpc": "2.0",
        "id": 1,
        "method": "eth_gasPrice",
        "params": []
    })
    data = response.json()
    gas_price_wei = int(data['result'], 16)
    gas_price_gwei = gas_price_wei / (10**9)
    update.message.reply_text(f"Current gas price is: {gas_price_gwei:.2f} Gwei")

def main() -> None:
    updater = Updater(token=TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("gas", get_gas_price))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()