import datetime
def task1():
    st = list(str(input("Строка")))
    st = list(set(st))
    sl = list(map(str.capitalize, st))
    sc = list(map(str.lower, st))
    print(list(zip(sl, sc)))

def task2():
    st = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
    sd = list(map(dict, zip(*[[(x , y) for y in value] for x, value in st.items()])))
    print(sd)
    return
def task3():
    st = [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]

    sd = list(map(" ".join, st))

    print(sd)
def task4():
    now = datetime.datetime.now()
    year = lambda x: x.year
    month = lambda x: x.month
    day = lambda x: x.day
    t = lambda x: x.time()
    dt = {"Year": year(now),
          "Month": month(now),
          "Time": str(t(now))}
    print(dt)
def task5():
    sa = []
    st = [12, 15, 151, "aba"]
    for x in st:
        f = (lambda x: str(x) == ''.join(reversed(str(x))))
        sa.append(f(x))
    print(sa)
def task6():
    st = ['red pink', 'white black', 'orange green']
    sa = ['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']
    ss = list(map((lambda x, y: x+" "+y), st, sa))
    print(ss)
if __name__ == "__main__":
    task6()