INPUT_FILE = "input.txt"
OUTPUT_FILE = "output.txt"


def task():
    with open('input.txt', "r") as f:
        with open('output.txt', "w") as fi:
            for x in f:
                fi.write(x.upper())


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
