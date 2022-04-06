#!/usr/bin/python

import sys
import json
import quotes_controller as q

def main():
    quotesController = q.QuotesController()

    if (len(sys.argv) < 2):
        print("Must have a quote as a parameter")
        return
    if (len(sys.argv) > 2):
        print("This program only allows one quote at a time")
        return

    newQuote = sys.argv[1]
    if quotesController.addQuote(newQuote):
        print("Added Quote:","\""+newQuote+"\"")
        return
    else:
        print("\""+newQuote+"\"", "already exists")
        return	

main()