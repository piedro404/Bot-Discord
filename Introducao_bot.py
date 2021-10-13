import os
import discord
import datetime
import youtube_dl
import time
#PyNaCl
from discord import embeds
from discord import channel
from discord import guild
from discord.channel import VoiceChannel
from discord.ext.commands.errors import CommandNotFound, MissingRequiredArgument, CommandInvokeError
import requests
import asyncio
from PIL import Image, ImageDraw, ImageFont, ImageOps
from discord.ext import commands, tasks
from io import BytesIO
from requests.models import Response

intents = discord.Intents.default()
intents.members = True
listmc=[]

censored=["PUTINHA","VADIA","TU DE 4","TUDE4","PENIS","XEREÇAO","BOLAS","ORGASMO","BUC3TA","XEREQUINHA","CHUPA","XERECÂO","XERECÃO","PENIANO","FUDEDOR","SEX0","WEBSEXO","ANAL","BIXA","SEXO","GAY","PINTO","PÊNIS","PENIS","ALIENADO","ANIMALDETETA","ANORMAL","ARREGASSADO","ARROMBADO","BAITOLA","BALEIA","BARRIL","BENFIQUISTA","BIBA","BICHA","BIOS","BIROSKA","BOCAL","BOLAGATO","BOQUETEIRO","BOSTA","BUCETA","BUNDAO","BURRO","CABACO","CADELONA","CAFONA","CAMBISTA","CAPIROTO","COCODRILO","COCOZENTO","DEBILMENTAL","DEMENTE","DESCICLOPE","DESGRACADO","EGUENORANTE","ENDEMONIADO","ENERGUMENO","ENFIANOCU","ENGOLEROLA","ESCROTO","ESDRUXULO","ESPORRADO","ESTIGALHADO","ESTRUME","ESTRUNXADO","ESTUPIDO","FIDUMAEGUA","FILHODAPUTA","FUDER","FUDIDO","FULERA","GAMBIARRA","GEISYARRUDA","GONORREIA","GORDOESCROTO","GOZADO","HEREGE","IMBECIL","IMUNDO","INASCIVEL","INSETO","INVERTEBRADO","KOMODO","LAZARENTO","LAZARO","LEPROSO","LEZADO","LIMPEZAANAL","LOMBRIGA","MACACO","MARIMOON","MERETRIZ","MIOLODECU","MOCORONGO","MONTEDEMERDA","MORFETICO","MULAMBO","NAZISTA","NEWBIE","NONSENSE","OGRO",'OLHODOCU',"OLHOGORDO","OTARIO","PALHACO","PANACA","PARAGUAIO","PASSARALHO","PAUNOCU","PERIQUITA","PIMENTEIRA","PIPOCA","PIRANHA","PIROCA","PISTOLEIRA","PORRA","PROSTITUTA","PUNHETA","PUTAQUEPARIU","QUASIMODO","QUENGA","QUIRGUISTAO","RAMPERO","RAPARIGA","RUSGUENTO","SANGUESUGA","TAPADO","TARADO","TESAO","TETUDA","TETUDO","TRAGADO","TRAVESTI","TREPADEIRA","TROGLODITA","VACA","VADIA","VAGABUNDO","VAGARANHA","VAIAMERDA","VAISEFUDER","VAITOMARNOCU","VERME","VIADO","XAVASCA","XERECA","XIXIZENTO","XOXOTA","XUPETINHA","XUPISCO","XURUPITA","XUXEXO","XXX","ZEBUCETA","ZIGUIZIRA","ZONEIRA","ZUERA","ZURETA","PORN"] #Palavra para Censurar

bot = commands.Bot(command_prefix="!", CaseInsensitive=True, intents=intents)
@bot.event
async def on_ready():
    channel = bot.get_channel(892907539312807966)
    #await channel.send("Bem-Vindos ao nosso Servidor Laboratório 51,  por favor, reaja com  <:lolicomunista:892905232059760680> este comentário para ter acesso aos demais canais do server!")
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
            mensagem = await message.channel.send(f"Por favor {message.author.mention}, não ofenda os demais usuários!")
            await message.delete()
            await asyncio.sleep(30)
            await mensagem.delete() 
            
    await bot.process_commands(message)

@bot.command(name="oi", help="Envia um Oi. Não requer argumentos!")
async def send_hello(ctx):
    name = ctx.author.name
    response = f"Olá, {ctx.author.mention}"
    await ctx.send(response)

@bot.command(name="calcular", help="Calcula uma expressão. Argumento: Expressão sem espaços!")
async def calculate_expression(ctx,expression):
    expression = "".join(expression)
    channel = bot.get_channel(891390556612210790)
    name = ctx.author.name
    embed_mat = discord.Embed(title = "Resultado da Expressão",description = "PS: Não pode haver espaços em meio a expressão",color = 0x778899)
    embed_mat.set_footer(text=f"Pesquisa feita para {name} atrávez do comando !calcular (expressão)", icon_url=ctx.message.author.avatar_url)
    embed_mat.set_thumbnail(url="https://cdn.pixabay.com/photo/2016/07/29/21/42/school-1555910_960_720.png")
    
    if("+" in expression or "-" in expression or "*" in expression or "/" in expression  or "^" in expression  or "%" in expression):
        calculate = eval(expression)
        
        embed_mat.add_field(name="Expressão", value=f"{expression}")
        embed_mat.add_field(name="Resultado", value=f"{str(calculate)}", inline=False)
        await channel.send(f"{ctx.author.mention}, está aqui o resultado ",embed=embed_mat)
    else:
        await channel.send(f"{ctx.author.mention}, algo deu errado =(")
@bot.command(name="binance", help="Verifica o preço de um par na binance. Argumentos: (moeda)(base)!")
async def binance(ctx,coin,base):
    try:
        coin = coin.upper()
        base = base.upper()
        response = requests.get(f"https://api.binance.com/api/v3/ticker/price?symbol={coin}{base}")
        data = response.json()
        price = data.get("price")
        channel = bot.get_channel(891428941791903805)
        name = ctx.author.name
        embed_binance=discord.Embed(title = "Binance",description = "OBS: A busca é realizada atrávez de uma API do próprio site",color = 0x32CD32)
        embed_binance.set_thumbnail(url="https://logodownload.org/wp-content/uploads/2021/03/binance-logo-1.png")  
        embed_binance.set_footer(text=f"Pesquisa feita para {name} atrávez do comando !binance (coin)(base)", icon_url=ctx.message.author.avatar_url)
        if price:
            if "USDT" in base:
                price = float(price)
                money = round(price,2)
                embed_binance.add_field(name=f"{coin} -> {base}:", value=f"$ {money}", inline=True)
                embed_binance.set_image(url="https://cdn.pixabay.com/photo/2017/07/01/14/04/dollar-2461576_960_720.png")
                await channel.send(f"{ctx.author.mention},",embed=embed_binance)
            elif "BRL" in base:
                price = float(price)
                money = round(price,2)
                embed_binance.add_field(name=f"{coin} -> {base}:", value=f"R$ {money}", inline=True)
                embed_binance.set_image(url="https://thumbs.dreamstime.com/b/moeda-real-do-brasileiro-um-isolada-no-fundo-branco-de-124134700.jpg")
                await channel.send(f"{ctx.author.mention},",embed=embed_binance)
            elif "EUR" in base:
                price = float(price)
                money = round(price,2)
                embed_binance.add_field(name=f"{coin} -> {base}:", value=f"€ {money}", inline=True)
                embed_binance.set_image(url="https://cdn.pixabay.com/photo/2017/07/01/14/04/euro-2461577_960_720.png")
                await channel.send(f"{ctx.author.mention},",embed=embed_binance)
            else:
                embed_binance.add_field(name=f"{coin} -> {base}:", value=f"{base} {price}", inline=True)
                embed_binance.set_image(url="https://images.vexels.com/media/users/3/146881/isolated/preview/c9358db7338035de67f494f317a1ef61-moedas.png")
                await channel.send(f"{ctx.author.mention},",embed=embed_binance)
        else:
            embed_binance.add_field(name=f"{coin} -> {base}:", value="É Invalido, tente com outra combinação!", inline=True)
            embed_binance.set_image(url="https://cdn.pixabay.com/photo/2012/04/24/12/29/no-symbol-39767_960_720.png")
            await channel.send(f"{ctx.author.mention},",embed=embed_binance)
    except Exception as error:
        await channel.send(f"Ops... {ctx.author.mention} ,deu algum erro!")
        #print(error)

@bot.command(name="segredo", help="Envia um segredinho no seu privado. Não requer argumentos!")
async def secret(ctx):
    name = ctx.author.name
    try:
        await ctx.author.send(f"{ctx.author.mention}, o segredo do século é...")
        await ctx.author.send("A palavra 'ovo' de trás pra frente continua 'ovo' =)")
    except discord.errors.Forbidden:
        await ctx.send(":hushed:") 
        await ctx.send(f"{ctx.author.mention}, não posso te mandar o segredo, porfavor habilite receber mensagens de qualquer pessoas do servidor!")
        await ctx.send("(Opções > Privacidade)")

@bot.command(name="russia", help="Enviar uma edit de sua foto de perfil do Discord. É requerido que tenha uma foto no seu perfil!")
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

        await channel.send(f"{ctx.author.mention}, ",file=discord.File("ArquivosS/ussr.png"))

    except:
        await channel.send(f"{ctx.author.mention}, infelimente para funcionar o comando, primeiramente terás que ter uma foto de perfil")
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
        
        await channel.send(f"{member.mention}, Bem-Vindo(a) ao nosso Servidor, por favor entre no canal recepção e pegue o cargo turista reagindo com <:lolicomunista:892905232059760680> na mensagem presente! {channel_cargo.mention}",file=discord.File("ArquivosS/ussrbv.png"))
    except:
        await channel.send(f"{member.mention}, infelimente para funcionar cartaz de Bem-Vindo, primeiramente terás que ter uma foto de perfil")
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

@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, MissingRequiredArgument):
        await ctx.send(f"Por Favor {ctx.author.mention}, envie todos os argumentos requiridos para o comando funcionar. Digite !help para ver os parâmetros de cada comando!")
    elif isinstance(error, CommandNotFound):
        await ctx.send(f"{ctx.author.mention}, este comando não existe. Digite !help para ver os comando do bot!")
    else:
        raise error

@bot.command(name="foto", help="Envia uma foto aleatória. Não requer argumentos!")
async def get__randow_image(ctx):
    url_image = "https://picsum.photos/1920/1080.jpg"
    response = requests.get(url_image)
    channel = bot.get_channel(894731073123127347)
    name=ctx.author.name

    embed_photo = discord.Embed(title = "Resultado da Busca da Imagem",description = "PS: A busca é totalmente aleatória",color = 0x00BFFF)
    embed_photo.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_photo.set_footer(text=f"Pesquisa feita para {name} atrávez do comando !foto", icon_url=ctx.message.author.avatar_url)
    embed_photo.add_field(name="API", value="Usamos a API do https://picsum.photos")
    embed_photo.add_field(name="Parâmetros", value="{largura}/{altura}")
    embed_photo.add_field(name="Exemplo", value=url_image, inline=False)
    embed_photo.set_image(url=url_image)

    await channel.send(f"{ctx.author.mention}, está aqui a foto aleatória ",embed=embed_photo)

@bot.command(name="time", help="Pegar o tempo de acordo com o server local. Não requer argumentos!")
async def current_time(ctx):
    now = datetime.datetime.now()
    now = now.strftime("%H:%M")
    channel = bot.get_channel(891070771127021598)
    name = ctx.author.name
    embed_time=discord.Embed(title = "Hora Atual",description = "OBS: A busca é realizada no servidor local",color = 0x708090)
    embed_time.set_thumbnail(url="https://images.vexels.com/media/users/3/151641/isolated/preview/4df6c21a932dc60b655649a55a602010-ilustracao-vetorial-de-relogio.png")
    embed_time.set_footer(text=f"Pesquisa feita para {name} atrávez do comando !time", icon_url=ctx.message.author.avatar_url)
    embed_time.add_field(name="Tempo:", value=now, inline=True)

    await channel.send(f"{ctx.author.mention},",embed=embed_time)

@bot.command(name="join", help="Faz o bot entrar no canal de música do server. Não requer argumentos!")
async def join(ctx):
    channel = bot.get_channel(897530495133446185)
    channelm = bot.get_channel(897530822364631130)
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name=channelm.name)
    try:
        await voiceChannel.connect()
    except:
        await channel.send(f"{ctx.author.mention}, o bot ja está no canal {channelm.mention}")
    

@bot.command(name="play", help="Inicia uma música selecionada. Argumento: (url)!")
async def play(ctx, url : str):
    channel = bot.get_channel(897530495133446185)
    channelm = bot.get_channel(897530822364631130)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    try:
        if voice.is_playing():
            voice.stop()
        if not voice is None: 
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': "bestaudio"}

            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(url, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                voice.play(source)
    except:
        if voice is None: 
            await channel.send(f"{ctx.author.mention}, o bot não está no canal {channelm.mention}, use !join")
        else:
            await channel.send(f"{ctx.author.mention}, o seu comando foi digitado incorreto, consute !help para ver os comando do bot!")

@bot.command(name="leave", help="Faz o bot sair do canal de música. Não requer argumentos!")
async def leave(ctx):
    channel = bot.get_channel(897530495133446185)
    channelm = bot.get_channel(897530822364631130)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await channel.send(f"{ctx.author.mention}, eu não estou conectado ao canal {channelm.mention}")

@bot.command(name="pause", help="Pausa a música que estiver tocando no momento. Não requer argumentos!")
async def pause(ctx):
    channel = bot.get_channel(897530495133446185)
    channelm = bot.get_channel(897530822364631130)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await channel.send(f"{ctx.author.mention}, eu já estou pausado neste exato momento, no canal {channelm.mention}")

@bot.command(name="resume", help="Retorna a música que foi interropida. Não requer argumentos!")
async def resume(ctx):
    channel = bot.get_channel(897530495133446185)
    channelm = bot.get_channel(897530822364631130)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await channel.send(f"{ctx.author.mention}, eu já estou tocando neste exato momento, no canal {channelm.mention}")

@bot.command(name="stop", help="Para música que estiver tocando. Não requer argumentos!")
async def stop(ctx):
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    voice.stop()

@bot.command(name="list", help="Playlist varias músicas. Argumento: (url)!")
async def list(ctx, url : str):
    channel = bot.get_channel(897530495133446185)
    YDL_OPTIONS = {'format': "bestaudio"}
    with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            if ydl.extract_info(url, download=False):
                listmc.append(url)
        except:
            await channel.send(f"{ctx.author.mention}, está URL é invalida, verifique a URL novamente!")

@bot.command(name="printl", help="Mostra todas as música presentes na playlist. Não requer argumentos!")
async def printl(ctx):
    channel = bot.get_channel(897530495133446185)
    name=ctx.author.name
    lenmc =len(listmc)
    embed_list = discord.Embed(title = "Resultado da músicas da playlist",description = "PS: É necessario concluir a playlist antes de esculta-la",color = 0x00BFFF)
    embed_list.set_thumbnail(url="https://static.vecteezy.com/system/resources/previews/001/208/095/non_2x/music-player-png.png")
    embed_list.set_author(name=bot.user.name, icon_url=bot.user.avatar_url)
    embed_list.set_footer(text=f"Playlist consutada por {name} atrávez do comando !printl", icon_url=ctx.message.author.avatar_url)
    embed_list.add_field(name="Número de Músicas", value=lenmc)
    if lenmc == 0:
        embed_list.add_field(name="Playlist",value="None")
    else:
        embed_list.add_field(name="Playlist",value=listmc)

    await channel.send(f"{ctx.author.mention},",embed=embed_list)

@bot.command(name="resetl", help="Reseta a playlist. Não requer argumentos!")
async def resetl(ctx):
    channel = bot.get_channel(897530495133446185)
    lenmc = len(listmc)
    if lenmc == 0:
        await channel.send(f"{ctx.author.mention}, a lista já foi resetada!")
    else:
        listmc.clear()
        await channel.send(f"{ctx.author.mention}, a lista foi resetada!")

@bot.command(name="playlist", help="Inicia as música da playlist. Argumento: (number)!")
async def playlist(ctx,number):
    numbermc=(int)(number)
    channel = bot.get_channel(897530495133446185)
    channelm = bot.get_channel(897530822364631130)
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    lenmc = (int)(len(listmc))
    
    try:
        urls = listmc[numbermc-1]
        if voice.is_playing():
            voice.stop()
        if not voice is None and lenmc != 0 and numbermc > 0: 
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format': "bestaudio"}
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                info = ydl.extract_info(urls, download=False)
                url2 = info['formats'][0]['url']
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
            voice.play(source)
        else:
            if lenmc == 0:
                await channel.send(f"{ctx.author.mention}, a sua lista está vazia, use !list (url) para adicionar música a ela!")
            elif numbermc <= 0:
                await channel.send(f"{ctx.author.mention}, o número {numbermc} que digitou não está presente na lista!")         
    except:
        if voice is None: 
            await channel.send(f"{ctx.author.mention}, o bot não está no canal {channelm.mention}, use !join")
        elif numbermc > lenmc:
            await channel.send(f"{ctx.author.mention}, o número {numbermc} que digitou não está presente na lista!")       
        else:
            await channel.send(f"{ctx.author.mention}, o seu comando foi digitado incorreto, consute !help para ver os comando do bot!")



bot.run(open("ArquivosS/token.txt").readlines()[0].strip())