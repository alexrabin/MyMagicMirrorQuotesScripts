import json

class QuotesController:

    def __init__(self):
        quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "r");
        self._quotes = json.load(quotesFile)
        quotesFile.close()

    def updateQuotesFile(self, quotesList):
        quotesFile = open("/home/pi/MagicMirror/modules/MMM-CloneWarsQuotes/MMM-MotivationQuotes.json", "w")
        json.dump(quotesList, quotesFile, indent=2)
        quotesFile.close()

    def addQuote(self,newQuote):
        if newQuote in self._quotes:
            return False
        self._quotes.append(newQuote)

        self.updateQuotesFile(self._quotes)
        return True

    def editQuote(self, index, newQuote):
        if (int(index) > len(self._quotes)):
            return False

        self._quotes[index] = newQuote;
        self.updateQuotesFile(self._quotes)
        return True

    def removeQuote(self, quoteToRemove):
        if (quoteToRemove.isnumeric() == True):
            return False

        if quoteToRemove not in self._quotes:
            return False

        self._quotes.remove(quoteToRemove)
        self.updateQuotesFile(self._quotes)
        return True

    def removeQuoteWithIndex(self,index):
        if (index.isnumeric() == False):
            return False

        if (int(index) > len(self._quotes) - 1):
            return False

        quote = self._quotes[int(index)]
        return removeQuote(quote)

    def getQuotes(self):
        return self._quotes