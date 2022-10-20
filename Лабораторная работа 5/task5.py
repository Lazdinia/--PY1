import string
from random import sample


def get_random_password(n) -> str:

    a = sample(string.ascii_uppercase+string.ascii_lowercase+string.digits,n)
    a="".join(map(str,a))
    return a
...  # TODO написать функцию генерации случайных паролей


print(get_random_password(10))
