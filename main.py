from tkinter import *
import time

foco = 25
intervalo_curto = 5
intervalo_longo = 15
contagem_pomodoros = 0


def iniciar():
  pass
def pausar():
  pass
def resetar():
  pass

janela = Tk()
janela.title("Pomodoro")
janela.geometry("300x250+550+200")
janela.resizable(False,False)

tempo = Label(janela, text="00:00", font=("Times",72))
tempo.place(x=35, y=30)
contagem = Label(janela, text=f"Pomodoros:{contagem_pomodoros}", font=("Times",15))
contagem.pack()
iniciar = Button(janela, width=6, text="Iniciar", font=("Comic Sans MS",15), command=iniciar)
iniciar.place(x=10, y=150)
pausar = Button(janela, width=6, text="Pausar", font=("Comic Sans MS",15))
pausar.place(x=110, y=150)
resetar = Button(janela, width=6, text="Resetar", font=("Comic Sans MS",15))
resetar.place(x=210, y=150)


janela.mainloop()
