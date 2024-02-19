import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox #messagebox = aknast välja minek
import tkinter.font as font #kirjasuuruse/fondi muutmiseks akendes


class View(Tk):
    def __init__(self, controller):
        super().__init__() #Tk jaoks
        self.controller = controller #kontrollerite asju saab views kasutada
        self.__width = 550
        self.__height = 500
        self.default_font = font.Font(family='Verdana', size=14) #Widgets kirjastiil

        #akna omadused
        self.title('Risttahukas') #akna tiitel
        self.center_window(self.__width, self.__height)

        #loome 2 frame-i
        self.top_frame = self.create_top_frame()
        self.bottom_frame = self.create_bottom_frame()

        #Widgets loomine
        (self.entry_length, self.entry_width, self.entry_height, self.btn_arvuta, self.text_box) = self.create_frame_widgets()


    def main(self):
        self.mainloop()

    def center_window(self, width, height):
        x = (self.winfo_screenwidth() // 2) - (width // 2)
        y = (self.winfo_screenheight() //2) - (height //2)
        self.geometry(f'{width}x{height}+{x}+{y}')

    def create_top_frame(self):
        frame = Frame(self, height=15)
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_bottom_frame(self):
        frame = Frame(self, bg='yellow')
        frame.pack(expand=True, fill=BOTH)
        return frame

    def create_frame_widgets(self): #widgetsite funkstioon

        #Label 'Sisesta Pikkus, Laius, Kõrgus'
        lbl_length = Label(self.top_frame, text='Pikkus', font=self.default_font)
        lbl_length.grid(row=1, column=0, padx=5, pady=5)

        lbl_width = Label(self.top_frame, text='Laius', font=self.default_font)
        lbl_width.grid(row=2, column=0, padx=5, pady=5)

        lbl_height = Label(self.top_frame, text='Kõrgus', font=self.default_font)
        lbl_height.grid(row=3, column=0, padx=5, pady=5)

        #Sisestuskastid Pikkusele, Laiusele ja kõrgusele
        entry_length = Entry(self.top_frame, font=self.default_font)
        entry_length.grid(row=1, column=1, padx=5, pady=5)
        entry_length.focus()

        entry_width = Entry(self.top_frame, font=self.default_font)
        entry_width.grid(row=2, column=1, padx=5, pady=5)
        entry_width.focus()

        entry_height = Entry(self.top_frame, font=self.default_font)
        entry_height.grid(row=3, column=1, padx=5, pady=5)
        entry_height.focus()

        #Nupp 'Arvuta'
        btn_arvuta = Button(self.top_frame, text='Arvuta', font=self.default_font, command=self.calculate)
        btn_arvuta.grid(row=3, column=3, padx=5, pady=5, sticky='ew')

        #Tekstikast
        text_box = Text(self.bottom_frame, font=self.default_font)
        text_box.pack(expand=True, fill=BOTH, padx=5, pady=5) #tekstbox kogu alale täita ära

        return entry_length, entry_width, entry_height, btn_arvuta, text_box #tagastab info

    def get_values(self):
        try:
            length = float(self.entry_length.get())
            width = float(self.entry_width.get())
            height = float(self.entry_height.get())

            if length < 0 or width < 0 or height < 0:
                messagebox.showerror("Viga", "Palun sisesta positiivsed väärtused")
                return None

            return length, width, height

        except ValueError:
            messagebox.showerror("Viga", "Palun sisestage arvulised väärtused")
            return None

    def set_result(self, result_text, input_values):
        self.text_box.delete(1.0, tk.END)  #Eelmised read kustutada

        input_text = f"Pikkus = {input_values[0]}, Laius = {input_values[1]}, Kõrgus = {input_values[2]}\n\n"
        full_result_text = input_text + result_text

        self.text_box.insert(tk.END, full_result_text)


    def calculate(self):
        values = self.get_values()
        if values:
            self.controller.calculate(values)
