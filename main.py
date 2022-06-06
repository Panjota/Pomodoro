from cProfile import label
from cgitb import text
from tkinter import *
#from comandos import *

janela = Tk()
janela.title("Pomodoro")

janela.geometry("300x300+550+200")
janela.resizable(False,False)

#timermin =str(25)
#timersec =str(20)

tempo = Label(janela, text="00:00", font=("Times",72))
tempo.pack()
iniciar = Button(janela, width=6, text="Iniciar", font=("Comic Sans MS",15))
iniciar.pack()
pausar = Button(janela, width=6, text="Pausar", font=("Comic Sans MS",15))
pausar.pack()
resetar = Button(janela, width=6, text="Resetar", font=("Comic Sans MS",15))
resetar.pack()


janela.mainloop()
