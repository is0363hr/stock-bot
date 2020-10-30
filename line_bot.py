
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)
import os
import sys

# 上の階層を見る方法
# sys.path.append('../')
from randomClass import StockPridict

app = Flask(__name__)

# 環境変数取得
# YOUR_CHANNEL_ACCESS_TOKEN = os.environ["YOUR_CHANNEL_ACCESS_TOKEN"]
# YOUR_CHANNEL_SECRET = os.environ["YOUR_CHANNEL_SECRET"]

line_bot_api = LineBotApi(YOUR_CHANNEL_ACCESS_TOKEN)
handler = WebhookHandler(YOUR_CHANNEL_SECRET)

if YOUR_CHANNEL_SECRET is None:
    print('Specify LINE_CHANNEL_SECRET.')
    sys.exit(1)
if YOUR_CHANNEL_ACCESS_TOKEN is None:
    print('Specify LINE_CHANNEL_ACCESS_TOKEN.')
    sys.exit(1)


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    stock = StockPridict()
    # event.message.textに入力されたものが入ってる
    if '株くんおはよう' == event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='明日晴れるよ！'))
    elif '株くん株価予測の精度は？' == event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=str(stock.processing_accuracy())))
    elif '株くん明日の株価は？' == event.message.text:
        result = stock.processing_predict()
        if result == 1:
            t = '株価が上がるよ！'
        elif result == -1:
            t = '株価が下がるよ！'
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=t))
    elif '株くんは何を予測してるの？' == event.message.text:
        stock = StockPridict()
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='野村総研の株価だよ！'))
    elif '株くん' == event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='「株くん明日の株価は？」って聞いてくれたら明日の株価を予測するよ！！'))
    elif '株くんこんにちは' == event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text='ブラジルは夜だよー'))
    elif '株くん' in event.message.text:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    #    app.run()
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
