def task(camel_case_str: str) -> str:
    return "".join(str(x) for x in camel_case_str if str.islower(x))  # TODO отфильтровать только буквы нижнего регистра


if __name__ == "__main__":
    word = "AbCdEfGh"
    print(task(word))
