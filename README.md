# discord-ttt
A discord bot which mutes dead players in [Garry's Mod](https://store.steampowered.com/app/4000/Garrys_Mod/ "Garry's Mod"), meant for the Trouble In Terrorist Town gamemode.

## About
This bot uses the [PyGmod](https://github.com/javabird25/PyGmod "PyGmod") Library to hook into the **Serverside** of Garry's Mod, detecting when a player spawns, dies, enters spectator mode or leaves the game and mutes them accordingly.

Please keep in mind this currently only works on Windows dedicated or peer-to-peer servers, as [PyGmod](https://github.com/javabird25/PyGmod "PyGmod") currently only works on Windows. Should [PyGmod](https://github.com/javabird25/PyGmod "PyGmod") be released for Linux, the script should automatically work.

### Installation
To install for a **dedicated server** follow these instructions but with your server files directory, for a **peer-to-peer** server install PyGmod and the addon to your game directory.
1. Install [PyGmod](https://github.com/javabird25/PyGmod/releases "PyGmod"), instructions available onsite.
2. Make sure you have [Python 3.7+](https://www.python.org/ "Python 3.7+") installed.
3. Install the following dependencies on your system-wide python:
* discord.py
* aiohttp
4. Install pip in the embedded PyGmod Python:
* Download [get-pip.py]("https://bootstrap.pypa.io/get-pip.py")
* Open a powershell window for Windows or Terminal for Linux
* Execute the following `./PATHTOGMOD/python.exe get-pip.py`
5. Clone or download this repository, copying the **entire** folder into your [Garry's Mod](https://store.steampowered.com/app/4000/Garrys_Mod/ "Garry's Mod") addons folder.
6. Edit the config.py file located in the subdirectory python/discord-bot, add your [guild id](https://support.discord.com/hc/en-us/articles/206346498-Where-can-I-find-my-User-Server-Message-ID-), [channel id](https://www.swipetips.com/how-to-get-channel-id-in-discord/ "channel id") and [bot token](https://www.writebots.com/discord-bot-token/ "Bots token"). Make sure to add only the channel id number.

### Troubleshooting
* Make sure to copy the **entire folder** to your GMod addons folder, not simply the root of the folder.
* Double-check if any other services are running on port 8080
* Double check your discord token and channel id
* Contact me on Discord: Romedius#4907

### Credits
* javabird25 for PyGmod
* aiohttp Library
* requests Library
* Python itself
