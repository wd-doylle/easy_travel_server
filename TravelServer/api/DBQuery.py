# -*- coding: utf-8 -*-
import sqlite3
import os

DB_FILE_PATH = "SBsDATASET.db"
TABLE_NAME = ''


def getSceneList(cityID):

    conn = sqlite3.connect(DB_FILE_PATH)
    cur = conn.cursor()
    sql = "SELECT NAME FROM SCENELIST WHERE CITY='%s'"%(cityID)
    cur.execute(sql)
    r = cur.fetchall()
    return [i[0] for i in r]



def getSceneInfo(sceneID):

    conn = sqlite3.connect(DB_FILE_PATH)
    cur = conn.cursor()
    sql = "SELECT * FROM SCENELIST WHERE NAME ='%s'"%(sceneID)
    cur.execute(sql)
    return cur.fetchone()


def getDistance(placeFrom,placeTo):
    
    conn = sqlite3.connect(DB_FILE_PATH)
    cur = conn.cursor()
    sql = "SELECT * FROM DISTANCELIST WHERE ORIGINNAME ='%s' AND DESTINATIONNAME = '%s'"%(placeFrom,placeTo)
    cur.execute(sql)
    return cur.fetchone()


def getHotelList(cityID):

    conn = sqlite3.connect(DB_FILE_PATH)
    cur = conn.cursor()
    sql = "SELECT NAME FROM HOTELLIST WHERE CITY='%s'"%(cityID)
    cur.execute(sql)
    r = cur.fetchall()
    return [i[0] for i in r]


def getHotelInfo(hotelID):

    conn = sqlite3.connect(DB_FILE_PATH)
    cur = conn.cursor()
    sql = "SELECT * FROM HOTELLIST WHERE NAME ='%s'"%(hotelID)
    cur.execute(sql)
    return cur.fetchone()


if __name__ == '__main__':

    sceneList = getSceneList(u"上海".encode('utf-8'))
    for i in sceneList:
        print i,
    sceneInfo = getSceneInfo(u"辰山植物园".encode('utf-8'))
    for i in range(len(sceneInfo)):
        print sceneInfo[i] , i
    print sceneInfo[9]
    print getDistance(u'南翔老街',u'上海杜莎夫人蜡像馆(南京西路)')[3]