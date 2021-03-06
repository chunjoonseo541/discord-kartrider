import requests, bs4
from zipfile import ZipFile
from io import BytesIO
from json import load

class kartrider():
    def __init__(self): pass
    
    def id(name, api_key):
        return requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]

    def level(name, api_key):
        return requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["level"]

    def cart_text(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        cart = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]['kart']
        data = load(open('kart.json', encoding='utf-8'))
        for i in data:
            if i['id'] == cart:
                return i['name']

    def cart_url(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        cart = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]['kart']
        return f"https://s3-ap-northeast-1.amazonaws.com/solution-userstats/metadata/kart/{cart}.png"
            
    def game_type_text(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        gametype = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]['matchType']
        data = load(open('gameType.json', encoding='utf-8'))
        for i in data:
            if i['id'] == gametype:
                return i['name']

    def channel_name_text(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        gametype = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]['channelName']
        if gametype == 'speedIndiCombine':
            gametype = '?????? ??????????????????'
        elif gametype == 'speedTeamCombine':
            gametype = '?????? ???????????????'
        elif gametype == 'speedIndiFastest':
            gametype = '???????????? ??????????????????'
        elif gametype == 'speedTeamFastest':
            gametype = '???????????? ???????????????'
        elif gametype == 'speedIndiInfinit':
            gametype = '??????????????? ??????????????????'
        elif gametype == 'speedTeamInfinit':
            gametype = '??????????????? ??????????????????'
        elif gametype == 'clubRace_speed':
            gametype == '????????? ?????? ?????????'
        elif gametype == 'tierMatching_speedIndi':
            gametype = '?????????????????? ?????????'
        elif gametype == 'tierMatching_speedTeam':
            gametype = '?????????????????? ??????'
        elif gametype == 'bokbulbokSpeedIndi':
            gametype = 'V1 ?????? ????????? ??????????????????'
        elif gametype == 'grandprix_speedIndiInfinit':
            gametype = '?????? ????????? ???????????? ??????????????????'
        elif gametype == 'itemIndiCombine':
            gametype = '?????? ???????????????'
        elif gametype == 'itemTeamCombine':
            gametype = '?????? ??????????????????'
        elif gametype == 'itemNewItemIndiFastest2Enchant':
            gametype = '???????????? ??????????????????'
        elif gametype == 'itemNewItemTeamFastest2Enchant':
            gametype = '???????????? ???????????????'
        elif gametype == 'clubRace_item':
            gametype = '????????? ?????? ?????????'
        elif gametype == 'grandprix_itemNewItemIndi':
            gametype = '?????? ?????????????????? ????????????'
        elif gametype == 'tierMatching_itemNewItemTeam':
            gametype = '??????????????????'
        elif gametype == 'battle':
            gametype = '????????? ??????'
        
        return gametype

    def character_url(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        character = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]["character"]
        return f'https://s3-ap-northeast-1.amazonaws.com/solution-userstats/metadata/character/{character}.png'

    def character_text(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        character = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]["character"]
        data = load(open('character.json', encoding='utf-8'))
        for i in data:
            if i['id'] == character:
                return i['name']

    def flying_pet_text(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        flyingpet = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]["flyingPet"]
        data = load(open('flyingPet.json', encoding='utf-8'))
        for i in data:
            if i['id'] == flyingpet:
                return i['name']

    def pet_text(name, api_key):
        id = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/nickname/{name}", headers={'Authorization': api_key}).json()["accessId"]
        pet = requests.get(f"https://api.nexon.co.kr/kart/v1.0/users/{id}/matches?start_date=&end_date=&offset=1&limit=1&match_types=", headers={'Authorization': api_key}).json()["matches"][0]["matches"][0]["player"]["pet"]
        data = load(open('pet.json', encoding='utf-8'))
        for i in data:
            if i['id'] == pet:
                return i['name']

    def license_url(name, api_key=None):
        result = requests.get(f'https://bazzi.gg/rider/{name}').text
        soup = bs4.BeautifulSoup(result, 'lxml')
        license = soup.find('span', {'class':'license'}).get_text()
        if license == "??????":
            url = "https://tmi.nexon.com/img/icon_beginner.png"
        if license == "??????":
            url = "https://tmi.nexon.com/img/icon_rookie.png"
        if license == "L3":
            url = "https://tmi.nexon.com/img/icon_l3.png"
        if license == "L2":
            url = "https://tmi.nexon.com/img/icon_l2.png"
        if license == "L1":
            url = "https://tmi.nexon.com/img/icon_l1.png"
        if license == "L1/?????????":
            url = "https://tmi.nexon.com/img/icon_l1.png"
        if license == "PRO":
            url = "https://tmi.nexon.com/img/icon_PRO.png"
        return url

    def license_text(name, api_key=None):
        result = requests.get(f'https://bazzi.gg/rider/{name}').text
        soup = bs4.BeautifulSoup(result, 'lxml')
        license = soup.find('span', {'class':'license'}).get_text()
        return license

    def reload_file():
        ZIP = ZipFile(BytesIO(requests.get('https://static.api.nexon.co.kr/kart/latest/metadata.zip').content))
        ZIP.extract('character.json')
        ZIP.extract('kart.json')
        ZIP.extract('flyingPet.json')
        ZIP.extract('pet.json')
        ZIP.extract('gameType.json')
        return print('(discord-kartrider) - ???????????? ??????!')