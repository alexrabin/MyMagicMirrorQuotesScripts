from guizero import App, ListBox, TextBox, Box, PushButton, yesno, question, info, error
import json
import quotes_controller as q


quotesController = q.QuotesController()

def getQuotes():
    rawQuotesList = quotesController.getQuotes()
    formatedQuotes = []
    for i in range(len(rawQuotesList)):
        q = rawQuotesList[i]
        formatedQuotes.append(f"{i + 1}.) "+ q)
    return formatedQuotes

app = App(title="Quotes")


currentQuoteBox = Box(app, width="fill", height=120, visible=False)
currentQuote = None
listBox = None
currentQuoteIndex = 0
def addQuote():
    response = question("Add Quote", None);
    if (response is not None):
        if (quotesController.addQuote(response)):
            listBox.clear()
            for q in getQuotes():
                listBox.append(q)
            info("Success", "Succesfully added quote\n\n" + response)

        else:
            error("Error", "Failed to save quote")

addButton = PushButton(app, text="New Quote", command=addQuote)
addButton.bg = "green"
addButton.text_color = "white"
def editQuoteAction():
    response = question("Edit Quote", None, initial_value=currentQuote.value[:len(currentQuote.value)-1])
    if (response is not None):
        if (quotesController.editQuote(currentQuoteIndex, response)):
            listBox.clear()
            for q in getQuotes():
                listBox.append(q)
            currentQuote.enable()
            currentQuote.value = response
            currentQuote.disable()
            info("Success", "Succesfully edited quote\n\n" + response)

        else:
            error("Error", "Failed to save quote")


def deleteQuoteAction():
    v = currentQuote.value[:len(currentQuote.value)-1]
    response = yesno("Delete?", "Are you sure you want to delete this quote?\n\n'" + v + "'")
    if (response == True):
        if (quotesController.removeQuote(v)):
            listBox.clear()
            for q in getQuotes():
                listBox.append(q)
            currentQuoteBox.hide()
            info("Success", "Succesfully removed quote\n\n" + v)



buttonGroup = Box(currentQuoteBox, layout="grid", height=50, width=120)
editButton = PushButton(buttonGroup, text="Edit", command=editQuoteAction, grid=[0,0])
deleteButton = PushButton(buttonGroup, text="Delete", command=deleteQuoteAction, grid=[1,0])
deleteButton.bg = "red"
deleteButton.text_color ="white"
currentQuote = TextBox(currentQuoteBox, width="fill", height=70, multiline=True)


def quoteSelected(option):
    currentQuote.enable()

    qComps = option.split(".) ")
    global currentQuoteIndex
    currentQuoteIndex = int(qComps[0]) - 1
    q = qComps[1]
    currentQuote.value = q
    if (currentQuoteBox.visible == False):
        currentQuoteBox.show()
    currentQuote.disable()

listBox = ListBox(app, items=getQuotes(), width="fill", command=quoteSelected, scrollbar=True)


app.display()