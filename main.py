import json

from bot import Bot

if __name__ == "__main__":
    bot_army = []
    max_likes = 50

    with open('accounts.json') as json_file:
        bots_data = json.load(json_file)
        for bot_data in bots_data:
            bot_army.append(Bot(bot_data["token"], bot_data["pickup"]))

    for bot in bot_army:
        print("Starting bot")
        bot.autolike(max_likes)
        bot.auto_start_conversations()

