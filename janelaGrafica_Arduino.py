import serial
import time
from Tkinter import *

conexao = serial.Serial('/dev/ttyACM0',9600)


def ligar_led():
     conexao.write('1'.encode())


def desligar_led():
     conexao.write('2'.encode())


janela = Tk()
janela.title("BLINK LED (Liga ou Desliga)")
janela.geometry("400x130")
botaoLigar = Button(janela,text="Ligar LED",command=ligar_led)
botaoDesliga = Button(janela,text="Desligar LED",command=desligar_led)
botaoLigar.pack()
botaoDesliga.pack()

janela.mainloop()
