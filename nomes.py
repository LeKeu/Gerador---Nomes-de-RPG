import random as r


c = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"]
v = ['a', 'e', 'i', 'o', 'u']


def criarNome(tam):
    nome = ''
    vez = r.randint(0, 1)
    #forma aleatória para decidir se o nome começa com vogal ou consoante
    if vez:
        for n in range(tam):
            nome += r.choice(c)
            nome += r.choice(v)
    else:
        for n in range(tam):
            nome += r.choice(v)
            nome += r.choice(c)
    return nome.capitalize()


def criarSobrenome(tam):
    nome = ''
    vez = r.randint(0, 1)
    if vez:
        for n in range(tam):
            nome += r.choice(c)
            nome += r.choice(v)
    else:
        for n in range(tam):
            nome += r.choice(v)
            nome += r.choice(c)
    return nome.capitalize()


def meio():
    l = ['de', 'da', 'of', 'thee', 'from', 'do']
    return r.choice(l)


if __name__ == "__main__":
    while True:
        t1 = int(input("Digite a quantidade de sílabas do primeiro nome: "))
        if t1 == 0:
            break
        t2 = int(input("Digite a quantidade de sílabas do sobrenome: "))
        if t2 != 0:
            vez = r.randint(0, 1)
            print(f"--> {criarNome(t1)} {criarSobrenome(t2)}") if vez else print(f"--> {criarNome(t1)} {meio()} {criarSobrenome(t2)}")
        else:
            print(f"--> {criarNome(t1)}")
