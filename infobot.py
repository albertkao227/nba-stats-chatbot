#!/usr/bin/env python
# -*- coding:utf-8 -*-

import discord
import json
import pandas as pd
import pandasql as ps
from datapuller import DataPuller
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
            
            if msg.strip() == 'ping':
                await message.reply('pong')
            elif msg.strip() == 'ping ping':
                await message.reply('pong pong')
            else:

                filterLIST = []
                resultDICT = runLoki([msg], filterLIST)        
                df = pd.read_csv('./test_data.csv')

                team = resultDICT['team'][0]
                stat = resultDICT['stat'][0]
                level = resultDICT['level'][0]

                if level == '平均':
                    qry = DataPuller.get_agg_stats(stat, 10, team, 2020)
                elif level == '單場':
                    qry = DataPuller.get_single_game_stats(stat, 10, team, 2020)
                else:
                    raise ValueError('invalid input') 

                statDICT = {'pts':['得分'], 
                            'reb':['籃板', '搶籃板'], 'ast':['助攻'], 
                            'blk':['阻攻', '火鍋', '蓋火鍋','搧帽', '蓋帽'], 
                            'stl':['抄截']}

                result = ps.sqldf(qry, locals())
                reply_message = level + statDICT[stat][0] + '最高的是' \
                                + result['player_name'].iloc[0] + ': ' + str(round(result['target_stat'].iloc[0], 2))

                await message.reply(reply_message)
                
        

if __name__ == "__main__":
    
    client = BotClient()
    client.run(accountDICT["discord_token"])

