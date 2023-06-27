
import time
import requests

data = {
    "accion": "consPorRuc",
    "razSoc": "",
    "nroRuc": "20600056477",
    "nrodoc": "",
    "token": "03AL8dmw-n7CgYqPxzqz7skVBw8-1-OqPRzNG9f3o2YaHOuB77kvSSBZaUKILHubUhI3tnTAxmssUMnAPDvDwf4U-kK6O1fqm280ALoeqle9jzuCwWWhLUyzetarrzzKGZkiVBW0dqVPuMk18QZtgtRwsA4eN1GAdxyR-Ox2GKzFQsgB_7paFZZhYY_-xZ93_Ynjofyq-Hn8dQzFGWDvGuykUOsFqd0ctvPUzzWTlvSllwO6o4uHI_LfRDklfqk7E6h1yLtRAfechc9V15LhagRqIjSrctzX6xnUp8hWsPLdJzbY6rtjSLsge46ABKclDsizwUpj2RpdOGhhwmTsbp4llLcodXLEWINjTIL34IxPTPUE_bCFn5PtY0N9OYX75QPGlHV5zXuZKZ1gK9eD1QTIf2RQ2j0P4ZxZGOL0B3-DOY0xcdGpO3935vxGRRmHxlfuArs-CWpjgpEhwN2-Nf-lv0ALg901ebKcfGPg9kgpKJSkr0e5XvGOPZb8P_bOm3YUox_ZBk9aKvSCSpgfWvtfFc9-HjusjqvIrH1Te7-hqNvJQnGXfIP-LYwdRi4PAwXVSMr5c9m9Ao",
    "contexto": "ti-it",
    "modo": "1",
    "rbtnTipo": "1",
    "search1": "20600056477",
    "tipdoc": "1",
    "search2": "",
    "search3": "",
    "codigo": ""
}

data2 = {
    "accion": "getRepLeg",
    "contexto": "ti-it",
    "modo": "1",
    "desRuc": "CUEROS AMESUR S.A.C.",
    "nroRuc": "20600056477"
}


headers = {
    "Content-Type": "application/x-www-form-urlencoded",
    "Origin": "https://e-consultaruc.sunat.gob.pe",
    "Referer": "https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias",
    "Sec-Ch-Ua": "\"Not.A/Brand\";v=\"8\", \"Chromium\";v=\"114\", \"Google Chrome\";v=\"114\"",
    "Sec-Ch-Ua-Mobile": "?0",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
}

time.sleep(1)  # Esperar 5 segundos antes de enviar la solicitud

response = requests.post("https://e-consultaruc.sunat.gob.pe/cl-ti-itmrconsruc/jcrS00Alias", headers=headers, data=data2)

# Imprimir la respuesta
print(response.text)


# Guardar la respuesta en un archivo llamado response2.html
with open('response2.html', 'w', encoding='utf-8') as f:
    f.write(response.text)