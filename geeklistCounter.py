from bs4 import BeautifulSoup
import requests
import operator
import re
import time
from collections import Counter

#add code to count 
## Done #list the combinations of subtype and objecttype
## Done #add username counting
#user with the most builds
## Done #how many builds does a user make
#display the list of builds for a user


theGeeklists = (
#("Jan 2010",50595),("Feb 2010",51588),("Mar 2010",52590),("Apr 2010",53571),("May 2010",54482),("Jun 2010",55395),
#("Jul 2010",56010),("Aug 2010",57209),("Sep 2010",57948),("Oct 2010",59285),("Nov 2010",59943),("Dec 2010",61565),
#("Jan 2011",62652),("Feb 2011",63902),("Mar 2011",64852),("Apr 2011",65972),("May 2011",66913),("Jun 2011",68105),
#("Jul 2011",69247),("Aug 2011",70426),("Sep 2011",71925),("Oct 2011",72852),("Nov 2011",74125),("Dec 2011",76063),
#("Jan 2012",98826),("Feb 2012",121410),("Mar 2012",136659),("Apr 2012",139986),("May 2012",141507),("Jun 2012",142944),
#("Jul 2012",144709),("Aug 2012",145111),("Sep 2012",146652),("Oct 2012",147767),("Nov 2012",149054),("Dec 2012",150365),
#("Jan 2013",151405),("Feb 2013",153114),("Mar 2013",154238),("Apr 2013",155500),("May 2013",156731),("Jun 2013",157988),
#("Jul 2013",159131),("Aug 2013",160495),("Sep 2013",161735),("Oct 2013",162801),("Nov 2013",164779),("Dec 2013",166087),
#("Jan 2014",167533),("Feb 2014",169320),("Mar 2014",170554),("Apr 2014",171805),("May 2014",173066),("Jun 2014",174411),
#("Jul 2014",175533),("Aug 2014",176987),("Sep 2014",178274),("Oct 2014",179755),("Nov 2014",181287),("Dec 2014",182633),
#("Jan 2015",184601),("Feb 2015",186760),("Mar 2015",188103),("Apr 2015",189473),("May 2015",190663),("Jun 2015",191937),
#("Jul 2015",193080),("Aug 2015",194538),("Sep 2015",196100),("Oct 2015",197524),("Nov 2015",199008),("Dec 2015",200255),
#("Jan 2016",202801),("Feb 2016",204614),("Mar 2016",205966),("Apr 2016",207204),("May 2016",208348),("Jun 2016",209529),
#("Jul 2016",208272),("Aug 2016",211766),("Sep 2016",213586),("Oct 2016",215051),("Nov 2016",216499),("Dec 2016",217620),
("Jan 2017",219372),("Feb 2017",221352),("Mar 2017",222622),("Apr 2017",223875),("May 2017",224940)
)

class BoardGame:
	def __init__(self):
		self.name = ""
		self.builds = 0
		self.mostPopularMonth = ""
		self.mostPopularMonthBuilds = 0
		self.mostPopularYear = ""
		self.mostPopularYearBuilds = 0
		self.firstBuild = ""
		self.buildList = []
		self.buildListLinks = []
		self.thumbs = 0
		self.objecttype = ""
		self.subtype = ""
		self.rank = -1
		self.bggItemNumber = 0
		self.mostRecentBuild = ""
		self.plays = 0

def most_common(lst):
	return max(set(lst), key=lst.count)

def occurDict(items):
	d = {}
	for i in items:
		if i in d:
			d[i] = d[i]+1
		else:
			d[i] = 1


foundGames = {}

users = []

subTypeThingList = []

for theGeekList in theGeeklists:
	#print "------------------"
	
	time.sleep(1)
	
	geekListItems = 0
	
	r = requests.get("http://www.boardgamegeek.com/xmlapi/geeklist/"+str(theGeekList[1])+"")
	
	while (r.status_code == 202):
		time.sleep(2)
		print("Got 202, retrying")
		r = requests.get("http://www.boardgamegeek.com/xmlapi/geeklist/"+str(theGeekList[1])+"")
		
	data = r.text

	

	soup = BeautifulSoup(data, 'html.parser')
	print (soup.find_all('numitems'))
	itemNumbers = int(soup.find_all('numitems')[0].text)
	#print "Item Numbers =", itemNumbers
	loopcount = 0
	
	maxNumber = 0
	maxNumberXML = soup
	
	
	
	while (itemNumbers != len(soup.find_all('item')) and loopcount < 1):
		time.sleep(1)
		print ("-", theGeekList[0], "Mismatch in count, getting list again.", itemNumbers, len(soup.find_all('item')), "MaxItems:", maxNumber)
		r = requests.get("http://www.boardgamegeek.com/xmlapi/geeklist/"+str(theGeekList[1])+"")
		data = r.text

		soup = BeautifulSoup(data, 'html.parser')
		itemNumbers = int(soup.find_all('numitems')[0].text)
		loopcount = loopcount + 1
		
		if len(soup.find_all('item')) > maxNumber:
			maxNumber = len(soup.find_all('item'))
			maxNumberXML = soup
			loopcount = 0
		
	soup = maxNumberXML
	
	#~ if itemNumbers < len(soup.find_all('item')):
		#~ print "Not enough found"
	#~ elif itemNumbers == len(soup.find_all('item')):
		#~ print "Equal"
	#~ else:
		#~ print "Too Many"
	
	for link in soup.find_all('item'):
		geekListItems = geekListItems + 1
		try:
			theGameName = (str(link.get('objectname')))
			theGameType = (str(link.get('subtype')))
			theGameObjectType = (str(link.get('objecttype')))
			theBGGItemNumber = (str(link.get('objectid')))
			#print theGameName, theGameType, theGameObjectType
			subtypeThing = theGameObjectType + "_" + theGameType
			subTypeThingList.append(subtypeThing)

			#if theGameObjectType == "thread"
				
			if theGameType == "boardgame" or theGameObjectType == "thread":
				#print link.text
				users.append(str(link.get('username')))
				imageList = re.findall(r"\[ImageID=.*\]", link.text)
				newImageList = []
				for item in imageList:
					newitem = item
					newitem = newitem.replace("medium", "")
					newitem = newitem.replace("small", "")
					newitem = newitem.replace("large", "")
					newitem = newitem.replace("inline", "")
					newitem = newitem.replace("[/center]", "")
					newitem = newitem.replace(" ", "")
					newImageList.append(newitem)
				imageList = re.findall(r"\[imageid=.*\]", link.text)
				for item in imageList:
					newitem = item
					newitem = newitem.replace("medium", "")
					newitem = newitem.replace("small", "")
					newitem = newitem.replace("large", "")
					newitem = newitem.replace("inline", "")
					newitem = newitem.replace("[/center]", "")
					newitem = newitem.replace("[/floatleft]", "")
					newitem = newitem.replace("[/floatright]", "")
					newitem = newitem.replace(" ", "")
					newImageList.append(newitem)
				#[ImageID=1259818]
				
				#print theGameName
				if (theGameName in foundGames.keys()):
					foundGames[theGameName].builds = foundGames[theGameName].builds + 1
					foundGames[theGameName].buildList.append(theGeekList[0])
					foundGames[theGameName].buildListLinks.append("[URL]http://www.boardgamegeek.com/geeklist/"+str(theGeekList[1])+"/item/"+str(link.get('id'))+"#item"+str(link.get('id'))+"[/URL]")
					foundGames[theGameName].thumbs += int(link.get('thumbs'))
				else:
					bg = BoardGame()
					bg.name = theGameName
					bg.builds = 1
					bg.buildList = [theGeekList[0]]
					bg.buildListLinks.append("[URL]http://www.boardgamegeek.com/geeklist/"+str(theGeekList[1])+"/item/"+str(link.get('id'))+"#item"+str(link.get('id'))+"[/URL]")
					bg.thumbs = int(link.get('thumbs'))
					bg.subtype = theGameType
					bg.objecttype = theGameObjectType
					bg.bggItemNumber = theBGGItemNumber
					foundGames[theGameName] = bg
				foundGames[theGameName].buildListLinks.extend(newImageList)
				
		except:
			test = 2
	print (theGeekList[0], geekListItems)


##


ranksDict = {}
playsDict = {}
maxPlays = 0
ranksInFile = open("bggRanks.txt", "r")
for row in ranksInFile:
	rowList = row.split(",")
	ranksDict[rowList[0]] = rowList[1]
	playsDict[rowList[0]] = int(rowList[2])
	if (int(rowList[2]) > maxPlays):
		maxPlays = int(rowList[2])
		print "Max Plays", maxPlays
ranksInFile.close()

ranksOutFile = open("bggRanks.txt", "a")

print ("Calculating build counts")
for key in foundGames.keys():
	#print key
	popularMonths = []
	popularYears = []
	for monthYear in foundGames[key].buildList:
		monthYearList = monthYear.split(" ")
		popularMonths.append(monthYear)
		popularYears.append(monthYearList[1])
	mostCommonMonth = most_common(popularMonths)
	mostCommonYear = most_common(popularYears)
	foundGames[key].mostPopularMonth = mostCommonMonth
	foundGames[key].mostPopularMonthBuilds = popularMonths.count(mostCommonMonth)
	foundGames[key].mostPopularYear = mostCommonYear
	foundGames[key].mostPopularYearBuilds = popularYears.count(mostCommonYear)
	getRanks = 1
	if getRanks == 1:
		if foundGames[key].subtype == "boardgame":
			if foundGames[key].bggItemNumber in ranksDict.keys():
				foundGames[key].rank = ranksDict[foundGames[key].bggItemNumber]
				foundGames[key].plays = playsDict[foundGames[key].bggItemNumber]
			else:
				time.sleep(2)
				try:
					print "link:   http://www.boardgamegeek.com/xmlapi2/thing?stats=1&id="+str(foundGames[key].bggItemNumber)+"&thing=boardgame"
					r=requests.get("http://www.boardgamegeek.com/xmlapi2/thing?stats=1&id="+str(foundGames[key].bggItemNumber)+"&thing=boardgame")	
					while (r.status_code == 202):
						time.sleep(2)
						print("Got 202, retrying")
						r=requests.get("http://www.boardgamegeek.com/xmlapi2/thing?stats=1&id="+str(foundGames[key].bggItemNumber)+"&thing=boardgame")
						
					data = r.text

					

					soup = BeautifulSoup(data, 'html.parser')
					theRankObject = (soup.find_all('rank')[0])
					theGameRank = (str(theRankObject.get('value')))
					print(foundGames[key].name, theGameRank, foundGames[key].bggItemNumber)
					
					if (theGameRank == "Not Ranked"):
						theGameRank = -1
					foundGames[key].rank = theGameRank
					
					
					
					
					print "link:   https://www.boardgamegeek.com/xmlapi2/plays?id="+str(foundGames[key].bggItemNumber)+"&thing=boardgame"
					r=requests.get("https://www.boardgamegeek.com/xmlapi2/plays?id="+str(foundGames[key].bggItemNumber)+"&thing=boardgame")	
					while (r.status_code == 202):
						time.sleep(2)
						print("Got 202, retrying")
						r=requests.get("https://www.boardgamegeek.com/xmlapi2/plays?id="+str(foundGames[key].bggItemNumber)+"&thing=boardgame")
						
					data = r.text

					

					soup = BeautifulSoup(data, 'html.parser')
					theRankObject = (soup.find_all('plays')[0])
					thePlays = (str(theRankObject.get('total')))
					print "The game has this many plays:", thePlays
					print(foundGames[key].name, theGameRank, foundGames[key].bggItemNumber)
					foundGames[key].plays = thePlays
					
					ranksOutFile.write(str(foundGames[key].bggItemNumber)+","+str(theGameRank)+","+str(thePlays)+"\n")
					
				except:
					foundGames[key].rank = 0
				#itemNumbers = int(soup.find_all('numitems')[0].text)
				
			
ranksOutFile.close()
gamesBuiltOnce = 0


print ("Printing Games")
for i in reversed(range(maxPlays)):
	#for key, value in sorted(foundGames.iteritems(), key=operator.itemgetter(1)):
	for key in foundGames.keys():
		#if foundGames[key].builds == i and i >0:
		#if foundGames[key].thumbs == i and i > 1:
		#print key, foundGames[key].plays, i
		if foundGames[key].plays == i and i >1 and foundGames[key].builds > 5:
		#if int(foundGames[key].rank) == i and foundGames[key].builds > 1:
			print ("---------------------------------------------------------------------------------------------------")
			print ("---------------------------------------------------------------------------------------------------")
			#print ("---------------------------------------------------------------------------------------------------")
			print key
			print "Type:", foundGames[key].objecttype, foundGames[key].subtype
			print "Builds:", foundGames[key].builds
			print "Thumbs:", foundGames[key].thumbs
			print "Plays:", foundGames[key].plays
			print "BGG Rank:", foundGames[key].rank
			print "Most Popular Year:", foundGames[key].mostPopularYear, "-", foundGames[key].mostPopularYearBuilds, "builds"
			print "Most Popular Month:", foundGames[key].mostPopularMonth, "-", foundGames[key].mostPopularMonthBuilds, "builds"
			for theLink in foundGames[key].buildListLinks:
				if "Image" in theLink:
					print (theLink)
				else:
					print ("")
					print (theLink)
		if foundGames[key].builds == 1 and i == 1:
			gamesBuiltOnce = gamesBuiltOnce + 1

print "Total Unique Games:", len(foundGames.keys())
print "Games built Once:", gamesBuiltOnce

print ("-------------------------------------------------------------------------------")
print ("Build by user")
theCounter = Counter(users)
for item in theCounter.most_common():
	print (item[0], item[1])

print ("-------------------------------------------------------------------------------")
print ("Types of objects")
theTypesCounter = Counter(subTypeThingList)
for item in theTypesCounter.most_common():
	print (item[0], item[1])

#~ for i in reversed(range(100)):
	#~ #for key, value in sorted(foundGames.iteritems(), key=operator.itemgetter(1)):
	#~ for key in sorted(foundGames.iterkeys()):
		#~ if foundGames[key] == i:
			#~ print key, ':', foundGames[key]
	
