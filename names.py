import re
import requests
from cleanco import basename


def get_companies_names():
    response = requests.get("http://127.0.0.1:5964/get-companies-names")
    #    data = response.json()
    print(response.status_code)
    print(response.text)
    return "data"


def clean_company_name(name):
    name = name.strip()
    name = name.replace(" ", "")
    name = re.sub(r"[^a-zA-Z0-9]+", "", name)
    # name = cleanco_company_name(name)
    return name


def cleanco_company_name(name):
    name = basename(name)
    name = basename(name)
    return name


def capital_letters(name):
    return name.title()


def capitalize_abbreviations(name):
    name = re.sub(r"\b[a-zA-Z]+(\.[a-zA-Z]+)*\b", lambda x: x.group().upper(), name)
    return name
