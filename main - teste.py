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
        
        self.cont3 = Frame(master)
        self.cont3.pack()
        
        self.cont4 = Frame(master)
        self.cont4.pack()
        
        self.cont5 = Frame(master)
        self.cont5.pack()
        
        self.cont6 = Frame(master)
        self.cont6.pack()
        
        self.cont7 = Frame(master)
        self.cont7.pack()
        
        self.cont8 = Frame(master)
        self.cont8.pack()
        
        self.cont9 = Frame(master)
        self.cont9.pack()
        
        #container para o botao submeter
        self.contPU = Frame(master)
        self.contPU["pady"] = 30
        self.contPU.pack()
        
        #container para as caixas de entrada
        self.contE = Frame(master)
        self.contE["pady"] = 15
        self.contE.pack()
        
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
        
        self.ver = IntVar()
        
        #botao 1 - pitágoras
        self.f1 = Radiobutton(self.cont2, variable=self.ver, value=1)
        self.f1.pack(side=LEFT)
        self.msg1 = Label(self.cont2, text=("a" + quadrado() + " + b" + quadrado() + " = c" + quadrado()))
        self.msg1["font"] = ("Arial", 10)
        self.msg1.pack()
        
        #botao 2 - gravidade
        self.f2 = Radiobutton(self.cont3, variable=self.ver, value=2)
        self.f2.pack(side=LEFT)
        self.msg2 = Label(self.cont3, text=("F = (G " + ponto() + " m" + unzinho() + " " + ponto() + " m" + doizinho() + ") / d" + quadrado()))
        self.msg2["font"] = ("Arial", 10)
        self.msg2.pack()
        
        #botao 3 - relatividade
        self.f3 = Radiobutton(self.cont4, variable=self.ver, value=3)
        self.f3.pack(side=LEFT)
        self.msg3 = Label(self.cont4, text=("E = m " + ponto() + " c" + quadrado()))
        self.msg3["font"] = ("Arial", 10)
        self.msg3.pack()
        
        #botao 4 - caos
        self.f4 = Radiobutton(self.cont5, variable=self.ver, value=4)
        self.f4.pack(side=LEFT)
        self.msg4 = Label(self.cont5, text=("x" + doizinho() + " = k " + ponto() + " x" + unzinho() + " " + ponto() + " (1 - x" + unzinho() + ")"))
        self.msg4["font"] = ("Arial", 10)
        self.msg4.pack()
        
        #botao 5 - clapeyron
        self.f5 = Radiobutton(self.cont6, variable=self.ver, value=5)
        self.f5.pack(side=LEFT)
        self.msg5 = Label(self.cont6, text=("p " + ponto() + " V = n " + ponto() + " R " + ponto() + " T"))
        self.msg5["font"] = ("Arial", 10)
        self.msg5.pack()
        
        #botao 6 - torricelli
        self.f6 = Radiobutton(self.cont7, variable=self.ver, value=6)
        self.f6.pack(side=LEFT)
        self.msg6 = Label(self.cont7, text=("v" + quadrado() + " = v" + zerinho() + quadrado() + " + 2 " + ponto() + " a " + ponto() + " S"))
        self.msg6.pack()
        
        #botao 7 - gauss
        self.f7 = Radiobutton(self.cont8, variable=self.ver, value=7)
        self.f7.pack(side=LEFT)
        self.msg7 = Label(self.cont8, text=("1/f = (1/p) + (1/p')"))
        self.msg7.pack()
        
        #botao 8 - força sobre partícula
        self.f8 = Radiobutton(self.cont9, variable=self.ver, value=8)
        self.f8.pack(side=LEFT)
        self.msg8 = Label(self.cont9, text=("F = B " + ponto() + " i " + ponto() + " l " + ponto() + " sen(" + theta() +")"))
        self.msg8.pack()
        
        cons = [None, self.f1, self.f2, self.f3, self.f4, self.f5, self.f6, self.f7, self.f8]
        
        #botao penultimo - submeter
        self.sub = Button(self.contPU)
        self.sub["text"] = "Escolher"
        self.sub["font"] = ("Arial", 10)
        self.sub["width"] = 10
        self.sub["command"] = cons[self.ver.get() - 1].invoke()
        self.sub.invoke()
        self.sub.pack(side=BOTTOM)
        self.teste = Label(self.contPU, text=(str(self.ver.get())))
        self.teste.pack()
        
        #espaço para resultado
        self.mr = Label(self.contU, text="Resultado: ")
        self.mr["font"] = ("Arial", 16, "bold")
        self.mr["padx"] = 400
        self.mr.pack(side=LEFT)
        
        #botao ultimo - sair
        self.sair = Button(self.contU)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Arial", 10)
        self.sair["width"] = 5
        self.sair["padx"] = 20
        self.sair["command"] = self.contU.quit
        self.sair.pack(side=RIGHT)
    
    def defVar(self, variavel, valor):
        variavel = valor
    
    
    def inserirValores(self, funcao, Container):
        qtd = self.incog(funcao)
        
        if qtd != 0 :
            self.v1 = Entry(Container)
            self.v1["width"] = 8
            self.v1["font"] = ("Arial", 10)
            self.v1.pack(side=LEFT)
            self.v2 = Entry(Container)
            self.v2["width"] = 8
            self.v2["font"] = ("Arial", 10)
            self.v2.pack(side=LEFT)
            self.v3 = Entry(Container)
            self.v3["width"] = 8
            self.v3["font"] = ("Arial", 10)
            self.v3.pack(side=LEFT)
            
            if qtd > 3 :
                self.v4 = Entry(Container)
                self.v4["width"] = 8
                self.v4["font"] = ("Arial", 10)
                self.v4.pack(side=LEFT)
                
                if qtd > 4 :
                    self.v5 = Entry(Container)
                    self.v5["width"] = 8
                    self.v5["font"] = ("Arial", 10)
                    self.v5.pack(side=LEFT)
    
    
    def incog(self, f):
        if f in [1,3,4,7]:
            return 3
        elif f in [2, 5, 8]:
            return 5
        elif f == 7:
            return 4
        
        return 0
    
myApp = Main()

myApp.master.title("Resolvedor de Funções")
myApp.master.resizable(True, True)

myApp.mainloop()
