from pygmod.gmodapi import *
import pickle, asyncio, os, sys


# dependency check
try:
    import pip
except ModuleNotFoundError:
    print("Please install pip! Run get-pip.py using the embedded interpreter!")
    sys.exit("Pip not installed!")

try:
    import discord
except ModuleNotFoundError:
    try:
        import pip
        pip.main(["install", "discord.py"])
    except:
        sys.exit("Caught error while trying to install discord.py! Check pip and internet connection!")
import discord

class MyClient(discord.Client):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        hook.Add('PlayerInitialSpawn', 'onPlayerInitialSpawn', onPlayerInitialSpawn)
    def onPlayerInitialSpawn(ply, args):
        new_player._.ChatPrint("Discord TTT Bot is running! Join the ttt voice channel to learn more!")
        new_player._.ChatPrint("Welcome to the server, " + new_player._.Nick() + "!")
