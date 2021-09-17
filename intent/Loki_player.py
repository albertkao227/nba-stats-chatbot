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

statDICT = {'pts':['得分'], 
            'reb':['籃板', '搶籃板'], 'ast':['助攻'], 
            'blk':['阻攻', '火鍋', '蓋火鍋','搧帽', '蓋帽'], 
            'stl':['抄截']}

aggDICT = {'平均':['場均'], '單場':['一場']}

levelDICT = {'平均':['平均', '場均'], '單場':['單場', '一場']}

#stat_index = {'得分': 'pts', '籃板': 'reb', '助攻':'ast', '阻攻':'stl', '抄截':'blk' }


def get_team(resultDICT, args):
    """Get NBA team name"""
    print(args)
    for i in range(len(args)):
        for key in teamDICT.keys():
            if args[i] in teamDICT[key]:
                resultDICT['team'].append(key)
    return resultDICT


def get_stat(resultDICT, args):
    """Get target stats"""
    print(args)
    for i in range(len(args)):
        for key in statDICT.keys():
            if args[i] in statDICT[key]:
                resultDICT['stat'].append(key)
    return resultDICT


def get_level(resultDICT, args):
    """Get stats aggregation level"""
    print(args)
    for i in range(len(args)):
        for key in levelDICT.keys():
            if args[i] in levelDICT[key]:
                resultDICT['level'].append(key)
    return resultDICT


def get_team(resultDICT, args):
    """Get NBA team name"""
    print(args)
    for i in range(len(args)):
        for key in teamDICT.keys():
            if args[i] in teamDICT[key]:
                resultDICT['team'].append(key)
    return resultDICT


# 將符合句型的參數列表印出。這是 debug 或是開發用的。
def debugInfo(inputSTR, utterance):
    if DEBUG_player:
        print("[player] {} ===> {}".format(inputSTR, utterance))


def getResult(inputSTR, utterance, args, resultDICT):
    debugInfo(inputSTR, utterance)
    resultDICT['team'] = []
    resultDICT['stat'] = []
    resultDICT['level'] = []
    if utterance == "[公牛][主力]是誰":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[公牛]誰是[主力]":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "誰是[公牛][最強]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "誰是[公牛]的[主力]":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "誰是[公牛]籃球[最強]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[2019][公牛隊][平均][得分][最多]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[2019][公牛隊][平均][得分]超過[30]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[2019][球季][公牛隊][平均][得分][最多]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[2019][球季][公牛隊][平均][得分]超過[30]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[2019年][公牛隊][平均][得分][最多]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    if utterance == "[2019年][公牛隊][平均][得分]超過[30]的球員":
        resultDICT = get_team(resultDICT, args)
        resultDICT = get_stat(resultDICT, args)
        resultDICT = get_level(resultDICT, args)

    return resultDICT