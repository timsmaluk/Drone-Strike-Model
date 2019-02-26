import json
import requests
import pandas as pd
import numpy as np
import csv

url = 'https://api.dronestre.am/data'
r = requests.get(url)
data = r.json()

number = [] 	# number of drone strikes
country =[]	 	# country drone strike occurred
date = []   	# date of strike
deaths = []	 	# number of deaths
location = [] 	# location of the strike 
lat = []		# latitude
lon = []		# longitude 
children = []	# number of children killed
civilians = [] 	# number of civilians killed
towns = []		# towns where strikes occurred

for strike in data['strike']:
	number.append(strike['number'])
	country.append(strike['country'])
	date.append(strike['date'])
	deaths.append(strike['deaths'])
	location.append(strike['location'])
	lat.append(strike['lat'])
	lon.append(strike['lon'])
	children.append(strike['children'])
	civilians.append(strike['civilians'])
	towns.append(strike['town'])

temp = [y for x in map(None,lat,lon) for y in x] #creates a concatenated list of lats and longs# 
temp = filter(None, temp)
temp = map(float, temp) #change a list of strings into a list of floats
fixed = [(temp[i],temp[i+1]) for i in range(0,len(temp),2)] #tuples of every two cells of temp list
triple = []

for i in range(0, len(towns)-1):
	if i < len(fixed):
		triple.append([fixed[i][0] or '', fixed[i][1] or '', towns[i]] or '')
	else:
		triple.append(['','',towns[i]])
#print triple

quadruple = []

for i in range(0, len(country)-1):
	if i < len(triple):
		quadruple.append([triple[i][0] or '', triple[i][1] or '', towns[i] or '', country[i]] or '')
	else:
		quadruple.append(['', '', country[i]])

print quadruple

outfile = open('./drone_strike_coordinates.csv', 'wb')
writer = csv.writer(outfile)
writer.writerow(['latitude', 'longitude', 'town', 'country'])
writer.writerows(quadruple)





