# cosmog
![cosmog](https://raw.githubusercontent.com/ShadowOcto/cosmog/refs/heads/main/assets/cosmog_small.png)\
A nice little discord bot base made in python.\
*This project isn't a feature complete bot, just a simple base for one to be built on.*

## Bot Setup
- Install the required packages using `pip install -r requirements.txt`
- Add your bot token to `config.json` under "token" alongside any of the webhooks you wish to run information through.

## Adding Commands
To register a command, simply create a python file within the `/commands` folder with both 'DESCRIPTION' and 'ARGS' variables alongside the actual slash command function you wish to add. *(Use one of the two currently including commands as an example).*

## Adding Events
Adding events is just as simple as addings commands, create a python file for your desired event inside the `/events` folder and specify the event you wish to fire your code on alongside the @bot.event annotation. *(import 'bot' from `/objects/bot_instance`, once again: use the already including on_message event as an example.)*

---
*I don't care what you use this for, remove all credit if you so please, I was just making a discord bot for a project and decided to release the base behind it*

*✦ shadowocto.dev*