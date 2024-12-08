"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Содержит локально API_KEY, без ипорта на GIT
import settings

import ephem

import logging
# Enable logging
logging.basicConfig(filename="bot.log", level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")



async def greeting_user(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    print("Вызвана команда /start")
    user = update.effective_user
    # print(user)
    # print(update)
    # print(1/0)
    await update.message.reply_html(
        rf"""Привет уважаемый {user.mention_html()}! 
            Бот работает в двух режимах:
            1. Повторяет ваши сообщения
            2. Дает информацию о созвездии в котором находится указанная вами планета.
            Пример команды, чтобы узнать созвездине: 
            \planet Mars
            Поддерживаютя планеты: Jupiter, Mars, Mercury, Moon, Neptune, Pluto, Saturn, Sun, Uranus, Venus
            """,
        reply_markup=ForceReply(selective=True),
    ) 


async def talk_to_me(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    text = update.message.text
    print(text)
    await update.message.reply_text(f'Ваше сообщение: {text}')    


async def planet_constellation_now(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /planet {planet} is issued."""
    print("Вызвана команда /planet")
    planet = update.message.text.split()[-1].lower().capitalize()
    print(planet)
    if planet == 'Jupiter':
        pl_const = ephem.Jupiter()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Mars':
        pl_const = ephem.Mars()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Mercury':
        pl_const = ephem.Mercury()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Moon':
        pl_const = ephem.Moon()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Neptune':
        pl_const = ephem.Neptune()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Pluto':
        pl_const = ephem.Pluto()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Saturn':
        pl_const = ephem.Saturn()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Sun':
        pl_const = ephem.Sun()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Uranus':
        pl_const = ephem.Uranus()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)
    elif planet == 'Venus':
        pl_const = ephem.Venus()
        pl_const.compute()
        constellation_now = ephem.constellation(pl_const)                        
    else:
        planet = f'Неизвестная планета - {planet}'
        constellation_now = 'Неизвестное созвездие'


    await update.message.reply_text(f'Созвездие на текущий момент для планеты {planet}: {constellation_now} ')



def main():

    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token(settings.API_KEY).build()

    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", greeting_user))
    application.add_handler(CommandHandler("planet", planet_constellation_now))

    # on non command i.e message - echo the message on Telegram
    # application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))


    # talk to me with text 
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, talk_to_me))    

    logging.info("Bot Started!")

    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

    logging.info("Bot Started!")



if __name__ == "__main__":
    main()
