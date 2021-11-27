def pairwise(iterable):
    for i in range(len(iterable) - 1):
        yield iterable[i] + iterable[i+1]


def task():
    sd = []
    for pair in pairwise("ABCDEFG"):
        sd.append(pair)
    print(sd)


if __name__ == "__main__":
    task()
