import random
from string import ascii_lowercase, ascii_uppercase, digits


def time_decorator(fn):
    def wrapper(*args):
        with open('output.txt', "a") as file:
            file.write(*args)
    return wrapper


def rand(step=8):
    while True:
        f = []
        x =list(ascii_uppercase + ascii_lowercase+digits+digits)
        f = ''.join(random.sample(x, step))
        yield f


def outp(step=3):
    with open('output.txt', "r") as file:
        while True:
            yield file.read(step)





@time_decorator
def wrt(a):
    return a



if __name__ == "__main__":

   # with open('input.txt', "a") as file:
   #     file.write(f'{next(rand())}, ')
    #with open('input1.txt', "a") as file:
    #    file.write(f'{next(rand())}, ')

    #with open('input.txt', "r") as file:
    #    with open('input1.txt', "r") as f:
    #        wrt(f'{file.read()}{f.read()}')
    y = outp()
    print(next(y))
    print(next(y))