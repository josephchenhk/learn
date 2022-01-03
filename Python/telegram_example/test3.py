# -*- coding: utf-8 -*-
# @Time    : 3/1/2022 3:10 pm
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test3.py.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the 
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

from telegram import Bot
from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from Credentials import TELEGRAM_TOKEN

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[ECHO] " + update.message.text
    )

def stop(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Terminate QTrader..."
    )

class TelegramBot:

    def __init__(self, token: str):
        self.bot = Bot(token=token)
        print(self.bot.get_me())

        # Handle responses
        self.updater = Updater(token=token, use_context=True)
        dispatcher = self.updater.dispatcher
        stop_handler = CommandHandler('stop', stop)
        echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
        dispatcher.add_handler(echo_handler)
        self.updater.start_polling()

    def close(self):
        self.updater.stop()

    def get_updates(self):
        self.updates = self.bot.get_updates()
        print(self.updates[0])

    def send_message(self, chat_id: int, msg: str):
        # chat_id = updates[0].message.from_user.id
        self.bot.send_message(
            chat_id=chat_id,
            text=msg
        )


if __name__=="__main__":
    bot = TelegramBot(token=TELEGRAM_TOKEN)

    # send msg to bot in your phone

    bot.get_updates()
    chat_id = bot.updates[0].message.from_user.id
    bot.send_message(chat_id=chat_id, msg="Yes I am here!")

    print()

    bot.close()

    print("Closed.")


