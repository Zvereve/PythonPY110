import json
import random
from mimesis import Person
from mimesis.locales import Locale
from mimesis import Field
from string import ascii_lowercase, ascii_uppercase, digits


# task1
def dect(a):
    y = "".join(str(x) for x in a)
    print(int(y, 2))


# task2
def wave(st):
    for x in [f'{st[:i]}{st.upper()[i:i + 1]}{st[i + 1:len(st)]}' for i in range(len(st))]:
        print(x)


# task3
def wave2(st="helo"):
    while True:
        for x in [f'{st[:i]}{st.upper()[i:i + 1]}{st[i + 1:len(st)]}' for i in range(len(st))]:
            yield x


# Task4
def alp(st):
    rd = {}
    ss = []
    summ = 0
    ralp = "".join(chr(i) for i in range(ord('а'), ord('а') + 32))
    for x, y in enumerate(ralp, start=1):
        rd.update({y: x})
    for i in st:
        for x in i:
            summ += rd.get(x, 0)
    print(summ)
    return summ


def str_(st):
    st = st.split()
    print(max(st, key=alp))


# Task5
def iznan(st="asd1fgy"):
    l = len(st)
    if l % 2 == 0:
        print("чет")
        return st[int(l / 2 - 1)::-1] + st[:int(l / 2 - 1):-1]
    else:
        print("не чет")
        return st[int(l / 2 - 1)::-1] + st[int(l / 2):int(l / 2 + 1)] + st[:int(l / 2):-1]


# Task6
def rti(st):
    roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    r = st[-1]
    rez = roman[r]
    for x in st[-2::-1]:
        if roman[x] >= roman[r]:
            rez += roman[x]
            r = x
        else:
            rez -= roman[x]
            r = x
    print(rez)
    return


# Task7
def rand(step=8):
    while True:
        f = []
        x = list(ascii_uppercase + ascii_lowercase + digits + digits)
        f = ''.join(random.sample(x, step))
        yield f


def randlogin():
    while True:
        f = []
        step = random.randint(3, 15)
        x = list(ascii_uppercase + ascii_lowercase + digits)
        f = ''.join(random.sample(x, step))
        yield f


def generate_person():
    person = Person(Locale.RU)
    t = Field(locale=Locale.RU)
    return {'name': person.name(),
            'surename': person.surname(),
            'Login': next(randlogin()),
            'password': next(rand()),
            'email': person.email(),
            'phone': person.telephone(),
            'register_time': t("timestamp", posix=False)}


def userlist(st):
    with open('UserList.json', 'a', encoding="utf-8") as f:
        json.dump(st, f, ensure_ascii=False, indent=4)



# dect([1, 0, 1, 1, 0])
# dect([1, 1, 1, 1, 0])
# wave("hello world")
# for i in range(5):
#    print(next(wave2()))
# str_("Мама мыла раму")
# print(iznan("вемпаерамваа"))
# rti('MCMCDXIX')
n = int(input("Число анкет"))
for _ in range(n):
    userlist(generate_person())
