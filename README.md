# discord-kartrider

**discord-kartrider** 는 단순하고 업데이트가 자주 될것입니다.

[![Downloads](https://static.pepy.tech/badge/discord_kartrider/month)](https://pepy.tech/project/discord_kartrider)
[![Supported Versions](https://img.shields.io/pypi/pyversions/discord_kartrider.svg)](https://pypi.org/project/discord_kartrider)
[![Contributors](https://img.shields.io/github/contributors/chunjoonseo541/discord-kartrider.svg)](https://github.com/chunjoonseo541/discord-kartrider/graphs/contributors)
[![Contributors](https://img.shields.io/pypi/v/discord-kartrider)](https://pypi.org/project/discord_kartrider)

# install
```
pip install discord-kartrider
```

# 사용법
```py
from discord.ext import commands
from discord_kartrider import kartrider as kart

bot = commands.Bot(command_prefix='YOUR_PREFIX')

@bot.event
async def on_ready():
    kart.kartrider.reload_file() # 메치 파일 업데이트

@bot.command()
async def 카트유저(ctx, name):
    id = kart.kartrider.id(name, API_KEY) # 유저의 ID가져오기
    level = kart.kartrider.level(name, API_KEY) # 유저의 level가져오기
    cart_text = kart.kartrider.cart_text(name, API_KEY) # 유저의 마지막에 탄 카트의 이름 가져오기
    cart_url = kart.kartrider.level(name, API_KEY) # 유저의 마지막에 탄 카트의 이름 가져오기
    game_type_text = kart.kartrider.game_type_text(name, API_KEY) # 유저의 마지막에 한 게임의 타입을 가져오기
    channel_name_text = kart.kartrider.channel_name_text(name, API_KEY) # 유저의 마지막에 한 게임의 채널 가져오기
    character_url = kart.kartrider.character_url(name, API_KEY) # 유저의 캐릭터 이미지 링크 가져오기
    character_text = kart.kartrider.character_text(name, API_KEY) # 유저의 캐릭터 이름 가져오기
    flying_pet_text = kart.kartrider.flying_pet_text(name, API_KEY) # 유저의 플라잉 팻 이름 가져오기
    pet_text = kart.kartrider.pet_text(name, API_KEY) # 유저의 팻 이름 가져오기
    license_text = kart.kartrider.license_text(name) # 유저의 캐릭터 텍스트 가져오기
    license_url = kart.kartrider.license_url(name) # 유저의 라이센스 이미지 링크 가져오기
    print(f"{id}{level}{character_url}{license_text}{license_url}... 이하 생략")

bot.run("YOUR_TOKEN_HERE")
```