import json
import re

BOOKS_FILE = "books.md"
BOOK_REGEX = r'####\s+(?P<position>\d?\d)\.\s+\[(?P<book>.+?)\]\((?P<book_url>.*?)\) by (?P<author>.*?)\((?P<recommended>\d?\d.?\d?%) recommended\)\s+\!\[.*?\]\((?P<cover_url>.+?)\)\s+\"(?P<description>.+?)\"'  # TDO записать ругулярное выражения для поиска книги


def task():
    book_pattern = re.compile(BOOK_REGEX, re.DOTALL)  # флаг re.DOTALL описывает, что под символом точка может содержаться символ переноса строки
    res = list()
    with open(BOOKS_FILE) as f:
        for book in book_pattern.finditer(f.read()):
            print(json.dumps(book.groupdict(), indent=4))
            res.append(book.groupdict())
            res.sort(key=lambda diktel: int(diktel["position"]))
        with open("json.json", "w") as f:
            json.dump(res, f, indent=4, ensure_ascii=False)
if __name__ == '__main__':
    task()
