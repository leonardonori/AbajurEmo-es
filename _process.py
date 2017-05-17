# -*- coding: utf-8 -*-
import sys
sys.path.append("dir_path")

import json
from _connection import *
from ibm import *

def getTweets(cursor):
    resp = []
    query = "SELECT id_tweet, tweet FROM tweets WHERE status = 0 ";
    cursor.execute(query)
    rows = cursor.fetchall()

    for row in rows:
        temp = {'id':row[0], 'tweet':row[1]}
        resp.append(temp)

    return resp

def getEmotion(response):

    array = (response)
    j = len(array);
    i = 0;
    positive = 0
    negative = 0
    for row in array:
        if row['tone_id'] == "joy":
            positive += row['score']
        else:
            negative += row['score']
    #verificar se é neutro
    if (
        (positive >= negative * 0.75 and positive <= negative * 1.15)
        or
        (negative >= positive * 0.75 and negative <= positive * 1.15)
        ):
        return 1
    #verificar se é positive
    if (positive > negative):
        return 2
    #se não for é negative
    return 0

def updateTweet(tweet, value, cursor):

    query = "UPDATE tweets SET status = 1 WHERE id_tweet = "+str(tweet['id'])
    cursor.execute(query)
    query = "SELECT id_signal, signal_status FROM signal_status WHERE id_signal = (SELECT MAX(id_signal) FROM signal_status)";
    cursor.execute(query)

    row = cursor.fetchall()
    current_val = row[0][1]
    if current_val < value:
        newValue = current_val + 1
    elif current_val > value:
        newValue = current_val - 1
    else:
        newValue = current_val

    if newValue < 0:
        newValue = 0
    elif newValue > 2:
        newValue = 2
    query = "UPDATE signal_status set signal_status = "+str(newValue)+ " WHERE id_signal = "+str(row[0][0])
    cursor.execute(query)

def updateDB():
    db = getConnection()
    cursor = db.cursor()
    tweets = getTweets(cursor)
    for tweet in tweets:
        emotion =  getJson(tweet['tweet'])
        value = getEmotion(emotion)
        updateTweet(tweet, value, cursor)
    db.commit()
    cursor.close()
    db.close();
