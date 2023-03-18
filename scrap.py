import requests
from bs4 import BeautifulSoup
import json
import os

URL = "https://padukata.com/2020/08/kamus-krama-inggil-lengkap/"

req = requests.get(URL)
parse = BeautifulSoup(req.text, "html.parser")

tables = parse.find_all("table")

for tabelAlphabet in tables:
    current_alphabet = tabelAlphabet.find_all("tr")[1].find_all("td")[1].text.strip()[0]
    kosakata = []

    for tr in tabelAlphabet.find_all("tr"):
        if tr.find_all("td")[0].text == "No":
            continue

        ngoko = tr.find_all("td")[1].text.strip()
        krama = tr.find_all("td")[2].text.strip()
        if not krama:
            krama = ngoko
        krama_inggil = tr.find_all("td")[3].text.strip()
        if not krama_inggil:
            krama_inggil = krama
        arti = tr.find_all("td")[4].text.strip()

        kosakata.append({
            "ngoko": ngoko,
            "krama": krama,
            "krama_inggil": krama_inggil,
            "arti": arti
        })

    with open(os.path.join("data/", current_alphabet + ".json"), "w") as outfile:
        json.dump(kosakata, outfile, indent=4)
