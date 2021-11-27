import json


def task(input_filename: str, output_filename: str) -> None:
    with open('input.json', "r") as op:
        dat = json.load(op)
        with open('output.json', "w") as wr:
            json.dump(dat, wr, indent=4)




if __name__ == "__main__":
    input_file = "input.json"
    output_file = "output.json"

    task(input_file, output_file)

    with open(output_file) as output_f:
        for line in output_f:
            print(line, end="")
