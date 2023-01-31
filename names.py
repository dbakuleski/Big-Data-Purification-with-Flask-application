import re
import requests

response = requests.get("http://127.0.0.1:5350/")
oneCompany = response.json()
print(oneCompany)


cleaned_names = []
for name in oneCompany:
    name = name.strip()
    name = name.replace(" ", "")
    name = re.sub(r"[^a-zA-Z0-9]+", "", name)
    cleaned_names.append(name)





