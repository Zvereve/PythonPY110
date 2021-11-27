from itertools import count


def header_footer(start: int =1, step: int = 2):
    num = start
    while True:
        yield num
        print(num)
        num *= step



if __name__ == "__main__":
   print(header_footer(5))
   print(header_footer(5))

