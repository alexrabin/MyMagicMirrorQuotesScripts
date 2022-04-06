import sys
import json
from word2number import w2n
import quotes_controller as q

def main():
    quoteController = q.QuotesController()
    option = getOption()
    done = False
    while (done != True):
        if option == 1:
            quote = input("What quote would you like to add?\n");
            script_descriptor = open("add_quote.py")
            add_quote = script_descriptor.read()
            sys.argv = ["add_quote.py", quote]
            exec(add_quote)
            script_descriptor.close()
            option = getOption()
        elif option == 2:
            print("You picked Option 2")
            quote = input("What quote would you like to remove? Enter a number or a quote. \n");
            script_descriptor = open("remove_quote.py")
            remove_quote = script_descriptor.read()
            sys.argv = ["remove_quote.py", quote]
            exec(remove_quote)
            script_descriptor.close()
            option = getOption()
        elif option == 3:
            quotes = quoteController.getQuotes()
            for i in range(len(quotes)):
                print(f"{i + 1}.)", quotes[i])

            option = getOption()
        elif option == 4:
            print("Bye Bye!")
            done = True
        else:
            option = getOption()

def getOption():
    showOptions()
    option = input("Enter the number you would like to perform:\n")
    if (option.lower() == "exit"):
        return 4

    while (option.isnumeric() == False):
        try:
            option = w2n.word_to_num(option)
            return option
        except:
            option =  input("The input you entered is not a number, please enter a number:\n")
            if (option.lower() == "exit"):
                return 4
    return int(option)

def showOptions():
    print("\nOptions:")
    print("1. Add Quote")
    print("2. Remove Quote")
    print("3. Show All Quotes")
    print("4. Exit\n")



main()