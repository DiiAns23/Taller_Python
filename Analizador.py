from tkinter import Tk
from tkinter.filedialog import askopenfilename
from Carro import Carro as NewCarro

class Analizador():

    def __init__(self):
        self.texto = ""
        self.data = [] 

    def getData(self):
        return self.data

    def Leer(self, ext):
        x = ""
        Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
        try:
            filename = askopenfilename(title ='Selecciona un archivo',
                                                filetypes=[('Archivos', f'*.{ext}'), 
                                                            ('All Files', '*')])
            with open(filename, encoding="utf-8") as infile:
                x = infile.read().strip()
        except:
            print("Error, no se ha seleccionado ningun archivo")
            return

        y = ''
        for letra in x:
            if (letra != " " and letra != "\n" and letra != "\t"):
                    y += letra
        self.texto = y
            
    def Analizar(self):
        texto = self.texto.split(';')
        for x in texto:
            carro = x.split(',')
            nuevoCarro = NewCarro(carro[0], carro[1],carro[2],carro[3],carro[4])
            self.data.append(nuevoCarro)
    
