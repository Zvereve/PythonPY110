def header_footer(start: int = 1, step: int = 2):
    while True:
        yield start
        start *= step


if __name__ == "__main__":
    y = header_footer(5, 25)
    for _ in range(10):
        print(next(y))