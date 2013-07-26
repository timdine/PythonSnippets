import pyttsx
engine = pyttsx.init()

print engine.getProperty('rate')
print engine.getProperty('volume')
print engine.getProperty('voice')
print engine.getProperty('voices')

engine.setProperty('rate', 130)
engine.setProperty('volume', 1.25)

#engine.say("I can see John Smith")
#engine.say("Bayside, Beechville, Big Lake, Blind Bay, Brookside, Goodwood, Halifax, Hatchet Lake, McGraths Cove, Prospect, Prospect Bay, Shad Bay, Terence Bay, Terence Bay River, Whites Lake")
#engine.say('The power is out in East Pennant, Halifax, Harrietsfield, Sambro, Sambro Creek, West Pennant, Williamswood')
engine.say("Shubenacadie, Musquodoboit, Berwick, Ecum Seecum, Stewiacke")
engine.runAndWait()

