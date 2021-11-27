OUTPUT_FILE = "output.txt"


def task(steps = 11):
    with open('output.txt', "w", encoding="utf-8") as f:
        for n in range(1, steps):
            f.writelines(f'{"*" * n }\n'.rjust(steps))
    # TOO записать лесенку в файл


if __name__ == "__main__":
    task()

    with open(OUTPUT_FILE) as file:
        for line in file:
            print(line, end="")
