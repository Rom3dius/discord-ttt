from pygmod.gmodapi import *
import pickle, os, sys


# dependency check
try:
    import pip
except ModuleNotFoundError:
    print("Please install pip! Run get-pip.py using the embedded interpreter!")
    sys.exit("Pip not installed!")

try:
    import requests
except ModuleNotFoundError:
    try:
        import pip
        pip.main(["install", "requests"])
    except:
        sys.exit("Caught error while trying to install requests! Check pip and internet connection!")
import requests

os.system("bot.py")

# initializing hooks
def onPlayerInitialSpawn(ply, args):
    ply._.ChatPrint("Welcome to the server, " + ply._.Nick() + "!")
    ply._.ChatPrint("Discord TTT Bot is running! Join the voice channel to learn more!")

hook.Add('PlayerInitialSpawn', 'onPlayerInitialSpawn', onPlayerInitialSpawn)

def onPlayerDeath(victim, inflictor, attacker):
    death = victim._.SteamID()
    print(death + " has died!")
    data = {"Player": death}
    request = requests.post("http://127.0.0.1:8080/ondeath", data = data)

hook.Add('PlayerDeath', 'onPlayerDeath', onPlayerDeath)

def onPlayerSpawn(ply, args):
    spawn = ply._.SteamID()
    print(spawn + " has spawned!")
    data = {"Player": spawn}
    request = requests.post("http://127.0.0.1:8080/onspawn", data = data)

hook.Add('PlayerSpawn', 'onPlayerSpawn', onPlayerSpawn)

def onPlayerSpawnAsSpectator(ply, args):
    spawn = ply._.SteamID()
    print(spawn + " has started spectating!")
    data = {"Player": spawn}
    request = requests.post("http://127.0.0.1:8080/onspawnasspectator", data = data)

hook.Add('PlayerSpawnAsSpectator', 'onPlayerSpawnAsSpectator', onPlayerSpawnAsSpectator)

def onPlayerDisconnect(ply, args):
    disconnect = ply._.SteamID()
    print(disconnect + " has disconnected!")
    data = {"Player": disconnect}
    request = requests.post("http://127.0.0.1:8080/ondisconnect", data = data)

hook.Add('PlayerDisconnected', 'onPlayerDisconnect', onPlayerDisconnect)
