import asyncio
import discord
import datetime
import random

client = discord.Client()

@client.event
async def on_ready():
    print("login")
    print(client.user.name)
    print(client.user.id)
    print("-------------------------")
    await client.change_presence(game=discord.Game(name='마이크체크', type=1))

    @client.event
    async def on_member_join(member):
        fmt = '{1.name}에 온걸 환영 한다., {0.mention}게이야'
        channel =  member.server.get_channel("channel_id_here")
        await client.send_message(channel, fmt.format(member, member.server))

    @client.event
    async def on_member_remove(member):
        channel = member.server.get_channel("channel_id_here")
        fmt = '{0.mention}게이가 나갔다.'
        await client.send_message(channel, fmt.format(member, member.server))


    @client.event
    async def on_message(message):
        if message.content.startswith('!정보'):
            date = datetime.datetime.utcfromtimestamp(((int(message.author.id) >> 22) + 1420070400000) / 1000)
            embed = discord.Embed(color=0x00ff00)
            embed.add_field(name="이름", value=message.author.name, inline=True)
            embed.add_field(name="서버이름", value=message.author.display_name, inline=True)
            embed.add_field(name="가입날짜", value=str(date.year) + "년" +str(date.month) + "월" +str(date.day) + "일", inline=True)
            embed.add_field(name="아이디", value=message.author.id, inline=True)
            embed.set_thumbnail(url=message.author.avatar_url)
            await client.send_message(message.channel, embed=embed)

        if message.content.startswith('!스폰지밥'):
            embed = discord.Embed(color=0x00ff00)
            embed.set_footer(text="ss")
            embed.set_image(url="https://ncache.ilbe.com/files/attach/new/20160118/377678/737853076/7333738691/2be888ee15f70de8eed821d45162caa5.jpg")
            await client.send_message(message.channel, embed=embed)


        if message.content.startswith('/안녕'):
            await client.send_message(message.channel, "반갑다")
        if message.content.startswith('/당신은?'):
            await client.send_message(message.channel, "나는 대한민국의 겁없는 mc 노박사입니다.")
        if message.content.startswith('/흔들어볼까요?'):
            await client.send_message(message.channel, "좋~지!")
        if message.content.startswith('/야 기분좋다'):
            await client.send_message(message.channel, "하아 언조비카이!")
        if message.content.startswith('!경제성장률'):
            mc = "6%입니다7%못해서죄송합니다 7%했으면됬지!그죠?"
            mcchoice = mc.split(" ")
            mcnumber = random.randint(1, len(mcchoice))
            mcresult = mcchoice[mcnumber-1]

            await client.send_message(message.channel, mcresult)


client.run('NTUwMzA3MTY5MzAwNjQzODcx.D1giwA.xOKQ1WclbE9K3-2PsnojUz6Mrso')