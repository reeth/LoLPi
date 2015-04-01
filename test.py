#!/usr/bin/env python

import time
from riotwatcher import RiotWatcher,EUROPE_WEST
import riotwatcher 

APIKey = 'c190266b-93ad-4496-be0a-84d18878810a'

summoner = ['reeth 26399324', 'crankmind13 24605042', 'Fluegelgraph 40409815', 'BKolrabi 35064136', 'Crankm1nd13 43822576', 'Zy0L0rd 71939928']

w = RiotWatcher(APIKey)

def wait():
	while not w.can_make_request():
		time.sleep(1)


def IsPlaying():
	for summoners in summoner:
	
		try:
	 
			id = summoners.split()
			print('Is %s In Game?') %(id[0])
			currentgame = w.get_current_game(summoner_id=id[1])
			gameId = currentgame['gameId']
			
			gameStartTime = currentgame['gameStartTime']
			platformId = currentgame['platformId']
			gameMode = currentgame['gameMode']
			mapId = currentgame['mapId']
			gameType = currentgame['gameType']
			gameQueueConfigId = currentgame['gameQueueConfigId']
			observers = currentgame['observers']
			encrpytionKey = currentgame['observers']
			
			print "Current Game Stats For %s:\n\nGame Id: %s\nGame Start Time: %s\nPlatform Id: %s\n \
			Game Mode: %s\nMap Id: %s\nGame Type: %s\nGame Queue Config Id: %s\nObservers: %s\nEncryption Key: %s" \
			 %(id[0],gameId, gameStartTime, platformId, gameMode, mapId, gameType, gameQueueConfigId, observers, encrpytionKey)	
			wait()
		
		except riotwatcher.LoLException:
			print('User Is Not In Game')

		except KeyboardInterrupt:
			print('User Aborted')
			break	



def ProfileStats():
	for summoners in summoner:	
		try:		
			name = summoners.split()
			wait()
			s = w.get_summoner(name=name[0], region=EUROPE_WEST)
			profileIconId = s['profileIconId']
			summonerLevel = s['summonerLevel']
			revisionDate  = s['revisionDate']
			revisionDate = str(revisionDate).strip("\r\n\t")
			id = s['id']
			name = s['name']

			print "Profile Stats For %s\n\nProfileIconId: %s\nSummonerLevel: %s\nRevisionDate: \
			%s\nAcount Id: %s\nAcount Name: %s \n\n" %(name,profileIconId,summonerLevel,revisionDate,id,name)
			wait()

		except riotwatcher.LoLException, Err:
			print('503 Service unavailable')
			print Err
			pass

		except KeyboardInterrupt:
			print('User Aborted')
			break



if __name__ == '__main__':
	
	while 1:
	
		try:
	
			ProfileStats()
			IsPlaying()
			print('Waiting 600...')
			time.sleep(600)
	
		except KeyboardInterrupt:
			print('User Aborted')
			break
