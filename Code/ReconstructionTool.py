from tkinter import *
from RubiksCube import Cube

"""
Copyright MartinK-99 2021
"""

singleMoves = ["R","R'","L","L'","U","U'","D","D'","F","F'","B","B'",
               "Rw","Rw'","Lw","Lw'","Uw","Uw'","Dw","Dw'","Fw","Fw'","Bw","Bw'",
               "r","r'","l","l'","u","u'","d","d'","f","f'","b","b'"]

doubleMoves = ["R2","L2","U2","D2","F2","B2",
               "Rw2","Lw2","Uw2","Dw2","Fw2","Bw2",
               "r2","l2","u2","d2","f2","b2",

               "R2'", "L2'", "U2'", "D2'", "F2'", "B2'",
               "Rw2'", "Lw2'", "Uw2'", "Dw2'", "Fw2'", "Bw2'",
               "r2'", "l2'", "u2'", "d2'", "f2'", "b2'"]

singleSliceMove = ["M","M'","E","E'","S","S'"]

doubleSliceMove = ["M2","E2","S2",
                   "M2'","E2'","S2'"]

rotations = ["x","x'","x2","x2'",
             "y","y'","y2","y2'",
             "z","z'","z2","z2'"]

def getData(inputthatisnotused=None):
    # Reset stringForClipboard
    stringForClipboard.set("")
    # Eingabe
    reconstructionString = reconstruction.get("1.0",END)
    # Reconstruction für die Weiterverarbeitung
    reconstructionEdit = reconstructionString.replace("(","")
    reconstructionEdit = reconstructionEdit.replace(")","")
    # Liste aller Rotationen und sonstigen Elementen
    recElem = reconstructionEdit.split()

    cube = Cube()
    if verifyRecon3.get() and scramble.get("1.0",END) != "":
        cube.algorithm(scramble.get("1.0",END))

    # Zähler
    moveCounter = 0

    # Für alle Elemente aus Liste...
    for i in recElem:
        if i in rotations:
            # Rotation auf Würfel anwenden
            if verifyRecon3.get(): cube.rotation(i)
        elif i in singleMoves or doubleMoves or singleSliceMove or doubleSliceMove:
            # Move auf Würfel anwenden
            if verifyRecon3.get(): cube.move(i)

            # Zählt Moves je nach Einstellungen, also
            # HTM oder QTM, slice als 2 Rotationen oder nicht
            if i in singleMoves:
                moveCounter += 1
            elif i in doubleMoves:
                if metric.get() in ["QTM","QSTM"]:
                    moveCounter +=2
                else:
                    moveCounter +=1
            elif i in singleSliceMove:
                if metric.get() in ["HTM","QTM"]:
                    moveCounter +=2
                else:
                    moveCounter +=1
            elif i in doubleSliceMove:
                if metric.get() in ["HTM","QSTM"]:
                    moveCounter += 2
                elif metric.get() == "QTM":
                    moveCounter += 4
                else:
                    moveCounter += 1

    # Exception, falls ungültige Time eingegeben wird
    try:
        enteredTime = abs(round(float(time.get("1.0", END)), 3))
        dataText = str(moveCounter) + " Moves (" + str(metric.get()) + ")\n" + "TPS: " +str(round(moveCounter/enteredTime,2))
        dataOutput.set(dataText)

        stringForClipboard.set(
            str(enteredTime) + " Single " + scramble.get("1.0",END) + "\nReconstruction:\n"
            + reconstructionString + "\n"
            + dataText
        )
    except ValueError:
        dataText = str(moveCounter) + " Moves (" + str(metric.get()) + ")\n" + "TPS: N/A"
        dataOutput.set(dataText)
        stringForClipboard.set(
            scramble.get("1.0", END) + "\nReconstruction:\n"
            + reconstructionString + "\n"
            + str(moveCounter) + " Moves (" + metric.get() + ")"
        )

    if cube.isSolved():
        checkRecon.set("")
    elif not(cube.isSolved()) and verifyRecon3.get():
        checkRecon.set("Your reconstruction may not solve the cube")

def copyToClipboard():
    root.clipboard_clear()
    root.clipboard_append(stringForClipboard.get())

def loadFromSave():
    try:
        savefile = open("save.txt","r")
        metric.set(metrics[int(savefile.readline())])
        verifyRecon3.set(bool(int(savefile.readline())))
        savefile.close()
    except FileNotFoundError:
        writeSave()


def writeSave():
    savefile = open("save.txt", "w")
    content = [str(int(metrics.index(metric.get())))+"\n",str(int(verifyRecon3.get()))]
    savefile.writelines(content)
    savefile.close()

def verifyOff():
    checkRecon.set("")

def focusScramble(event):
    scramble.focus()
    return 'break'

def focusReconstruction(event):
    reconstruction.focus()
    return 'break'

def focusTime(event):
    time.focus()
    return 'break'

def getDataEnter(event):
    getData()
    return 'break'

def openPopup(e):
    try:
        def copy(e):
            e.widget.event_generate('<Control-c>')

        def paste(e):
            e.widget.event_generate('<Control-v>')

        e.widget.focus()
        popupmenu = Menu(root, tearoff=False,takefocus=0)
        popupmenu.add_command(label="Copy", command=lambda e=e:copy(e))
        popupmenu.add_command(label="Paste", command=lambda e=e:paste(e))
        popupmenu.tk_popup(e.x_root, e.y_root)
    except TclError:
        print("Something went wrong rightclick popupmenu")
        pass
    return "break"



root = Tk()
root.title("Reconstruction Tool")
root.configure(background="black")
#root.iconbitmap('Icon.ico')

# Scramble Überschrift
Label(root,text="Scramble",bg = "black",fg="white",font="none 12 bold").\
    grid(row=0,columnspan=2)

# Scramble Textfeld
scramble = Text(root,width=60,height=1,bg="white", padx=10, font = "none 10",wrap=NONE)
scramble.grid(row=1,columnspan=2)
scramble.bind('<Return>',focusReconstruction)
scramble.bind('<Tab>',focusReconstruction)
scramble.bind('<Shift-Tab>',lambda event:'break')

# Reconstruction Überschrift
Label(root,text="Reconstruction",bg="black",fg="white",font="none 12 bold").\
    grid(row=2,columnspan=2)

# Reconstruction Textfeld
reconstruction = Text(root, width=50,height=20, bg="white", pady = 10, padx = 10,font = "none 13")
reconstruction.grid(row=3,columnspan=2)
reconstruction.bind('<Shift-Return>',focusTime)
reconstruction.bind('<Control-Return>',focusTime)
reconstruction.bind('<Tab>',focusTime)
reconstruction.bind('<Shift-Tab>',focusScramble)

checkRecon = StringVar()
checkRecon.set("")

Label(root,textvariable=checkRecon,bg="black",fg="red",font="none 10 bold").\
    grid(row=4,column=0,columnspan=2)

# Time Überschrift
Label(root,text="Time in Seconds",bg="black",fg="white",font="none 12 bold").\
    grid(row=5,column=0)

# Time Textfeld
time = Text(root,width=10,height=1,bg="white",font="none 12")
time.grid(row=6,column=0)
time.bind('<Return>',getDataEnter)
time.bind('<Shift-Tab>',focusReconstruction)
time.bind('<Tab>',lambda event:'break')


Label(root,text="Format: 12.123",bg="black",fg="white",font="none 10").\
    grid(row=7,column=0,sticky=N)

# Stats Output String
dataOutput = StringVar()
dataOutput.set("Moves\nTPS")

# Stats Überschrift
Label(root,text="Stats",bg="black",fg="white",font="none 12 bold").\
    grid(row=5,column=1)

# Stats Label
Label(root,textvariable=dataOutput,bg="black",fg="white",font="none 12").\
    grid(row=6,column=1,rowspan=2)

# Enter Button
Button(root,text="Enter",width=6,command=getData).\
    grid(row=8,columnspan=2)

# Copy To Clipyboard Button
Button(root,text="Copy To Clipboard",width=15,command=copyToClipboard,\
       bg="black",fg="white",bd=0).\
    grid(row=9,column=1,sticky=E)

# String der zum Clipboard hinzugefügt wird
stringForClipboard = StringVar()

root.bind("<Button-3>",openPopup)

# Standard Variablen für
# die Settings
verifyRecon3 = BooleanVar()
verifyRecon3.set(True)
metrics = ["HTM","QTM","STM","QSTM"]
metric = StringVar()
metric.set(metrics[2])

loadFromSave()

# Settings Window
def settingsWindow():
    settings = Toplevel(root)
    settings.title("Settings")
    #settings.iconbitmap('Icon.ico')

    # Settings Überschrift
    Label(settings,text="Settings",font="none 12 bold",fg="black").\
        grid(row=0,columnspan=2,sticky=W)

    # Metrik Label
    Label(settings,text="     Metric",font="none 10",fg="black").\
        grid(row=2,column=0,sticky=W)
    # Metrik auswählen
    metricDropDown = OptionMenu(settings,metric,*metrics,command=lambda m:[writeSave(),getData()])
    metricDropDown.grid(row=2,column=1,sticky=W)


    # Checkbutton für Einstellungen
    # Verifiziert Reconstruction bei 3x3 Würfel
    Checkbutton(settings, text="Verify 3x3 Reconstruction", font="none 10", fg = "black",
                variable=verifyRecon3,onvalue=True,offvalue=False,command=lambda:[writeSave(),verifyOff()]).\
        grid(row=1,columnspan=2,sticky=W)

    # About
    Label(settings, text="About", font="none 12 bold").\
        grid(row=3,columnspan=2,sticky=W)

    # Text für About
    Label(settings, text="Creator: Martin Köhler\n© 2020 Martin Köhler", font="none 12").\
        grid(row=4,columnspan=2)

    # Position basierend auf Position von Hauptfenster
    x = root.winfo_x()
    y = root.winfo_y()

    w = 250
    h = 200
    dx = 50
    dy = 300
    settings.geometry("%dx%d+%d+%d" % (w, h, x + dx, y + dy))

    # Nicht Resizable
    settings.resizable(0,0)
    # Nur ein einziges Settingswindow
    settings.transient(root)
    settings.grab_set()
    root.wait_window(settings)

# Settings Button
Button(root,text="Settings",font="none 10",command=settingsWindow,bg="black",fg="white",bd=0).\
    grid(row=9,column=0,sticky=W)

scramble.focus()

# Nicht Resizable
root.resizable(0,0)
#root.call("tk","scaling",2.0)
root.mainloop()