import tkinter as tk
from tkinter import messagebox

class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry('400x450')
        self.resizable(0,0)
        self.title('Calculadora')
        self.iconbitmap('cal.ico')
        self.expresion = ''
        self.entrada = None
        self.entrada_texto = tk.StringVar()
        self._creacion_componentes()

    def _creacion_componentes(self):
        entrada_frame = tk.Frame(self, width = 400, height = 50, bg = 'grey')
        entrada_frame.pack(side = tk.TOP)
        entrada = tk.Entry(entrada_frame, font=('arial', 18, 'bold'), textvariable = self.entrada_texto, width = 30, justify = tk.RIGHT)
        entrada.grid(row = 0, column = 0, ipady = 10)
        botones_frame = tk.Frame(self, width=400, height=450, bg='grey')
        botones_frame.pack()
        boton_limpiar = tk.Button(botones_frame, text='C', width=32, height=3, bd=0, bg='#eee', cursor='hand2', command=self._evento_limpiar)
        boton_limpiar.grid(row=0, column=0, columnspan=3, padx=1, pady=1)

    def _evento_limpiar(self):
        pass

if __name__ == '__main__':
    calculadora = Calculadora()
    calculadora.mainloop()