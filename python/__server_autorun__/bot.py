# modules
import asyncio, pickle, config
from aiohttp import web
from discord.ext import commands

# values
channelid = 0 # integer value

# check ids.p file
try:
    open("ids.p", "rb")
except EOFError:
    os.remove("ids.p")
try:
    open("ids.p", "rb")
except FileNotFoundError:
    ids = {"Placeholder": "Placeholder"}
    pickle.dump(ids, open("ids.p", "wb"))

# asyncio
loop = asyncio.get_event_loop()

# import users
ids = pickle.load(open("ids.p", "rb"))
muted = []

# aiohttp
routes = web.RouteTableDef()
app = web.Application()
runner = web.AppRunner(app)

# the bot
bot = commands.Bot(command_prefix="!")

@bot.command(pass_context=True)
async def ping(ctx, arg1):
    await ctx.send(str(arg1))

@bot.command(pass_context=True)
async def register(ctx, arg1):
    await ctx.send("Please double check to make sure this is your SteamID!")
    ids[ctx.author.id] = arg1
    pickle.dump(ids, open("ids.p", "wb"))

@bot.event
async def on_voice_state_update(member, before, after):
    print("Voice update!")
    for x in muted:
        if x == member.id:
            if after.channel.id == channelid:
                await member.edit(mute = True, reason = None)
            else:
                await member.edit(mute = False, reason = None)
        else:
            await member.edit(mute = False, reason = None)

@routes.get('/ondeath')
async def ondeath(request):
    await request.json
    player = json.loads(json.dumps(request.json))["Player"]
    member = discord.Guild.get_member(ids[player])
    await member.edit(mute = True, reason = None)
    muted.append(ids[player])

@routes.get('/onspawn')
async def onspawn(request):
    await request.json
    player = json.loads(json.dumps(request.json))["Player"]
    member = discord.Guild.get_member(ids[player])
    await member.edit(mute = False, reason = None)
    muted.remove(ids[player])

@routes.get('/onspawnasspectator')
async def onspectatorspawn(request):
    await request.json
    player = json.loads(json.dumps(request.json))["Player"]
    member = discord.Guild.get_member(ids[player])
    await member.edit(mute = True, reason = None)
    muted.append(ids[player])

@routes.get('/ondisconnect')
async def ondisconnect(request):
    await request.json
    player = json.loads(json.dumps(request.json))["Player"]
    member = discord.Guild.get_member(ids[player])
    await member.edit(mute = False, reason = None)
    muted.remove(ids[player])

@routes.get('/ping')
async def pong(request):
    return web.Response(text="Pong!")

asyncio.ensure_future(bot.start(config.token), loop=loop)

# aiohttp
if __name__ == '__main__':
    app.add_routes(routes)
    web.run_app(app)

#runner = web.AppRunner(app)
#runner.setup()
#site = web.TCPSite(runner, 'localhost', 8080)
#site.start()

#handler = app.make_handler()
#server = loop.create_server(handler, host='127.0.0.1', port=8080)


#loop = asyncio.get_event_loop()
#loop.create_task(web.run_app(app))
#loop.create_task(bot.run("NzEwMTMxNjMyNTM0NzE2NDU2.XtBCcQ.QO1kxAn1mERaEjN-gGtKlmT1Pcg"))
#loop.run_forever()

#if __name__ == '__main__':
#    app.add_routes(routes)
#    webserver = Process(target=web.run_app(app)).start()
#    webserver.join()
#    discordbot = Process(target=bot.run("NzEwMTMxNjMyNTM0NzE2NDU2.XtBCcQ.QO1kxAn1mERaEjN-gGtKlmT1Pcg")).start()
#    discordbot.join()
