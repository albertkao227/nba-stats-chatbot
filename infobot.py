#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json
import pandas as pd

from nba_search import * 

with open("account.info", encoding="utf-8") as f:
    accountDICT = json.loads(f.read())


class BotClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {} with id {}'.format(self.user, self.user.id))

    async def on_message(self, message):
        # Don't respond to bot itself. Or it would create a non-stop loop.
        # 如果訊息來自 bot 自己，就不要處理，直接回覆 None。不然會 Bot 會自問自答個不停。
        if message.author == self.user:
            return None

        print("到到來自 {} 的訊息".format(message.author))
        print("訊息內容是 {}。".format(message.content))
        if self.user.mentioned_in(message):
            print("本 bot 被叫到了！")
            msg = message.content.replace("<@!{}> ".format(self.user.id), "")
            if msg == 'ping':
                await message.reply('pong')
            elif msg == 'ping ping':
                await message.reply('pong pong')
            else:
                
                filterLIST = []
                resultDICT = runLoki([msg], filterLIST)        
                df = pd.read_csv('./intent/stats.csv')

                team = resultDICT['team'][0]
                stats = df[(df['team']==team) & (df['season']==2020)]
                player = stats.loc[stats['pts_per_game']==max(stats['pts_per_game'])]  
                output = player['player_name'].values[0] + ' 平均每場得分: ' + str(round(player['pts_per_game'].values[0], 2))

                await message.reply(output)


if __name__ == "__main__":
    
    client = BotClient()
    client.run(accountDICT["discord_token"])

