
import sys
import json
import quotes_controller as q

def main():
    quotesController = q.QuotesController()

    if (len(sys.argv) < 2):
        print("Must have a quote to remove as a parameter")
        return

    if (len(sys.argv) > 2):
        print("This program only allows one quote at a time")
        return


    quotesList = quotesController.getQuotes()
    quote = sys.argv[1]
    if (quote.isnumeric() == True):
        if (int(quote) >= len(quotesList)):
            print("I'm sorry that quote does not exist")
            return
        quote = quotesList[int(quote) - 1]


    if quotesController.removeQuote(quote):
        print("Removed Quote:","\""+ quote+"\"")
        return
    else:
        print("\""+quote+"\"", "does not exist")
        return

main()