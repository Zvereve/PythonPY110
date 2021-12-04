import random
from string import ascii_lowercase, ascii_uppercase, digits
def rand(step =8):
    while True:
        f = []
        x =list(ascii_uppercase + ascii_lowercase+digits+digits)
        for i in range(step):
            f = ''.join(random.sample(x, step))
        yield f



if __name__ == "__main__":
    y = rand(25)
    print(next(y))
