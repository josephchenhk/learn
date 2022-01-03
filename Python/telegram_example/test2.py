# -*- coding: utf-8 -*-
# @Time    : 3/1/2022 11:54 am
# @Author  : Joseph Chen
# @Email   : josephchenhk@gmail.com
# @FileName: test2.py

"""
Copyright (C) 2020 Joseph Chen - All Rights Reserved
You may use, distribute and modify this code under the 
terms of the JXW license, which unfortunately won't be
written for another century.

You should have received a copy of the JXW license with
this file. If not, please write to: josephchenhk@gmail.com
"""

from telegram import Update
from telegram.ext import Updater
from telegram.ext import CallbackContext
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters

from Credentials import TELEGRAM_TOKEN

def start(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Telegram bot greetings..."
    )

def echo(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[ECHO] " + update.message.text
    )

def caps(update: Update, context: CallbackContext):
    text_caps = ' '.join(context.args).upper()
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[CAPS] " + text_caps
    )

def unknown(update: Update, context: CallbackContext):
    context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="[UNKNOWN] Sorry, I don't understand that command."
    )

updater = Updater(token=TELEGRAM_TOKEN, use_context=True)

dispatcher = updater.dispatcher

start_handler = CommandHandler('start', start)
echo_handler = MessageHandler(Filters.text & (~Filters.command), echo)
caps_handler = CommandHandler('caps', caps)
unknown_handler = MessageHandler(Filters.command, unknown)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(echo_handler)
dispatcher.add_handler(caps_handler)
dispatcher.add_handler(unknown_handler, group=1)

updater.start_polling()
updater.idle()
updater.stop()


