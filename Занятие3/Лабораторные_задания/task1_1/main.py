INPUT_FILE = "input.txt"


def task() -> None:
    with open('input.txt') as file:  # TOO открыть указатель на файл
        for line in file:
            print(line, end="")



if __name__ == "__main__":
    task()
