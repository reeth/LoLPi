#!/usr/bin/env python
# -*- coding: utf-8 -*-
from riotwatcher import RiotWatcher
import riotwatcher
import json, time, sys, datetime, re
from time import gmtime, strftime
from datetime import datetime
from pytz import timezone
fmt = "%Y-%m-%d %H:%M:%S"
# Current time in UTC
now_utc = datetime.now(timezone('UTC'))
# Convert to US/Pacific time zone
now_pacific = now_utc.astimezone(timezone('US/Pacific'))
# Convert to Europe/Berlin time zone
zeit = now_pacific.astimezone(timezone('Europe/Berlin'))
print zeit.strftime(fmt)

from riotwatcher import EUROPE_WEST 
w = RiotWatcher('') #API Key for RIOT
print(w.can_make_request())
euw = RiotWatcher('', default_region=EUROPE_WEST)

UIDS = ['26399324',  '24605042', '40409815', '35064136', '43822576']



for UserId in UIDS:
	try:
		#Obtain User Details Via UIDS
		currentgame = euw.get_current_game(summoner_id=UserId)
		#Quick Hack Saves Learning Parsing Python Json LOL
		data = re.compile('.*')
		stats = data.findall(json.dumps(currentgame, indent=4))

		#Grab The GameId From The Json Request.
		gameId = stats[2].split()
		gameId = gameId[1].strip()

		#Grab The GameStartTime From The Json Request.
		gameStartTime = stats[4].split()
		gameStartTime = gameStartTime[1]

		#Grab The PlatformId From The Json Request.
		platformId = stats[6].split()
		platformId = platformId[1]

		#Grab The GameMode From The Json Request.
		gameMode = stats[8].split()
		gameMode = gameMode[1]

		#Grab The MapId From The Json Request.
		mapId = stats[10].split()
 		mapId = mapId[1]

		#Grab The GameType From The Json Request.
		gameType = stats[12].split()
		gameType = gameType[1]

		#Grab The GameQueueConfigId From The Json Request.
		gameQueueConfigId = stats[14].split()
		gameQueueConfigId = gameQueueConfigId[1]

		#Grab The Observers From The Json Request.
		observers = stats[16].split()
		observers = observers[1]
		
		encryptionKey = stats[18].split()
		encryptionKey = encryptionKey[1]

		#Print All The Stats If User Is Online 
		print "Printing Stats\n"


		print("GameId: %s\nGameStartTime: %s\nPlatformId: %s\nGameMode: %s\nMapId: %s \nGameType: %s\nGameQueueConfigId: %s\n Observers:%s\n EncryptionKey: %s\n" \
		
		%(gameId,gameStartTime,platformId,gameMode,mapId,gameType,gameQueueConfigId,observers,encryptionKey))
		#^^^^^^^^^^^^^^^^^^^^^^^^^^^^ Defines The Values to be  put in the print statement^^^^^^^^^^^^^^^^^# 

		


	except riotwatcher.LoLException, Err:
		print('User %s Possibly Offline %s' %(UserId, Err))
