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


info_fields = {'season': None,
                'team': None,
                'player': None,
                'stat': None,
                'level': None} 

statDICT = {'pts':['得分'], 
            'reb':['籃板', '搶籃板'], 'ast':['助攻'], 
            'blk':['阻攻', '火鍋', '蓋火鍋','搧帽', '蓋帽'], 
            'stl':['抄截']}

seasonDICT = {'2016':['2016', '2016球季', '2016賽季', '二零一六球季', '二零一六賽季'], 
              '2017':['2017', '2017球季', '2017賽季', '二零一七球季', '二零一七賽季'],
              '2018':['2018', '2018球季', '2018賽季', '二零一八球季', '二零一八賽季'],
              '2019':['2019', '2019球季', '2019賽季', '二零一九球季', '二零一九賽季'],
              '2020':['2020', '2020球季', '2020賽季', '二零二零球季', '二零二零賽季']}


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
                
                df = pd.read_csv('./test_data.csv')

                for name in list(set(df['player_name'])):
                    if name in msg:
                        info_fields['player'] = name
                        msg = msg.replace(name, '').strip()
                        
                for season_key in seasonDICT.keys():
                    for year in seasonDICT[season_key]:
                        if year in msg:
                            info_fields['season'] = season_key
                            msg = msg.replace(year, '').strip()

                filterLIST = []
                resultDICT = runLoki([msg], filterLIST)   
                
                if len(resultDICT['team']) > 0:
                    info_fields['team'] = resultDICT['team'][0]
                
                info_fields['stat'] = resultDICT['stat'][0]
                info_fields['level'] = resultDICT['level']

                if info_fields['player'] and info_fields['level'] == 'avg':
                    qry = DataPuller.get_player_agg_stats(info_fields['stat'], 
                                                          info_fields['player'], 
                                                          info_fields['season'])

                elif info_fields['player'] and info_fields['level'] == 'single':
                    qry = DataPuller.get_player_single_game_stats(info_fields['stat'], 
                                                                  info_fields['player'], 
                                                                  info_fields['season'])
                elif info_fields['team']:
                    qry = DataPuller.get_team_best_player_stats(info_fields['stat'], 
                                                                info_fields['team'], 
                                                                info_fields['season'])

                else:
                    raise ValueError('invalid input') 


                result = ps.sqldf(qry, locals())

                await message.reply(result)
                
        

if __name__ == "__main__":
    
    client = BotClient()
    client.run(accountDICT["discord_token"])

