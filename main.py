from tkinter import *

janela = Tk()
janela.title("Pomodoro")

janela.geometry("300x300+550+200")
janela.resizable(False,False)
janela.iconbitmap("icon/icon_apple.ico")

iniciar = Button(janela, text="Iniciar")
iniciar.pack()
pausar = Button(janela, text="Pausar")
pausar.pack()
resetar = Button(janela, text="Resetar")
resetar.pack()


janela.mainloop()
