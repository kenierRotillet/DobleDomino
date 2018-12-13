import Jugador
import generaFichas
import tkinter as tk

class cGame(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        for i in range(0,55):
            self.hi_there = tk.Button(self)
            self.hi_there["text"] = "Hello World\n(click me)"
            self.hi_there["command"] = self.say_hi
            self.hi_there.pack(side="top")

        self.quit = tk.Button(self, text="QUIT", fg="red",
                              command=self.master.destroy)
        self.quit.pack(side="bottom")

    def say_hi(self):
        print("hi there, everyone!")

root = tk.Tk()
app = cGame(master=root)
app.mainloop()

listafichas=generaFichas.cGenera()

j1=Jugador.cJugador("jugador1",listafichas.listas[0:10])
j2=Jugador.cJugador("jugador2",listafichas.listas[10:20])
j3=Jugador.cJugador("jugador3",listafichas.listas[20:30])
j4=Jugador.cJugador("jugador4",listafichas.listas[30:40])

print(j1.fichas)
print(j2.fichas)
print(j3.fichas)
print(j4.fichas)


