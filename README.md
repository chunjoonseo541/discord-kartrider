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

# 사용법(localhost)
```py
from nextcord.ext import commands
from discord_kartrider import kartrider as kart

bot = commands.Bot(command_prefix='YOUR_PREFIX')

@bot.command()
async def 카트유저(ctx, name):
    await kart.kartrideruser(ctx, nexon_api, name, chromedriver_link, discord_module)

bot.run("YOUR_TOKEN_HERE")
```

# 사용법(Heroku)
```python
from nextcord.ext import commands
from discord_kartrider import kartrider as kart

bot = commands.Bot(command_prefix='YOUR_FREFIX')

@bot.command()
async def 카트유저(ctx, name):
    await kart.kartrideruser(ctx, nexon_api, name, discord_module)

bot.run("YOUR_TOKEN_HERE")
```