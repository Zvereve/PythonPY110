def make_string_upper(fn):
    def wrapper():
        res = fn()
        res = res.upper()
        return  res
    return wrapper


@make_string_upper
def get_text() -> str:
    return "Hello, World!!!"


if __name__ == "__main__":
    print(get_text())
