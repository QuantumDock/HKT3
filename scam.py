from bs4 import BeautifulSoup
import requests
import re
#  from timeit import timeit


def check_scam(number: str) -> bool:
    number.replace(" ", "").replace("-", "")
    if re.match(r"\+48[0-9]{9}", number):
        number.replace("+48", "")
    if not re.match(r"[0-9]{9}", number):
        raise SyntaxError
    try:
        soup = BeautifulSoup(requests.get(f"https://www.nieznany-numer.pl/Numer/{number}").text, "html.parser")
        return soup.select_one(".spec-WD").text.strip() in ["Negatywna", "Irytująca"]
    except Exception:
        return False

