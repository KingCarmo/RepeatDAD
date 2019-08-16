#!/usr/bin/env python
import sys

myList = []
n = 20	# Number of top N records

for line in sys.stdin:

	line = line.strip()
	data = line.split(",")


	try:
		viewers = float(data[7])
	except ValueError:
		continue
	
	myList.append( (viewers, line) )
	myList.sort(reverse=True)
	
	if len(myList) > n:
		myList = myList[:n]
		
# Print top N records
for (k,v) in myList:
	print(v)
