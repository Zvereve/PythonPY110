def header_footer(mf):  # TDO написать декоратор
    def wrapper():
        print("="*8)
        mf()
        print("="*8)

    return wrapper





@header_footer
def my_func():
    print("Hello World")


if __name__ == "__main__":
    my_func()
