# -*- coding: utf-8 -*
import discord
import datetime
import random
import aiocron

client = discord.Client()

content_dict = {
    'ㄚㄇ': {
        '該做什麼': 'ㄚㄇ喝水！ myfriend',
        '我們來玩好玩的遊戲': '喝水遊戲',
        '水喝不夠': '打屁股！',
        '今天有喝水水': '你好棒棒:cowboy::cowboy::star_struck::star_struck::partying_face::partying_face:',
        '喝飲料': '壞壞:rage:',
        '的腎你還好嗎': ['給我...水水...', '救命......'],
    },
    '預備備': '喝水!',
    '一天要喝多少ㄈㄈ': '兩千ㄈㄈ',
    '現在是什麼時間': 'ㄚㄇ喝水的時間！'
}

CHANNEL_ID = ###CHANGE ME###

@client.event
async def on_ready():
    print(f'Login as: {client.user}')

@client.event
async def on_message(message):
    myfriend = '<@###ID###>'
    now = datetime.datetime.now()

    if message.author == client.user:
        return

    if message.content == 'DrinkWaterBot --help':
        response = """
        使用方法 -
        你可以問:
        """
        content_list = []
        for k, v in content_dict.items():
            if isinstance(v, dict):
                for k2, v2 in v.items():
                    content_list.append('\t\t\t{0} {1}'.format(k, k2))
            else:
                content_list.append('\t\t\t{0}'.format(k))
        text = response + '\n' + '\n'.join(content_list)
        await message.channel.send('{0}'.format(text))

    if now.weekday() not in [5, 6] and (now.hour < 5 or now.hour > 20):
       specify_user = myfriend
    else:
       specify_user = ""
    if 'ㄚㄇ' in message.content:
        for k, v in content_dict['ㄚㄇ'].items():
            if k in message.content:
                if isinstance(v, list):
                    v = random.choice(v)
                v = v.replace("myfriend", specify_user)
                await message.channel.send('{0}'.format(v))
    for k, v in content_dict.items():
        if k in message.content and not isinstance(v, dict):
            await message.channel.send('{0}'.format(v))

@aiocron.crontab('14 20-23,0-5 * * *')
async def reminder_drinking():
    channel = client.get_channel(CHANNEL_ID)
    await channel.send('現在是喝水時間')

client.run('')
