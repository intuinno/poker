value = {"A":0, "2":10, "3":20, "4":30, "5":40, "6":50, "7":60, "8":70, "9":80, "T":90, "J":100, "Q":110, "K":120}
suit = {"C":1, "D":2, "H":3, "S":4}
handHashTable = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] #ace through king, this is the default
suitHashTable = {"C":0, "D":0, "H":0, "S":0} #clubs, diamonds, hearts, spades in that order
currentHand = []
finalValue = 0


def highAceHash():
	value["A"] = 140

def lowAceHash():
	value["A"] = 10

def rankCard(card):
	return value[card[0]] + suit[card[1]]

def initHash(valueArray):
	for i in range(0, len(valueArray)):
		handHashTable[valueArray[i] / 10] += 1

	for i in range(0, len(currentHand)):
		suitHashTable[(currentHand[i])[1]] += 1

#resets our hand hash table to default
def reset():
	for i in range(0, len(handHashTable)):
		handHashTable[i] = 0

	for i in range(0, len(suitHashTable)):
		suitHashTable[i] = 0

	for i in range(0, len(currentHand)):
		currentHand.pop()

	finalValue = 0

#checks our hand for a pair
def existsPair():
	for i in range(0, handHashtable):
		if handHashTable[i] == 2:
			return True
	return False

#checks our hand for 2 pairs
def existsTwoPairs():
	pairs = 0
	for i in range(0, len(handHashTable)):
		if handHashTable[i] == 2:
			pairs++

	if pairs >= 2:
		return True
	else:
		return False

#checks for three-of-a-kind
def existsTOaK():
	for i in range(0, len(handHashTable)):
		if handHashTable[i] == 3:
			return True
	return False

#checks for straight
def existsStraight():
	for i in range(0, len(handHashTable) - 4):
		if handHashTable[i] > 0 and handHashTable[i + 1] > 0 and handHashTable[i + 2] > 0 and handHashTable[i + 3] > 0 and handHashTable[i + 4] > 0:
			return True
	return False

#checks for flush
def existsFlush():
	for i in suitHashTable:
		if suitHashTable[i] >= 5:
			return True
	return False

#checks for full house
def existsFullHouse():
	pair = False
	toak = False
	for i in range(0, len(handHashTable)):
		if handHashTable[i] == 3:
			toak = True
		elif handHashTable[i] == 2:
			pair = True
	return toak and pair

#checks for four-of-a-kind
def existsFOaK():
	for i in range(0, len(handHashTable)):
		if handHashTable[i] == 4:
			return True
	return False

#the inputs are cards. this function is where we figure out what hand we have
def evaluateHand(currentHand):
	valueArray = []
	for j in currentHand:
		valueArray.append(rankCard(j))

	initHash(valueArray)
	if existsFOaK() == True:
		finalValue = 7
	elif existsFullHouse() == True:
		finalValue = 6
	elif existsFlush() == True:
		finalValue = 5
	elif existsStraight() == True:
		finalValue = 4
	elif existsTOaK() == True:
		finalValue = 3
	elif existsTwoPairs() == True:
		finalValue = 2
	elif existsPair() == True:
		finalValue = 1
	else:
		finalValue = 0