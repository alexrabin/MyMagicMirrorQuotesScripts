from guizero import App, ListBox
import json

def getRawQuotes():
    quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "r");
    jsonObject = json.load(quotesFile)
    quotesFile.close()
    return jsonObject

def quoteSelected(option):
    print(option)

app = App(title="Quotes")

rawQuotesList = getRawQuotes()
formatedQuotes = []
for i in range(len(rawQuotesList)):
    q = rawQuotesList[i]
    formatedQuotes.append(f"{i + 1}.) "+ q)

ListBox(app, items=formatedQuotes, width="fill", command=quoteSelected)

app.display()