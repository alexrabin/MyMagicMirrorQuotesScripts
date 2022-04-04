#!/usr/bin/python

import sys
import json

def main():
	if (len(sys.argv) < 2):
		print("Must have a quote as a parameter")
		return
	if (len(sys.argv) > 2):
		print("This program only allows one quote at a time")
		return

	quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "r");
	jsonObject = json.load(quotesFile)
	quotesFile.close()

	newQuote = sys.argv[1]
	if newQuote in jsonObject:
		print("\""+newQuote+"\"", "already exists")
		return

	jsonObject.append(newQuote)

	quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "w")

	json.dump(jsonObject, quotesFile, indent=2)

	quotesFile.close()

	print("Added Quote:","\""+newQuote+"\"")

main()
