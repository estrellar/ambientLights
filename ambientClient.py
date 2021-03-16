from PIL import ImageGrab
from tkinter import *
import serial.tools.list_ports
import tkinter as ttk
import serial
import time
from threading import Thread


keepSending = True;
cerealDevice = None;
def pourCereal(bowl):
    bowl = bowl.split()[0]
    global keepSending, cerealDevice
    cerealDevice = serial.Serial(bowl)

    while keepSending:
        image = ImageGrab.grab()
        pixels = image.load();
        colors = list()
        x1 = list()
        x2 = list()
        y1 = list()
        y2 = list()

        for x in range(0, 2560, 73):
            x1.append(image.getpixel((x, 20)))

        for x in range(0, 2560, 73):
            x2.append(image.getpixel((x, 1420)))
        for y in range(0, 1440, 68):
            y1.append(image.getpixel((20, y)))
        for y in range(0, 1440, 68):
            y2.append(image.getpixel((2540, y)))

        x1.pop()
        print(x1)
        x1 = [item for subl in x1 for item in subl]
        x1.append(0xA);

        x2.pop()
        x2 = [item for subl in x2 for item in subl]
        x2.append(0xA)

        y1.pop()
        y1 = [item for subl in y1 for item in subl]
        y1.append(0xA)

        y2.pop()
        y2 = [item for subl in y2 for item in subl]
        y2.append(0xA)

        cerealDevice.write(bytearray(x1))
        cerealDevice.write(bytearray(y1))
        cerealDevice.write(bytearray(x2))
        cerealDevice.write(bytearray(y2))


def test():
    image = ImageGrab.grab()
    px = image.load()


    for x in range(0, 2560, 73):
        px[x, 20] = (0, 0, 0)

    for x in range(0, 2560, 73):
        px[x, 1420] = (0, 0, 0)
    for y in range(0, 1440, 68):
        px[20, y] = (0, 0, 0)
    for y in range(0, 1440, 68):
        px[2540, y] = (0, 0, 0)

    image.save('test.png')


def stopPouring():
    global keepSending
    keepSending = False



def getCerealBoxes():
    return list(serial.tools.list_ports.comports())

root = ttk.Tk()
root.title('AmbientLites Client');
mainframe = Frame(root)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)
mainframe.pack(pady=100, padx=100)
tkvar = StringVar(root)
cereals = getCerealBoxes()
tkvar.set(cereals[0])

popMenu = OptionMenu(mainframe, tkvar, *cereals)
Label(mainframe, text="Choose Cereal Port").grid(row=1, column=1)
popMenu.grid(row=2, column=1)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

#buttons
B = ttk.Button(root, text='Start Pouring Cereal', command= lambda: pourCereal(tkvar.get()))
B.pack()
Abort = ttk.Button(root, text='test', command=test)
Abort.pack()
Abort = ttk.Button(root, text='Stop Pouring Cereal', command=stopPouring)
Abort.pack()


# link function to change dropdown
tkvar.trace('w', change_dropdown)

root.mainloop()
