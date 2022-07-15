import serial
import serial.tools.list_ports
import tkinter as tk
from tkinter import ttk

class Model(serial.Serial):
    def __init__(self):
        super().__init__()

        for device in serial.tools.list_ports.comports():
            if device.pid == 0x7523 and device.vid == 0x1a86:
                ch340 = device.name
                print("Ch340 found")

        self.port = ch340
        self.baudrate = 115200
        self.open

class View(ttk.Frame):
    def __init__(self, container):
        super().__init__(container)

    
class Controller():
    def __init__(self, model, view):
        self.model = model
        self.view = view

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("MVC Demo")

        model = Model()

        view = View(self)

        controller = Controller(model, view)

if __name__ == "__main__":
    app = App()
    app.mainloop()