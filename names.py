import string
import re
import requests
from cleanco import prepare_terms, basename


def get_companies_names():
    response = requests.get("http://127.0.0.1:5964/get-companies-names")
    data = response.json()
    # print(response.status_code)
    # print(response.text)
    return data


# def post_companies_names():
#     companies = requests.get("http://127.0.0.1:5964/get-companies-names").json()
#     for company in companies:
#         company = final_name(company)
#     response = requests.post("http://127.0.0.1:5964/create", data=json.dumps(company))
#     return response


def final_name(name):
    name = capital_letters(name)
    name = clean_company_name(name)
    name = cleanco_company_name(name)
    name = capitalize_abbreviations(name)
    return name


def clean_company_name(name):
    name = name.strip()
    name = name.split(",", 1)[0]
    name = name.replace('(', '').replace(')', '')
    name = name.replace('"', '')
    name = re.sub("\(.*?\)", "()", name)
    return name


def cleanco_company_name(name):
    terms = prepare_terms()
    name = basename(name, terms)
    name = basename(name, terms)
    return name


def capital_letters(name):
    name = name.title()
    return name


def capitalize_abbreviations(name):
    name = re.sub(r"\b[a-zA-Z]+(\.[a-zA-Z]+)*\b", lambda x: x.group().upper(), name)
    return name
