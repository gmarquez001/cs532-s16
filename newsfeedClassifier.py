# -*- coding: UTF-8 -*-
import feedparser 
import unicodedata
import ConfigParser
import sys 

sys.path.insert(0, '../lib/chapter6')
from docclass import *

def createHeadings(format=None):
	if format:
		if format == 'latex':
			return columnTitles = '{title} & {predictedCategory} & {actualCategory} & {cProb} & {fisherProb} & \\\\\\hline'.format(title='Title',predictedCategory='Predicted Category',actualCategory='Actual Category',cProb='cProb()',fisherProb='fisherProb()')

def printClassifierResults(classifiedFeeds):
	pass 

def readTrainingData(dataFileName):
	# Read the training_data
	trainData = None
	try:
		fileN = open(dataFileName,'r')
		trainData = {}
		for line in fileN.readlines():
			tmp = line.split('|')
			trainData[int(tmp[0])] = tmp[1].strip('\n')

	except IOError as e:
		sys.stderr.write('Error opening training data file: {0}, {1}\n'.format(dataFileName,e[1]))
	return trainData

def readCategories(categoryFileName):
	# Read the categories 
	categories = None
	try:
		v = open(categoryFileName,'r')
		v.close()
		categories = [line.strip('\n') for line in file(categoryFileName)]
	except IOError as e:
		sys.stderr.write('Error opening category list file: {0}, {1}\n'.format(categoryFileName,e[1]))
	return categories

def createIdsToEntries(feedNameFile):
	# Create a dictionary mapping article ids to entries
	idsToEntries = None
	try:
		v = open(feedNameFile,'r')
		v.close()
		d = feedparser.parse(feedName)
		idsToEntries = {}
		for e in d.entries:
			idsToEntries[int(e['articleid'])] = e
	except IOError as e:
		sys.stderr.write('Error opening feed file: {0}, {1}\n'.format(feedNameFile,e[1]))

	return idsToEntries




if __name__ =='__main__':
	config = ConfigParser.ConfigParser()
	config.read(str('../classiferSettings.ini'))

	feedName = str(config.get('feedInformation','file'))
	
	trainingDataFileName = '../data/training_data/partialClassifiedEntries.txt'
	categoryFileName = '../data/categories.txt'
	databaseName = str(config.get('training','database'))


	
	# Read the training_data
	trainingData = readTrainingData(trainingDataFileName)

	# Read the categories 
	categories = readCategories(categoryFileName)

	# Create a dictionary mapping article ids to entries
	idsToEntries = createIdsToEntries(feedName)



	#c1 = fisherclassifier(getwords)
	#c1.setdb(databaseName)

	# Train the classifier using description (the content in the blog)
	#for key in trainingData:
	#	descript = idsToEntries[key].description
	#	#print(descript)
	#	c1.train(descript,trainingData[key])
	