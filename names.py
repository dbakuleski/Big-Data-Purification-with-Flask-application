import json
import re
import requests
from cleanco import prepare_terms, basename


def get_companies_names():
    """
    Sending get request, saving the response as response object and extracting data in json format.

    :return: the extracted data in json format.
    """
    response = requests.get("http://127.0.0.1:5769/get-companies-names")
    data = response.json()
    return data


def post_companies_names():
    """
    Sending post request to post the data with a specific API.

    :return:
    """
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
    """
    Uses all the functions below for cleaning the company names.

    :param str name: the name of the company that is being cleaned
    :return: the final version of the name after cleaning
    """
    name = clean_company_name(name)
    name = cleanco_company_name(name)
    name = capital_letters(name)
    return name


def clean_company_name(name):
    """
    Processes company names by stripping away and removing unwanted characters (such as commas, brackets, quotation marks, etc.)

    :param str name: the name of the company that is being processed
    :return: the cleaned name of the company without unwanted characters
    """
    name = name.strip()
    name = name.split(",", 1)[0]
    name = name.replace('(', '').replace(')', '')
    name = name.replace('"', '')
    name = re.sub("\(.*?\)", "()", name)
    return name


def cleanco_company_name(name):
    """
    Processes company names by stripping away terms indicating organization type (such as "Ltd." or "Corp").

    :param str name: the name of the company that is being processed
    :return: the cleaned name of the company without terms indicating organization type
    """
    terms = prepare_terms()
    name = basename(name, terms)
    name = basename(name, terms)
    return name


def capital_letters(name):
    """
    Capitalizing the first letter of the company names like a header or a title.

    :param str name: the name of the company that is being capitalized
    :return: the name of the company with capital first letters
    """
    name = name.title()
    return name


post_companies_names()
