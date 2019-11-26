from tkinter import *
from special_char import *

class Main(Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        
        #container para o titulo e a petição
        self.cont1 = Frame(master)
        self.cont1["pady"] = 20
        self.cont1.pack()
        
        #containers para cada equacao
        self.cont2 = Frame(master)
        self.cont2.pack()
        self.cont2.v = Frame(master)
        self.cont2.v.pack()
        
        self.cont3 = Frame(master)
        self.cont3.pack()
        self.cont3.v = Frame(master)
        self.cont3.v.pack()
        
        self.cont4 = Frame(master)
        self.cont4.pack()
        self.cont4.v = Frame(master)
        self.cont4.v.pack()
        
        self.cont5 = Frame(master)
        self.cont5.pack()
        self.cont5.v = Frame(master)
        self.cont5.v.pack()
        
        self.cont6 = Frame(master)
        self.cont6.pack()
        self.cont6.v = Frame(master)
        self.cont6.v.pack()
        
        self.cont7 = Frame(master)
        self.cont7.pack()
        self.cont7.v = Frame(master)
        self.cont7.v.pack()
        
        self.cont8 = Frame(master)
        self.cont8.pack()
        self.cont8.v = Frame(master)
        self.cont8.v.pack()
        
        self.cont9 = Frame(master)
        self.cont9.pack()
        self.cont9.v = Frame(master)
        self.cont9.v.pack()
        
        #container para o botao submeter
        self.contPU = Frame(master)
        self.contPU["pady"] = 30
        self.contPU.pack()
        
        #container para o botao sair
        self.contU = Frame(master)
        self.contU["pady"] = 15
        self.contU.pack()
        
        #definindo o titulo
        self.titulo = Label(self.cont1, text="Resolvedor de funções 2000")
        self.titulo["font"] = ("Arial", 18, "bold")
        self.titulo["pady"] = 20
        self.titulo.pack()
        
        #definindo a mensagem
        self.msg = Label(self.cont1, text="Escolha a equação a qual deseja resolver!")
        self.msg["font"] = ("Arial", 12, "italic")
        self.msg["pady"] = 10
        self.msg.pack()
        
        self.msgg = Label(self.cont1, text="Digite também, na ordem apresentada, os valores para cada variável.\n\n Deixe em branco o campo relativo ao valor que quer descobrir.")
        self.msgg["font"] = ("Arial", 10)
        self.msgg["pady"] = 10
        self.msgg.pack()
        
        #variavel de controle para escolher apenas um botão
        self.ver = IntVar()
        
        #botao 1 - pitágoras
        self.f1 = Radiobutton(self.cont2, variable=self.ver, value=1)
        self.f1.pack(side=LEFT)
        self.msg1 = Label(self.cont2, text=("a" + quadrado() + " + b" + quadrado() + " = c" + quadrado()))
        self.msg1["font"] = ("Arial", 10)
        self.msg1.pack()
        
        #caixas de entrada
        self.a = Entry(self.cont2.v)
        self.a["width"] = 5
        self.a["font"] = ("Arial", 10)
        self.a.pack(side=LEFT)
        self.b = Entry(self.cont2.v)
        self.b["width"] = 5
        self.b["font"] = ("Arial", 10)
        self.b.pack(side=LEFT)
        self.c = Entry(self.cont2.v)
        self.c["width"] = 5
        self.c["font"] = ("Arial", 10)
        self.c.pack(side=LEFT)
        
        #botao 2 - gravidade
        self.f2 = Radiobutton(self.cont3, variable=self.ver, value=2)
        self.f2.pack(side=LEFT)
        self.msg2 = Label(self.cont3, text=("F = (G " + ponto() + " m" + unzinho() + " " + ponto() + " m" + doizinho() + ") / d" + quadrado()))
        self.msg2["font"] = ("Arial", 10)
        self.msg2.pack()
        
        #caixas de entrada
        self.F = Entry(self.cont3.v)
        self.F["width"] = 5
        self.F["font"] = ("Arial", 10)
        self.F.pack(side=LEFT)
        self.g = Entry(self.cont3.v)
        self.g["width"] = 5
        self.g["font"] = ("Arial", 10)
        self.g.pack(side=LEFT)
        self.m1 = Entry(self.cont3.v)
        self.m1["width"] = 5
        self.m1["font"] = ("Arial", 10)
        self.m1.pack(side=LEFT)
        self.m2 = Entry(self.cont3.v)
        self.m2["width"] = 5
        self.m2["font"] = ("Arial", 10)
        self.m2.pack(side=LEFT)
        self.d = Entry(self.cont3.v)
        self.d["width"] = 5
        self.d["font"] = ("Arial", 10)
        self.d.pack(side=LEFT)
        
        #botao 3 - relatividade
        self.f3 = Radiobutton(self.cont4, variable=self.ver, value=3)
        self.f3.pack(side=LEFT)
        self.msg3 = Label(self.cont4, text=("E = m " + ponto() + " c" + quadrado()))
        self.msg3["font"] = ("Arial", 10)
        self.msg3.pack()
        
        #caixas de entrada
        self.e = Entry(self.cont4.v)
        self.e["width"] = 5
        self.e["font"] = ("Arial", 10)
        self.e.pack(side=LEFT)
        self.m = Entry(self.cont4.v)
        self.m["width"] = 5
        self.m["font"] = ("Arial", 10)
        self.m.pack(side=LEFT)
        self.co = Entry(self.cont4.v)
        self.co["width"] = 5
        self.co["font"] = ("Arial", 10)
        self.co.pack(side=LEFT)
        
        #botao 4 - caos
        self.f4 = Radiobutton(self.cont5, variable=self.ver, value=4)
        self.f4.pack(side=LEFT)
        self.msg4 = Label(self.cont5, text=("x" + doizinho() + " = k " + ponto() + " x" + unzinho() + " " + ponto() + " (1 - x" + unzinho() + ")"))
        self.msg4["font"] = ("Arial", 10)
        self.msg4.pack()
        
        #caixas de entrada
        self.x2 = Entry(self.cont5.v)
        self.x2["width"] = 5
        self.x2["font"] = ("Arial", 10)
        self.x2.pack(side=LEFT)
        self.k = Entry(self.cont5.v)
        self.k["width"] = 5
        self.k["font"] = ("Arial", 10)
        self.k.pack(side=LEFT)
        self.x1 = Entry(self.cont5.v)
        self.x1["width"] = 5
        self.x1["font"] = ("Arial", 10)
        self.x1.pack(side=LEFT)
        
        #botao 5 - clapeyron
        self.f5 = Radiobutton(self.cont6, variable=self.ver, value=5)
        self.f5.pack(side=LEFT)
        self.msg5 = Label(self.cont6, text=("p " + ponto() + " V = n " + ponto() + " R " + ponto() + " T"))
        self.msg5["font"] = ("Arial", 10)
        self.msg5.pack()
        
        #caixas de entrada
        self.pr = Entry(self.cont6.v)
        self.pr["width"] = 5
        self.pr["font"] = ("Arial", 10)
        self.pr.pack(side=LEFT)
        self.v = Entry(self.cont6.v)
        self.v["width"] = 5
        self.v["font"] = ("Arial", 10)
        self.v.pack(side=LEFT)
        self.n = Entry(self.cont6.v)
        self.n["width"] = 5
        self.n["font"] = ("Arial", 10)
        self.n.pack(side=LEFT)
        self.r = Entry(self.cont6.v)
        self.r["width"] = 5
        self.r["font"] = ("Arial", 10)
        self.r.pack(side=LEFT)
        self.t = Entry(self.cont6.v)
        self.t["width"] = 5
        self.t["font"] = ("Arial", 10)
        self.t.pack(side=LEFT)
        
        #botao 6 - torricelli
        self.f6 = Radiobutton(self.cont7, variable=self.ver, value=6)
        self.f6.pack(side=LEFT)
        self.msg6 = Label(self.cont7, text=("v" + quadrado() + " = v" + zerinho() + quadrado() + " + 2 " + ponto() + " a " + ponto() + " S"))
        self.msg6.pack()
        
        #caixas de entrada
        self.v = Entry(self.cont7.v)
        self.v["width"] = 5
        self.v["font"] = ("Arial", 10)
        self.v.pack(side=LEFT)
        self.v0 = Entry(self.cont7.v)
        self.v0["width"] = 5
        self.v0["font"] = ("Arial", 10)
        self.v0.pack(side=LEFT)
        self.ac = Entry(self.cont7.v)
        self.ac["width"] = 5
        self.ac["font"] = ("Arial", 10)
        self.ac.pack(side=LEFT)
        self.s = Entry(self.cont7.v)
        self.s["width"] = 5
        self.s["font"] = ("Arial", 10)
        self.s.pack(side=LEFT)
        
        #botao 7 - gauss
        self.f7 = Radiobutton(self.cont8, variable=self.ver, value=7)
        self.f7.pack(side=LEFT)
        self.msg7 = Label(self.cont8, text=("1/f = (1/p) + (1/p')"))
        self.msg7.pack()
        
        #caixas de entrada
        self.f = Entry(self.cont8.v)
        self.f["width"] = 5
        self.f["font"] = ("Arial", 10)
        self.f.pack(side=LEFT)
        self.p = Entry(self.cont8.v)
        self.p["width"] = 5
        self.p["font"] = ("Arial", 10)
        self.p.pack(side=LEFT)
        self.p2 = Entry(self.cont8.v)
        self.p2["width"] = 5
        self.p2["font"] = ("Arial", 10)
        self.p2.pack(side=LEFT)
        
        #botao 8 - força sobre partícula
        self.f8 = Radiobutton(self.cont9, variable=self.ver, value=8)
        self.f8.pack(side=LEFT)
        self.msg8 = Label(self.cont9, text=("F = B " + ponto() + " i " + ponto() + " l " + ponto() + " sen(" + theta() +")"))
        self.msg8.pack()
        
        self.fm = Entry(self.cont9.v)
        self.fm["width"] = 5
        self.fm["font"] = ("Arial", 10)
        self.fm.pack(side=LEFT)
        self.B = Entry(self.cont9.v)
        self.B["width"] = 5
        self.B["font"] = ("Arial", 10)
        self.B.pack(side=LEFT)
        self.i = Entry(self.cont9.v)
        self.i["width"] = 5
        self.i["font"] = ("Arial", 10)
        self.i.pack(side=LEFT)
        self.l = Entry(self.cont9.v)
        self.l["width"] = 5
        self.l["font"] = ("Arial", 10)
        self.l.pack(side=LEFT)
        self.o = Entry(self.cont9.v)
        self.o["width"] = 5
        self.o["font"] = ("Arial", 10)
        self.o.pack(side=LEFT)
        
        #botao penultimo - submeter
        self.sub = Button(self.contPU)
        self.sub["text"] = "Submeter"
        self.sub["font"] = ("Arial", 10)
        self.sub["width"] = 10
        self.sub.pack(side=BOTTOM)
        
        #botao ultimo - sair
        self.sair = Button(self.contU)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", 10)
        self.sair["width"] = 5
        self.sair["command"] = self.contU.quit
        self.sair.pack(side=BOTTOM)

myApp = Main()

myApp.master.title("Resolvedor de Funções")

myApp.mainloop()
