from ServerApp.model.s_wcg_player import s_wcg_player
from ServerApp import db
from flask import jsonify

def showWorldRank():
    playerItemArray = s_wcg_player.query.order_by(db.desc(s_wcg_player.bestScore)).all()[0:50]
    jsonArray = []
    index = 0
    for playerItem in playerItemArray:
        jsonItem = {"index": index, "data": {"id": playerItem.id, "wxid": playerItem.wxid, "name": playerItem.name,
                                             "head": playerItem.head,"bestScore": playerItem.bestScore, "bestCombo": playerItem.bestCombo,"coin":playerItem.coin,
                                             "curSkin": playerItem.curSkin,
                                             "store": {"ball1": playerItem.ball_1,"ball2": playerItem.ball_2,
                                                       "ball3": playerItem.ball_3, "ball4": playerItem.ball_4,
                                                       "ball5": playerItem.ball_5,"ball6": playerItem.ball_6,
                                                       "ball7": playerItem.ball_7,"ball8": playerItem.ball_8}}}
        jsonArray.append(jsonItem)
        index = index + 1
    return jsonify(jsonArray)

def getSelfData(wxid):
    playerItem = s_wcg_player.query.filter(s_wcg_player.wxid == wxid).first()
    if(playerItem):
        jsonItem = {"id": playerItem.id, "wxid": playerItem.wxid, "name": playerItem.name,
                                             "head": playerItem.head, "bestScore": playerItem.bestScore,
                                             "bestCombo": playerItem.bestCombo,"coin":playerItem.coin,"curSkin": playerItem.curSkin,
                                             "store": {"ball1": playerItem.ball_1, "ball2": playerItem.ball_2,
                                                       "ball3": playerItem.ball_3, "ball4": playerItem.ball_4,
                                                       "ball5": playerItem.ball_5, "ball6": playerItem.ball_6,
                                                       "ball7": playerItem.ball_7, "ball8": playerItem.ball_8}}
    else:
        jsonItem = {"id": 0, "wxid": 0, "name": 0,
                    "head":0, "bestScore": 0,
                    "bestCombo": 0,"coin":0,"curSkin":1,
                    "store": {"ball1": 1, "ball2": 0,
                              "ball3": 0, "ball4": 0,
                              "ball5": 0, "ball6": 0,
                              "ball7": 0, "ball8": 0}}
    return jsonify(jsonItem)

def buyItems(wxid,itemNum,sale):
    playerItem = s_wcg_player.query.filter(s_wcg_player.wxid == wxid).first()
    if int(itemNum) == 1:
        playerItem.ball_1 = 1
    elif int(itemNum) == 2:
        playerItem.ball_2 = 1
    elif int(itemNum) == 3:
        playerItem.ball_3 = 1
    elif int(itemNum) == 4:
        playerItem.ball_4 = 1
    elif int(itemNum) == 5:
        playerItem.ball_5 = 1
    elif int(itemNum) == 6:
        playerItem.ball_6 = 1
    elif int(itemNum) == 7:
        playerItem.ball_7 = 1
    elif int(itemNum) == 8:
        playerItem.ball_8 = 1
    playerItem.coin = playerItem.coin - int(sale)
    playerItem.curSkin = int(itemNum)
    db.session.commit()
    return

def submitData(wxid,bestScore,bestCombo,coin,name,head):
    playerItem = s_wcg_player.query.filter(s_wcg_player.wxid == wxid).first()
    if (playerItem):
        if( int(bestScore) > playerItem.bestScore):
            playerItem.bestScore = int(bestScore)
        if( int(bestCombo) > playerItem.bestCombo):
            playerItem.bestCombo = int(bestCombo)
        playerItem.coin = playerItem.coin + int(coin)
    else:
        newPlayerItem = s_wcg_player(
            wxid = wxid,
            name = name,
            head= head,
            bestScore = bestScore,
            bestCombo= bestCombo,
            coin= coin,
            ball_1=1,
            ball_2=0,
            ball_3=0,
            ball_4=0,
            ball_5=0,
            ball_6=0,
            ball_7=0,
            ball_8=0,
            curSkin=1
        )
        db.session.add(newPlayerItem)
    db.session.commit()
    return

