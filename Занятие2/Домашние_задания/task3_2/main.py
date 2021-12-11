def output_type_list(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        if not isinstance(result, int):
            raise TypeError(f"Результатом выполнения функции {fn} должен быть INT")

    return wrapper


@output_type_list
def return_list() -> list:
    return []


@output_type_list
def return_tuple() -> str:
    return ""


@output_type_list
def return_int() -> int:
    return 123

if __name__ == "__main__":
   # return_list()
   # return_tuple()
    return_int()
