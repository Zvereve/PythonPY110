def output_type_list(fn):
    def wrapper(*args, **kwargs):

        result = fn(*args, **kwargs)
        print(type(result), result)
        for _ in result:

            raise TypeError(
                    "Объект <{название или номер позиционного аргумента}> <значение аргумента> не является итерируемым")
    return wrapper


@output_type_list
def return_dict():
    return [{1:2}, "dfgtfgdf", "rtrtrtert"]


if __name__ == "__main__":
    return_dict()