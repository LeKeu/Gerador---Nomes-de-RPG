from tkinter import *
import random as r

c = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
v = ['a', 'e', 'i', 'o', 'u']


def meio():
    l = ['de', 'da', 'of', 'thee', 'from', 'do']
    return r.choice(l)


def criarNome():
    label3 = Label(janela)
    label3.grid(column=1, row=3)
    label3["text"] = ""
    try:
        tam = int(tam_priNome_input.get())
    except ValueError:
        print("no")
    else:
        nome = ''
        vez = r.randint(0, 1)
        # forma aleatória para decidir se o nome começa com vogal ou consoante
        if vez:
            for n in range(tam):
                nome += r.choice(c)
                nome += r.choice(v)
        else:
            for n in range(tam):
                nome += r.choice(v)
                nome += r.choice(c)
        label3["text"] = nome.capitalize()
        print(nome.capitalize())

    try:
        tam1 = int(tam_sbrNome_input.get())
    except ValueError:
        pass
    else:
        nome1 = ''
        vez1 = r.randint(0, 1)
        if vez1:
            for n1 in range(tam1):
                nome1 += r.choice(c)
                nome1 += r.choice(v)
        else:
            for n1 in range(tam1):
                nome1 += r.choice(v)
                nome1 += r.choice(c)
        m = r.randint(0, 1)
        if m:
            label3["text"] += f" {nome1.capitalize()}"
        else:
            label3["text"] += f" {meio()} {nome1.capitalize()}"
        print(nome1.capitalize())


janela = Tk()  # começa assim
janela.title("Gerador de nomes - RPG")
#|||||||||||||
label1 = Label(janela, text="Quantidade de sílabas do Primeiro nome: ")
label1.grid(column=0, row=0)

tam_priNome_input = Entry(janela)
tam_priNome_input.grid(column=1, row=0)

label2 = Label(janela, text="Quantidade de sílabas do Sobrenome: ")
label2.grid(column=0, row=1)

tam_sbrNome_input = Entry(janela)
tam_sbrNome_input.grid(column=1, row=1)

but_prosseg = Button(janela, text="ok", command=criarNome)
but_prosseg.grid(column=1, row=2)




#|||||||||||||

janela.mainloop()