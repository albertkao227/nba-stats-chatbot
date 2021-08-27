#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
    Loki module for player

    Input:
        inputSTR      str,
        utterance     str,
        args          str[],
        resultDICT    dict

    Output:
        resultDICT    dict
"""

import json

DEBUG_player = True

with open("./intent/nba_teams.json", encoding="utf-8") as f:
    teamDICT = json.loads(f.read())


def get_team(resultDICT, args):
    for i in range(len(args)):
        for key in teamDICT.keys():
            if args[i] in teamDICT[key]:
                resultDICT['team'].append(args[i])
    return resultDICT


# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_player:
        print("[player] {} ===> {}".format(inputSTR, utterance))


def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT["team"] = []
    if utterance == "[公牛][主力]是誰":
        resultDICT = get_team(resultDICT, args)

    if utterance == "[公牛]誰是[主力]":
        resultDICT = get_team(resultDICT, args)

    if utterance == "誰是[公牛][最強]的球員":
        resultDICT = get_team(resultDICT, args)

    if utterance == "誰是[公牛]的[主力]":
        resultDICT = get_team(resultDICT, args)

    if utterance == "誰是[公牛]籃球[最強]的球員":
        resultDICT = get_team(resultDICT, args)

    return resultDICT