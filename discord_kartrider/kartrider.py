import requests, bs4
from zipfile import ZipFile
from io import BytesIO
from os import chdir

class kartrider():
    def __init__(self):
        pass
    
    def id(name, api_key):
        return requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]

    def level(name, api_key):
        return requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["level"]

    def character_url(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        character = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]["character"]
        return f'https://s3-ap-northeast-1.amazonaws.com/solution-userstats/metadata/character/{character}.png'

    def license_url(name):
        result = requests.get(f'https://bazzi.gg/rider/{name}').text
        soup = bs4.BeautifulSoup(result, 'lxml')
        license = soup.find('span', {'class':'license'}).get_text()
        if license == "초보":
            url = "https://tmi.nexon.com/img/icon_beginner.png"
        if license == "뉴비":
            url = "https://tmi.nexon.com/img/icon_rookie.png"
        if license == "L3":
            url = "https://tmi.nexon.com/img/icon_l3.png"
        if license == "L2":
            url = "https://tmi.nexon.com/img/icon_l2.png"
        if license == "L1":
            url = "https://tmi.nexon.com/img/icon_l1.png"
        if license == "L1/마엠블":
            url = "https://tmi.nexon.com/img/icon_l1.png"
        if license == "PRO":
            url = "https://tmi.nexon.com/img/icon_PRO.png"
        return url
    def license_text(name):
        result = requests.get(f'https://bazzi.gg/rider/{name}').text
        soup = bs4.BeautifulSoup(result, 'lxml')
        license = soup.find('span', {'class':'license'}).get_text()
        return license



if __name__ == "__main__":
    chdir("/")
    ZipFile(BytesIO(requests.get('https://static.api.nexon.co.kr/kart/latest/metadata.zip').content)).extractall(r'discord-kartrider')
    api_key = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJhY2NvdW50X2lkIjoiMTk0Njg0MDUyNCIsImF1dGhfaWQiOiIyIiwidG9rZW5fdHlwZSI6IkFjY2Vzc1Rva2VuIiwic2VydmljZV9pZCI6IjQzMDAxMTM5MyIsIlgtQXBwLVJhdGUtTGltaXQiOiI1MDA6MTAiLCJuYmYiOjE2NDQ4MDA0MTksImV4cCI6MTY2MDM1MjQxOSwiaWF0IjoxNjQ0ODAwNDE5fQ.S2C3wwTpp8ESE1xNNtKeBy65uSU_dURtver4CvLA1As"
    id = kartrider.license_text(name='붐힐과태료남')
    print(id)