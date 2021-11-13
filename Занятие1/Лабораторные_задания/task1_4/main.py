def list_comprehension(words: list) -> list:
    return [str.capitalize(x) for x in words]


def list_map(words: list) -> list:
    return list(map(str.capitalize, words))

if __name__ == "__main__":
    list_words = [
        "goldenROD",
        "puRPle",
        "sAlMoN",
        "TURQUOISE",
        "cYAN"
    ]
    print(list_comprehension(list_words))
    print(list_map(list_words))

