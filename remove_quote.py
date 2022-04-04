
import sys
import json

def main():

    if (len(sys.argv) < 2):
        print("Must have a quote to remove as a parameter")
        return

    if (len(sys.argv) > 2):
        print("This program only allows one quote at a time")
        return

    quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "r");
    jsonObject = json.load(quotesFile)
    quotesFile.close()

    quote = sys.argv[1]
    if (quote.isnumeric() == True):
        if (int(quote) >= len(jsonObject)):
            print("I'm sorry that quote does not exist")
            return
        quote = jsonObject[int(quote) - 1]


    if quote not in jsonObject:
        print("\""+quote+"\"", "does not exist")
        return

    jsonObject.remove(quote)

    quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "w")

    json.dump(jsonObject, quotesFile, indent=2)

    quotesFile.close()

    print("Removed Quote:","\""+ quote+"\"")

main()