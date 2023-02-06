import re
import requests
from cleanco import basename
import string


def get_companies_names():
    response = requests.get("http://127.0.0.1:5964/get-company-names")
    data = response.json()
    return data


def clean_company_name(name):
    print("Cleaning company name")
    name = name.strip()
    name = name.replace(" ", "")
    name = re.sub(r"[^a-zA-Z0-9]+", "", name)
    print("Finished cleaning company name")
    return name


cleaned_company_name = clean_company_name(company_name)
cleaned_company_name = basename(cleaned_company_name)
cleaned_company_name = basename(cleaned_company_name)


def normal_company_name():
    normal_name = string.capwords(cleaned_company_name)
    return normal_name
