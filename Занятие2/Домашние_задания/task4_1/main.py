def pairwise(iterable):
    for i in range(len(iterable) - 1):
        sp = []
        sd = []
        lin = zip(iterable[i], iterable[i+1])
        for x in lin:
            dlinna = (x[1]-x[0])**2
            sp.append(dlinna)
        sd.append((sp[0] + sp[1])**0.5)
        yield sd


def task(st):
    sd = []
    y =0
    for pair in pairwise(st):
        sd.append(pair)
    for x in sd:
       y = y +x[0]
    return y




if __name__ == "__main__":
    pts = [
        (3, 4),
        (4.5, 3),
        (2.1, -1),
        (6.8, -3),
        (1.4, 2.9)
    ]
    print("Длинна ломаной", task(pts))