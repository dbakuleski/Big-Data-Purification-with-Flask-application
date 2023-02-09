import json
import re
import requests
from cleanco import prepare_terms, basename


def get_companies_names():
    """

    :return:
    """
    response = requests.get("http://127.0.0.1:5769/get-companies-names")
    data = response.json()
    return data


def post_companies_names():
    companies = get_companies_names()
    for company in companies:
        name = final_name(company[1])
        dictionary = {"id": company[0],
                      "name": name,
                      "country_iso": company[2],
                      "city": company[3],
                      "nace": company[4],
                      "website": company[5]
                      }
        requests.post("http://127.0.0.1:5769/create", data=json.dumps(dictionary))


def final_name(name):
    name = clean_company_name(name)
    name = cleanco_company_name(name)
    name = capital_letters(name)
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


post_companies_names()
