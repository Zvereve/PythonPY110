import json


def task():
    filename = "input.json"
    with open(filename, "r") as dat:
        f = json.load(dat)


    return max(f, key=lambda item: item["score"])


if __name__ == "__main__":
    print(task())
