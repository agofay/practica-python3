/*
TablaAlambres=[7,44.2; 8,
preguntar voltaje_entrada, voltaje_salida, amperios_salida

vatios = voltaje_salida * amperios_salida

cm2 = 1.3 * Raiz(vatios)

amperio_entrada = vatios / voltaje_entrada

VueltasVoltios = 40 / cm2

VueltasPrimario = voltaje_entrada * VueltasVoltios
AlambrePrimario = 

vueltasSecundario = voltaje_salida * VueltasVoltios
*/

#!/usr/bin/python
from tkinter import *
import math

class App:
    def __init__(self,master):
        root.title('Calculo de vueltas para tranformadores')
        Label(master,text='Ingresar valores').grid(row=0,columnspan=2,sticky=W+E)
        Label(master,text='Voltaje de Entrada: ').grid(row=1,sticky=W)
        VoltajeEntrada=Entry(master).grid(row=1,column=1)
        Label(master,text='Voltaje de Salida: ').grid(row=2,sticky=W)
        VoltajeSalida=Entry(master).grid(row=2,column=1)
        Label(master,text='Amperios de salida: ').grid(row=3,sticky=W)
        AmperiosSalida=Entry(master).grid(row=3,column=1)
        Label(master,text='').grid(row=4)
        Button(master,text='Calcular',command=self.Calcular).grid(row=5,columnspan=2)

        Vatios = float(VoltajeSalida.get()) * float(AmperiosSalida.get())
        cm2 = 1.3 #* sqrt(Vatios)
        AmperiosEntrada = Vatios / float(VoltajeEntrada)
        VueltasVoltios = 40 / cm2
        VueltasPrimario = float(VoltajeEntrada) * VueltasVoltios
        AlambrePrimario =
        VueltasSecundario = float(VoltajeSalida) * VueltasVoltios
        TablaAlambres={7:44.2}

    def Calcular():
      print(master.VoltajeEntrada*VoltajeSalida)

root = Tk()
app = App(root)
root.mainloop()

