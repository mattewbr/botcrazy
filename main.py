#SCRIPT BY MATTEW BR

import discord
import asyncio
import time
import datetime
import random



client = discord.Client()

players = {}
COR = 0xF7FE2E  #COLOCAR A COR, COLOCAR A COR DA OPÇOES DE MUSICA


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='BOT EM TEST', type=1,url='https://www.twitch.tv/m4ttewbr'))
    print('BOT FODA ATIVO !')






#BAN ,BANIR UM MENBRO DO SERVIDOR
@client.event
async def on_message(message):
    if message.content.startswith("!ban"):
        if not message.author.server_permissions.ban_members:
            return await client.send_message(message.channel,
                                             "**Você não tem permissão para executar esse comando bobinho(a)!**")
        try:
            user = message.mentions[0]
            await client.send_message(message.channel,
                                      "**O usuario(a) <@{}> foi banido com sucesso do servidor.**".format(user.id))
            await client.ban(user, delete_message_days=1)
        except:
            await client.send_message(message.channel, "**Você deve especificar um usuario para banir!**")
        finally:
            pass



  #MUSICA, TOCAR MUSICA EM UMA CALL
    if message.content.startswith('!entrar'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "O bot ja esta em um canal de voz")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('!sair'):
        try:
            mscleave = discord.Embed(
                title="\n",
                color=COR,
                description="Sai do canal de voz e a musica parou!"
            )
            voice_client = client.voice_client_in(message.server)
            await client.send_message(message.channel, embed=mscleave)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "O bot não esta em nenhum canal de voz.")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))

    if message.content.startswith('!play'):
        try:
            yt_url = message.content[6:]
            if client.is_voice_connected(message.server):
                try:
                    voice = client.voice_client_in(message.server)
                    players[message.server.id].stop()
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb.add_field(name="Enviado em:", value="`{}`".format(player.uploaded_date))
                    mscemb.add_field(name="Enviado por:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Duraçao:", value="`{}`".format(player.uploadeder))
                    mscemb.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb)
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))

            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = await voice.create_ytdl_player('ytsearch: {}'.format(yt_url))
                    players[message.server.id] = player
                    player.start()
                    mscemb2 = discord.Embed(
                        title="Música para tocar:",
                        color=COR
                    )
                    mscemb2.add_field(name="Nome:", value="`{}`".format(player.title))
                    mscemb2.add_field(name="Visualizações:", value="`{}`".format(player.views))
                    mscemb2.add_field(name="Enviado em:", value="`{}`".format(player.upload_date))
                    mscemb2.add_field(name="Enviado por:", value="`{}`".format(player.uploader))
                    mscemb2.add_field(name="Duraçao:", value="`{}`".format(player.duration))
                    mscemb2.add_field(name="Likes:", value="`{}`".format(player.likes))
                    mscemb2.add_field(name="Deslikes:", value="`{}`".format(player.dislikes))
                    await client.send_message(message.channel, embed=mscemb2)
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))

    if message.content.startswith('!pause'):
        try:
            mscpause = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscpause)
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    if message.content.startswith('!resume'):
        try:
            mscresume = discord.Embed(
                title="\n",
                color=COR,
                description="Musica pausada com sucesso!"
            )
            await client.send_message(message.channel, embed=mscresume)
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))




    #TESTAR SE O BOT TA ATIVO
    if message.content.lower().startswith('!ativo'):
        await client.send_message(message.channel, "Sim estou ativo xD !")
    if message.content.lower().startswith('oii'):
        await client.send_message(message.channel, "Ola ! como vai ? ")
    if message.content.lower().startswith('iae'):
        await client.send_message(message.channel, "iiae de boa ?")



#SORTEIO NO SERVIDOR
    if message.content.lower().startswith("!sorteio"):  # esse comandos sorteia um memebro
        if message.author.server_permissions.administrator:
            n = random.choice(list(message.server.members))
            n1 = '{}'.format(n.name)
            m1 = discord.utils.get(message.server.members, name="{}".format(n1))
            embed = discord.Embed(
                title="Sorteiar membro",
                colour=0xab00fd,
                description="Membro sorteado foi {}".format(m1.mention)
            )
            hh = await client.send_message(message.channel, "{}".format(m1.mention))
            await client.delete_message(hh)
            await client.send_message(message.channel, embed=embed)
        else:
            await client.send_message(
                "{} você não tem permissão de executar esse comando!".format(message.author.mention))





#USER INFO ,VER INFORMACOES DO USUARIO
    if message.content.lower().startswith('!userinfo'):
        try:
            user = message.mentions[0]
            server = message.server
            embedinfo = discord.Embed(title='Informações do usuário', color=0x03c3f5, )
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='Usuário:', value=user.name)
            embedinfo.add_field(name='Apelido', value=user.nick)
            embedinfo.add_field(name='🆔 ID:', value=user.id)
            embedinfo.add_field(name='📅 Entrou em:', value=user.joined_at.strftime("%d %b %Y às %H:%M"))
            embedinfo.add_field(name='📅 Server criado em:', value=server.created_at.strftime("%d %b %Y %H:%M"))
            embedinfo.add_field(name='Jogando:', value=user.game)
            embedinfo.add_field(name="Status:", value=user.status)
            embedinfo.add_field(name='Cargos:', value=([role.name for role in user.roles if role.name != "@everyone"]))
            await client.send_message(message.channel, embed=embedinfo)
        except ImportError:
            await client.send_message(message.channel, 'Buguei!')
        except:
            await client.send_message(message.channel, '❎ | Mencione um usuário válido!')
        finally:
            pass



#MUTE,SILENÇIAR UM MEMBRO
    if message.content.lower().startswith('!mute'):
        try:
            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel, 'âš ï¸PermissÃµes insuficientes')
            author = message.author.mention
            user = message.mentions[0]
            motivo = message.content[29:]
            cargo = discord.utils.get(message.author.server.roles,
                                      name='MUTADO') #COLOCAR O CARGO DE MUTE
            await client.add_roles(user, cargo)
            await client.send_message(message.channel,
                                      'O usuario: {} foi mutado pelo Administrador {} pelo motivo: {}.'.format(
                                          user.mention, author, motivo))
        except:
            await client.send_message(message.channel, " Vc nao selecionou ninguem para mutar.")


#UNMUTE, TIRAR MUTE DE UM MEMBRO
    if message.content.lower().startswith('!unmute'):
        try:
            if not message.author.server_permissions.administrator:
                return await client.send_message(message.channel, 'âš ï¸PermissÃµes insuficientes')
            author = message.author.mention
            user = message.mentions[0]
            motivo = message.content[29:]
            cargo = discord.utils.get(message.author.server.roles,
                                      name='MUTADO')
            await client.remove_roles(user, cargo)
            await client.send_message(message.channel,
                                      'O Usuario: {} foi desmutado pelo Administrador: {} pelo motivo: {}.'.format(
                                          user.mention, author, motivo))
        except:
            await client.send_message(message.channel, "Vc nao selecionou ninguem para desmutar.")








#APAGAR MENSAGEM NO CHAT DO SERVIDOR
    prefixo = "!"
    if message.content.lower().startswith(prefixo + "limpar"):
        try:
            a = len(prefixo) + 7
            if int(message.content[a:]) < 500:
                qntd = int(message.content[a:]) + 1
                await client.purge_from(message.channel, limit=qntd)
                cleared = await client.send_message(message.channel,
                                                    f'{qntd} mensagens foram apagadas por {message.author.mention}!')
                await asyncio.sleep(5)
                await client.delete_message(cleared)
            else:
                await client.send_message(message.channel, 'Você nao pode apagar mais de 500 mensagens de uma so vez!')
        except ValueError:
            await client.send_message(message.channel, 'Digite um valor para apagar')
        except discord.Forbidden:
            await client.send_message(message.channel, 'Não tenho permissões para apagar mensagens!')



#MUDAR APELIDO
    if message.content.lower().startswith('!mudarapelido'):
        if not message.author.server_permissions.administrator:
            await client.send_message(message.channel, 'Você não tem permissão.')
        try:
            user = message.mentions[0]
            msg = str(message.content[12:]).replace('<', '').replace('>', '').replace('@', '').replace(user.id, '')
            await client.change_nickname(user, msg)
            await client.send_message(message.channel, 'Apelido trocado com sucesso !')
        except:
            await client.send_message(message.channel, 'Você precisa especificar um usuário.')



#AVATAR,PEGAR AVATAR DE UM MEMBRO
    prefixo = "!"
    if message.content.startswith(prefixo + "avatar"):
        xtx = message.content.split(' ')
        if len(xtx) == 1:
            useravatar = message.author
            avatar = discord.Embed(
                title="Avatar de: {}".format(useravatar.name),
                color=0x000000, #COLOCAR A COR
                description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
            )

            avatar.set_image(url=useravatar.avatar_url)
            avatar.set_footer(text="Pedido por {}#{}".format(useravatar.name, useravatar.discriminator))
            await client.send_message(message.channel, embed=avatar)
        else:
            try:
                useravatar = message.mentions[0]
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=0x000000, #COLOCAR A COR
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)

            except IndexError:
                a = len(prefixo) + 7
                uid = message.content[a:]
                useravatar = message.server.get_member(uid)
                avatar = discord.Embed(
                    title="Avatar de: {}".format(useravatar.name),
                    color=0x000000, #COLOCAR A COR
                    description="[Clique aqui](" + useravatar.avatar_url + ") para baixar a imagem"
                )

                avatar.set_image(url=useravatar.avatar_url)
                avatar.set_footer(text="Pedido por {}".format(message.author))
                await client.send_message(message.channel, embed=avatar)


#EMOJIS ,VER TODOS EMOJIS DO SERVIDOR
    if message.content.lower().startswith("!emojis"):
        if len(message.server.emojis) == 0:
            return await client.send_message(message.channel,
                                             message.author.mention + ", **esse servidor não possui nenhum emoji!**")

        emojis = ""
        mostrando = 0
        for emoji in message.server.emojis:
            if len(str(emoji)) + 1 + len(emojis) <= 1024:
                emojis += str(emoji) + " "
                mostrando += 1

        em = discord.Embed(colour=0x00FFFF, description="**Mostrando `{}` de `{}`**\n\n".format(mostrando, len(
            message.server.emojis)) + emojis)
        em.set_author(name=message.server.name, icon_url=message.server.icon_url)
        em.set_footer(text="Requisitado por " + str(message.author), icon_url=message.author.avatar_url)
        await client.send_message(message.channel, embed=em)




    #PING, VER O PING DO BOT
    if message.content.lower().startswith('!ping'):
        channel = message.channel
        t1 = time.perf_counter()
        await client.send_typing(channel)
        t2 = time.perf_counter()
        ping_embed = discord.Embed(title="🏓 Pong!", color=0x000000, description='Meu tempo de resposta é `{}ms`!'.format(round((t2 - t1) * 1000)))
        await client.send_message(message.channel, f"{message.author.mention}", embed=ping_embed)



#HORA LOCAL ,SABER AS HORAS
    if message.content.startswith('!hora'):
        # importe o time e datetime
        horario = datetime.datetime.now().strftime("%H:%M:%S")
        await client.send_message(message.channel,
                                  "**⌚ Hora local atual {} **{}".format(message.server.region, horario))




    #SERVE INFO, VER INFORMAÇOES DO SERVIDOR

    if message.content.startswith('!serverinfo'):
        user = message.author.name

        horario = datetime.datetime.now().strftime("%H:%M:%S")

        serverinfo_embed = discord.Embed(title="\n", description="Abaixo está as informaçoes principais do servidor!",
                                         color=0x000000,)
        serverinfo_embed.set_thumbnail(url=message.server.icon_url)
        serverinfo_embed.set_footer(text="{} • {}".format(user, horario))
        serverinfo_embed.add_field(name="Nome:", value=message.server.name, inline=True)
        serverinfo_embed.add_field(name="Dono:", value=message.server.owner.mention)
        serverinfo_embed.add_field(name="ID:", value=message.server.id, inline=True)
        serverinfo_embed.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        serverinfo_embed.add_field(name="Canais de texto:", value=len(
            [message.channel.mention for channel in message.server.channels if
             channel.type == discord.ChannelType.text]), inline=True)
        serverinfo_embed.add_field(name="Canais de voz:", value=len(
            [message.channel.mention for channel in message.server.channels if
             channel.type == discord.ChannelType.voice]), inline=True)
        serverinfo_embed.add_field(name="Membros:", value=len(message.server.members), inline=True)
        serverinfo_embed.add_field(name="Bots:",
                                   value=len([user.mention for user in message.server.members if user.bot]),
                                   inline=True)
        serverinfo_embed.add_field(name="Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"),
                                   inline=True)
        serverinfo_embed.add_field(name="Região:", value=str(message.server.region).title(), inline=True)
        await client.send_message(message.channel, embed=serverinfo_embed)




#MEMBROS NO TOPICO DO CANAL
@client.event
async def on_member_join(member):
    canal = client.get_channel("480357580607062052")# substitua pelo id do canal que voce queria que apareça o contador
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
# ele ira por o emoji dos numeros, caso nao queria com emoji basta retirar todos os replaces
@client.event
async def on_member_remove(member):
    canal = client.get_channel("480357580607062052")# substitua pelo id do canal que voce queria que apareça o contador
    await client.edit_channel(canal, topic="Membros: "+str(member.server.member_count).replace('1', '1⃣').replace('2', '2⃣').replace('3', '3⃣').replace('4', '4⃣').replace('5', '5⃣').replace('6', '6⃣').replace('7', '7⃣').replace('8', '8⃣').replace('9', '9⃣').replace('0', '0⃣'))
# ele ira por o emoji dos numeros, caso nao queria com emoji basta retirar todos os replaces
# obs:isso so funciona com canais de texto(obvio pq canal de voz nao tem topico



#MENSAGEM DE BEM VINDO
@client.event
async def on_member_join(member):
  canal = client.get_channel("480357580607062052")
  msg = "{} Bem Vindo ao servidor de teste !".format(member.mention)
  await client.send_message(canal, msg) #substitua canal por member para enviar a msg no DM do membro
  msg = "{} Bem Vindo no privado !".format(member.mention) #mensagem de bem vindo no privado
  await client.send_message(member, msg)













client.run('NDgwMzU2OTcyMTcyOTM1MTY5.DlmnAQ.x8fEH9_E2NWzR82VTPrALgXp_uY')


