
import tkinter as tk
#cria uma instancia de uma janela
janela = tk.Tk()
janela.title(" Bem vindo ao Tkinter")
label = tk.Label( janela,text="Este é um label", font = ("Arial Bold",70))
label_2 = tk.Label( janela, text= "Este é outro label", font =("Arial Bold",red, 50))




label.grid(column=0, row=0)
label_2.grid(column=0, row=1)



janela.mainloop()
