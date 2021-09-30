import discord
import datetime
import requests
import asyncio
from PIL import Image, ImageDraw, ImageFont, ImageOps
from discord.ext import commands, tasks
from io import BytesIO

TOKEN = open("ArquivosS/token.txt").readlines()[0].strip()

intents = discord.Intents.default()
intents.members = True

censored=["PUTINHA","VADIA","TU DE 4","TUDE4","PENIS","XEREÇAO","BOLAS","ORGASMO","BUC3TA","XEREQUINHA","CHUPA","XERECÂO","XERECÃO","PENIANO","FUDEDOR","SEX0","WEBSEXO","ANAL","BIXA","SEXO","GAY","PINTO","PÊNIS","PENIS","ALIENADO","ANIMALDETETA","ANORMAL","ARREGASSADO","ARROMBADO","BAITOLA","BALEIA","BARRIL","BENFIQUISTA","BIBA","BICHA","BIOS","BIROSKA","BOCAL","BOLAGATO","BOQUETEIRO","BOSTA","BUCETA","BUNDAO","BURRO","CABACO","CADELONA","CAFONA","CAMBISTA","CAPIROTO","COCODRILO","COCOZENTO","DEBILMENTAL","DEMENTE","DESCICLOPE","DESGRACADO","EGUENORANTE","ENDEMONIADO","ENERGUMENO","ENFIANOCU","ENGOLEROLA","ESCROTO","ESDRUXULO","ESPORRADO","ESTIGALHADO","ESTRUME","ESTRUNXADO","ESTUPIDO","FIDUMAEGUA","FILHODAPUTA","FUDER","FUDIDO","FULERA","GAMBIARRA","GEISYARRUDA","GONORREIA","GORDOESCROTO","GOZADO","HEREGE","IMBECIL","IMUNDO","INASCIVEL","INSETO","INVERTEBRADO","KOMODO","LAZARENTO","LAZARO","LEPROSO","LEZADO","LIMPEZAANAL","LOMBRIGA","MACACO","MARIMOON","MERETRIZ","MIOLODECU","MOCORONGO","MONTEDEMERDA","MORFETICO","MULAMBO","NAZISTA","NEWBIE","NONSENSE","OGRO",'OLHODOCU',"OLHOGORDO","OTARIO","PALHACO","PANACA","PARAGUAIO","PASSARALHO","PAUNOCU","PERIQUITA","PIMENTEIRA","PIPOCA","PIRANHA","PIROCA","PISTOLEIRA","PORRA","PROSTITUTA","PUNHETA","PUTAQUEPARIU","QUASIMODO","QUENGA","QUIRGUISTAO","RAMPERO","RAPARIGA","RUSGUENTO","SANGUESUGA","TAPADO","TARADO","TESAO","TETUDA","TETUDO","TRAGADO","TRAVESTI","TREPADEIRA","TROGLODITA","VACA","VADIA","VAGABUNDO","VAGARANHA","VAIAMERDA","VAISEFUDER","VAITOMARNOCU","VERME","VIADO","XAVASCA","XERECA","XIXIZENTO","XOXOTA","XUPETINHA","XUPISCO","XURUPITA","XUXEXO","XXX","ZEBUCETA","ZIGUIZIRA","ZONEIRA","ZUERA","ZURETA","PORN"] #Palavra para Censurar

bot = commands.Bot(command_prefix="!", CaseInsensitive=True, intents=intents)
@bot.event
async def on_ready():
    channel = bot.get_channel(892907539312807966)
    await channel.send("Bem-Vindos ao nosso Servidor Laboratório 51,  por favor, reaja com  <:lolicomunista:892905232059760680> este comentário para ter acesso aos demais canais do server!")
    print(f"Estou Pronto! Estou Conectado como {bot.user}!")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    lenc = len(censored)
    msg = message.content
    msg = msg.upper()
    for i in range(0,lenc):
        if censored[i-1] in msg :
            mensagem = await message.channel.send(f"Por favor {message.author.name}, não ofenda os demais usuários!")
            await message.delete()
            await asyncio.sleep(30)
            await mensagem.delete() 
            
    await bot.process_commands(message)

@bot.command(name="oi")
async def send_hello(ctx):
    name = ctx.author.name
    response = "Olá, "+name
    await ctx.send(response)

@bot.command(name="calcular")
async def calculate_expression(ctx,expression):
    expression = "".join(expression)
    calculate = eval(expression)
    channel = bot.get_channel(891390556612210790)
    name = ctx.author.name
    response = name+", a resposta é: "+str(calculate)
    await channel.send(response)

@bot.command(name="binance")
async def binance(ctx,coin,base):
    try:
        coin = coin.upper()
        base = base.upper()
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}{base}")
        data = response.json()
        price = data.get("price")
        channel = bot.get_channel(891428941791903805)
        name = ctx.author.name
        if price:
            if "USDT" in base:
                price = float(price)
                money = round(price,2)
                await channel.send(f"{name}, o valor do {coin}/{base} é ${money}")
            elif "BRL" in base:
                price = float(price)
                money = round(price,2)
                await channel.send(f"{name}, o valor do {coin}/{base} é R${money}")
            elif "EUR" in base:
                price = float(price)
                money = round(price,2)
                await channel.send(f"{name}, o valor do {coin}/{base} é €{money}")
            else:
                await channel.send(f"{name}, o valor do {coin}/{base} é {price}")
        else:
            await channel.send(f"{name}, o valor do {coin}/{base} é inválido")
    except Exception as error:
        await channel.send(f"Ops... {name} ,deu algum erro!")
        #print(error)

@bot.command(name="segredo")
async def secret(ctx):
    name = ctx.author.name
    try:
        await ctx.author.send(f"{name}, o segredo do século é...")
        await ctx.author.send("A palavra 'ovo' de trás pra frente continua 'ovo' =)")
    except discord.errors.Forbidden:
        await ctx.send(":hushed:") 
        await ctx.send(f"{name}, não posso te mandar o segredo, porfavor habilite receber mensagens de qualquer pessoas do servidor!")
        await ctx.send("(Opções > Privacidade)")

@bot.command(name="russia")
async def ussr(ctx):
    name = ctx.author.name
    channel = bot.get_channel(891744322905600040)
    try:
        url = requests.get(ctx.message.author.avatar_url)
        avatar = Image.open(BytesIO(url.content))
        img = Image.open("ArquivosS/stalin.jpg")
        hat = Image.open("ArquivosS/hat.png")

        hat = hat.resize((750,750))
        avatar = avatar.resize((400,400))
        bigavatar = (avatar.size[0]*3, avatar.size[1]*3)
        mascara = Image.new('L', bigavatar,0)
        recortar = ImageDraw.Draw(mascara)
        recortar.ellipse((0,0)+bigavatar,fill=255)
        mascara = mascara.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mascara)
        saida = ImageOps.fit(avatar, mascara.size, centering=(0.5, 0.5))
        saida.putalpha(mascara)
        saida.save("ArquivosS/avatar.png")

        fonte = ImageFont.truetype("ArquivosS/RussoOne-Regular.ttf", 40)
        escrever = ImageDraw.Draw(img)
        escrever.text(xy=(220,-5), text=name+" é Comunista",fill=(255,0,0), font=fonte)
        img.paste(avatar,(100,315), avatar)
        img.paste(hat,(-40,-50), hat)
        img.save("ArquivosS/ussr.png")

        await channel.send(file=discord.File("ArquivosS/ussr.png"))

    except:
        await channel.send(f"{name}, infelimente para funcionar o comando, primeiramente terás que ter uma foto de perfil")
        await channel.send("(Configuração de Usúario > Editar Perfil)")

@bot.event
async def on_member_join(member):
    name = member.name
    channel = bot.get_channel(891850029936041994)
    channel_cargo = bot.get_channel(892907539312807966)
    try:
        url = requests.get(member.avatar_url)
        avatar = Image.open(BytesIO(url.content))
        img = Image.open("ArquivosS/ingressar.jpg")

        avatar = avatar.resize((275,275))
        bigavatar = (avatar.size[0]*3, avatar.size[1]*3)
        mascara = Image.new('L', bigavatar,0)
        recortar = ImageDraw.Draw(mascara)
        recortar.ellipse((0,0)+bigavatar,fill=255)
        mascara = mascara.resize(avatar.size, Image.ANTIALIAS)
        avatar.putalpha(mascara)
        saida = ImageOps.fit(avatar, mascara.size, centering=(0.5, 0.5))
        saida.putalpha(mascara)
        saida.save("ArquivosS/avatarbv.png")

        fonte = ImageFont.truetype("ArquivosS/RussoOne-Regular.ttf", 40)
        escrever = ImageDraw.Draw(img)
        escrever.text(xy=(340,0), text=name,fill=(255,255,255), font=fonte)
        escrever.text(xy=(75,858), text="Bem-Vindo(a) Companheiro(a)",fill=(255,0,0), font=fonte)
        img.paste(avatar,(20,10), avatar)
        img.save("ArquivosS/ussrbv.png")
        
        await channel.send(f"{member.mention}, Bem-Vindo ao nosso Servidor, por favor entre no canal recepção e pegue o cargo turista reagindo com <:lolicomunista:892905232059760680> na mensagem presente! {channel_cargo.mention}")
        await channel.send(file=discord.File("ArquivosS/ussrbv.png"))
    except:
        await channel.send(f"{name}, infelimente para funcionar cartaz de Bem-Vindo, primeiramente terás que ter uma foto de perfil")
        await channel.send("(Configuração de Usúario > Editar Perfil)")

@bot.event
async def on_reaction_add(reaction, user):
    channel = bot.get_channel(892907539312807966)
    loli = 892905232059760680
    if reaction.emoji.id == loli:
        role = user.guild.get_role(891756085277491210)
        await user.add_roles(role)
    else:
        await channel.send("Error...")

@bot.command(name="time")
async def current_time(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%H:%M")
    channel = bot.get_channel(891070771127021598)
    name = ctx.author.name
    response = f"{ctx.author.mention}\n Hora Atual: "+now
    await channel.send(response)


bot.run(TOKEN)