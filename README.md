V5.3 was released on 11/28/2021!
For more information, check [Updates.md](https://github.com/StethoSaysHello/KikBotnet/blob/main/Updates.md)


# About
This is a Kik botnet that uses [Tomer8007's Kik Bot API](https://github.com/tomer8007/kik-bot-api-unofficial) to spam users and groups.

I've hosted a copy on Replit for those of you who want to run it from your web browser, which you can find [here](https://replit.com/@StethoSaysHello/KikBotnet?v=1). _(Please note that this version is in 5.2 due to automatic setup, as 5.3 is designed to be run induvidually.)_

# Installation

Make sure you are using Python 3.6+, not python 2.7!

Use `git clone https://github.com/StethoSaysHello/KikBotnet`

Then just run [botnet.py](https://github.com/StethoSaysHello/KikBotnet/blob/main/botnet.py), it will install all of the needed dependancies for you. 

_Alternatively, you can just copy and paste the contents of [botnet.py](https://github.com/StethoSaysHello/KikBotnet/blob/main/botnet.py)._

# Usage

Once you run the script, the prompts should be self explanatory, but if you need an elaboration on each step [click here](https://pastebin.com/6kdHjVKk).

You cannot trigger the botnet from the terminal, you need to trigger the bots themselves via messages on Kik. To trigger an entire botnet, either add the whole botnet to a group and use the command, or send a mass message to each bot's PMs via modded Kik. Keep in mind that you need to make your own bot accounts, it will not make them for you!

- **"Spam [JID or Username] w/ [Message]"** -  Used to spam a user's PMs.

- **"Spam Gif [JID or Username] w/ [Query]"** - Used to spam a user's PMs with a gif.

- **"Poke [JID or username] w/ [Message]"** -  Used for forwarding a single message to a user.

- **"Poke Gif [JID or username] w/ [Query]"** - Used for forwarding a single gif to a user.

- **"Friend"** - Used to add the bot as a friend so that you can add it to groups.

- **"SendFriend [JID or Username]"** - Used to send a friend attribution request to a user.

- **"GroupSpam [Message]"** - Used to spam the group that this command is used in.

- **"GroupSpam Gif [Query]"** - Used to spam the group that this command is used in with gifs.

- **"Gif [Query]"** - Used to send a single gif in the group that this command is used in.

- **"Leave [GJID]"** - Used for making your bot(s) leave groups.

# Disclaimers

None of the code here is taken from other developers! It does not contain any malicious or hidden content, you are more than welcome to share and edit this code. 

Previous versions of this bot were obfuscated and required an access key, these limits no longer apply. 

There was previously a premium version with antipurge, addall, and promote/demote, but it is no longer being sold.
