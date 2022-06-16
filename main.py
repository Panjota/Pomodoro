from tkinter import *
from tkinter import messagebox
import time

cont = 0

def intervalo_curto():
  nome.config(text="Intervalo Curto")
  minute = 1
  sec = 60
  while sec >= 0:
    minuto.config(text=f"0{minute}")
    segundo.config(text=sec)
    if sec < 10: 
      segundo.config(text=f"0{sec}")
    janela.update()
    time.sleep(0.1)
    sec -= 1
    print(f"{minute}{sec}")
    if minute > 0 and sec == 0:
      minute -= 1
      sec = 60
    if minute == 0 and sec == 0:
      messagebox.showinfo("Pomodoro", "Fim do intervalo curto")
      #iniciar.config(text ="Foco", width=6, command=iniciar)

def iniciar():
  nome.config(text="Foco")
  global cont
  cont += 1 
  contagem_pomodoros.set(f"Pomodoros: {cont}")
  minute = 0
  sec = 15
  while sec >= 0:
    minuto.config(text=minute)
    segundo.config(text=sec)
    janela.update()
    if minute < 10:
      minuto.config(text=f"0{minute}")
    if sec < 10: 
      segundo.config(text=f"0{sec}")
    janela.update()
    time.sleep(0.1)
    sec -= 1
    print(sec)
    if minute > 0 and sec == 0:
      minute -= 1
      sec = 60
    if minute == 0 and sec == 0:
      messagebox.showinfo("Pomodoro", "Hora do intervalo curto")
      iniciar.config(text ="Intervalo", width=8, command=intervalo_curto)
      


def resetar():
  janela.destroy()

janela = Tk()
janela.title("Pomodoro")
janela.geometry("300x250+550+200")
janela.resizable(False,False)

contagem_pomodoros = StringVar()
contagem_pomodoros.set(f"Pomodoros: 0")

nome = Label(janela, text="", font=("Times", 20))
contagem = Label(janela, textvariable=contagem_pomodoros, font=("Times",15))
minuto = Label(janela, text="25", font=("Times",72))
separador = Label(janela,text=":", font=("Times",72))
segundo = Label(janela, text="00", font=("Times", 72))
iniciar = Button(janela, width=6, text="Iniciar", font=("Comic Sans MS",15), command=iniciar)
resetar = Button(janela, width=6, text="Resetar", font=("Comic Sans MS",15), command=resetar)

nome.pack()
contagem.place(x=90, y=200)
minuto.place(x=35, y=30)
separador.place(x=130, y=30)
segundo.place(x=160, y=30)
iniciar.place(x=50, y=150)
resetar.place(x=170, y=150)

janela.mainloop()
