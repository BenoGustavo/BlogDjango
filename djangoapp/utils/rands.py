from random import SystemRandom
import string
from django.utils.text import slugify


def get_random_letters(k: int = 8) -> str:
    return "".join(SystemRandom().choices(string.ascii_letters + string.digits, k=k))


def create_slug(text: str) -> str:
    return slugify(text + "-" + get_random_letters(), allow_unicode=True)
