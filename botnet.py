'''

You may notice there are a TON of #comments in here, this is to make it as easy as possible for you to understand how this code functions.
Too many comments probably. But feedback on the beta was that there wasn't enough comments, and there were already a lot then, soooo...
ANYWAYS, this code is FREE, so if someone sold this to you, I'm sorry to say that you got scammed. Poor you.
Nothing here was skidded, everything here was made by yours truly, aside from Tomer8007's api, obviously.
You're welcome to modify this as much as you'd like! Have fun <3
- Stetho

P.S:
I don't mind people "skidding" this at all, that's what I made it open source for.
So long as people aren't impersonating me or claiming they made the original copy, it's totally fine for people to modify and repost this script.
Exploring and playing with existing code is how a lot of new developers learn, so quit harrassing people for it!


'''
import sys
import os
import time
import subprocess
import contextlib
#from keepalive import keep_alive
from urllib.request import urlopen
check_for_startup = os.path.exists("startup.py")
if check_for_startup == False:
  clear = open("startup.py", "w+")
  clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = False\n\npreset_username = \"\"\n\npreset_password = \"\"\n\npreset_num_of_bots = 0")
  clear.close()
from startup import use_preset, preset_username, preset_password, preset_num_of_bots

global ominous_dots, bcolors #This allows us to use the bcolors class and ominous_dots function later in the script.

class bcolors:  # This is for adding colors to text in the terminal.
    OKBLUE = '\033[94m'  # This is blue
    FAIL = '\033[91m'  # This is red
    OKGREEN = '\033[92m'  # This is green
    ENDC = '\033[0m'  # This is to stop using color.

def ominous_dots(string): #This function is for making a "..." with a delay between each period at the end of a print statement.
    sys.stdout.write(string) #This prints the string that was given to the function
    dots = bcolors.OKGREEN + ("...") + bcolors.ENDC #This makes the periods green
    for dot in dots: #This loops through the 3 periods
        sys.stdout.write(dot) #This prints a period
        sys.stdout.flush() #This makes sure it doesn't make a new line like print() would
        time.sleep(0.3) #This waits 1/3 of a sec
    time.sleep(0.1) #This waits another split second so that the total wait time is exactly 1 second

ominous_dots(bcolors.OKGREEN + ("Booting up") + bcolors.ENDC) # This lets the user know the bot is booting up.

with contextlib.redirect_stdout(None): #This hides the output from installation to avoid spam
    automatic_setup = os.path.isdir("kik-bot-api-unofficial")  # This checks if the user has already installed the Kik Bot API
    if automatic_setup == False:  # This is triggered if they have not
        os.system('git clone -b new https://github.com/StethoSaysHello/kik-bot-api-unofficial')  # This installs the stuff from stetho's fork of Tomer8007's API. Just has some redundant stuff quoted out, keys added
    os.system('pip3 install ./kik-bot-api-unofficial')

try:
  version_page = "https://UpdateCheck.stethosayshello.repl.co" #This grabs the page where the current version is
  page = urlopen(version_page) #This opens the page
  raw_version = page.read() #This reads the page
  version = raw_version.decode("utf-8") #This decodes the page and gives us a string
  '''
  The 5 lines below this comment is a killswitch.
  You are welcome to remove it, it will not effect the botnet if you do, but it is there for YOUR safety!
  It is only used if a serious, potentially harmful bug or exploit in the botnet's code is discovered.
  The killswitch does not cause any kind of harm, it simply asks you to update and deletes the bot code.
  '''
  if version == "killswitch": #This checks if the killswitch has been activated
      print(bcolors.FAIL + ("This version of the botnet has been killswitched!\nThis is only used if a serious, potentially harmful bug or exploit in the botnet's code is discovered.\nPlease visit https://github.com/StethoSaysHello/KikBotnet to check for updates! If you need help, email StethoSpasm@Gmail.com\n\nFor your saftey, I am now deleting this script.\nDon't worry, this will not cause any harm to your local machine!") + bcolors.ENDC) #This explains the killswitch to a user
      path = os.getcwd() #This finds the path the script is running on
      os.remove(path + '\%s' % sys.argv[0]) #This removes the script
      exit() #This stops the script if its still somehow active
  if version == "v5.3": #This checks if this script is up to date
    pass
  else: #This is activated if the user is not up to date
      print(bcolors.FAIL + ("There is a new version of the botnet available! Please install the update, it can be found at https://github.com/StethoSaysHello/KikBotnet") + bcolors.ENDC)  # This asks the user to update
      input("Press enter to continue if you still want to use this outdated version! (Weirdo! lol)")
except:
  print(bcolors.FAIL + "Oh no! There was a problem checking for updates... This is probably from hosting issues. If you need to check for updates in the meantime, please visit Github.com/StethoSaysHello/KikBotnet\n(You can still use the botnet!)" + bcolors.ENDC)
  input(bcolors.OKBLUE + "Press enter to continue: " + bcolors.ENDC)

def install(package):  # This is a function to make the installs a little more efficient. I could have just used os.system again, but...
    subprocess.check_call([sys.executable, "-m", "pip", "install", package]) #This installs the package

try: #This tries to import
    import emoji
except ModuleNotFoundError: #This is triggered if the import fails
    print(bcolors.OKGREEN + ("\nOne moment while I install the emoji module.") + bcolors.ENDC) #This lets the user know it will install the module
    install('emoji')  # This is used to send/recieve, and encode/decode emojis.
    import emoji
try: #This tries to import
    import colorama
except ModuleNotFoundError: #This is triggered if the import fails
    print(bcolors.OKGREEN + ("\nOne moment while I install the colorama module.") + bcolors.ENDC) #This lets the user know it will install the module
    install('colorama')  # This is used to make pretty colors in the terminal. oooooo
    import colorama
try: #This tries to import
    import kik_unofficial
except ModuleNotFoundError: #This is triggered if the import fails
    print(bcolors.OKGREEN + ("\nOne moment while I install the kik_unofficial module.") + bcolors.ENDC) #This lets the user know it will install the module
    install('kik_unofficial')  # This is pretty obvious
    import kik_unofficial

import kik_unofficial.datatypes.xmpp.chatting as chatting
from kik_unofficial.client import KikClient
from kik_unofficial.callbacks import KikClientCallback
from kik_unofficial.datatypes.xmpp.errors import LoginError
from kik_unofficial.datatypes.xmpp.roster import FetchRosterResponse
from kik_unofficial.datatypes.xmpp.login import LoginResponse, ConnectionFailedResponse

clear = open("kik-debug.log", "w+")  #This clears out debug logs if there are any.
clear.close()  #This closes the debug log, always a good practice.

global username_thing, spam, debug_jid, thing, attempt_number, given_pass, setup_preset #This declares these variables as global to be used everywhere because I'm lazy
attempt_number = 0 #This helps to check if it is the first set of logins or not for retrying closed connections.
print("For help, check out the README! https://github.com/StethoSaysHello/KikBotnet\n") #This is a lil disclaimer on bootup.
print(bcolors.OKGREEN + ("╭╮╭━╮╭╮    ╭━━╮   ╭╮      ╭╮\n┃┃┃╭╯┃┃    ┃╭╮┃  ╭╯╰╮    ╭╯╰╮\n┃╰╯╯╭┫┃╭╮  ┃╰╯╰┳━┻╮╭╋━╮╭━┻╮╭╯\n┃╭╮┃┣┫╰╯╯  ┃╭━╮┃╭╮┃┃┃╭╮┫┃━┫┃\n┃┃┃╰┫┃╭╮╮  ┃╰━╯┃╰╯┃╰┫┃┃┃┃━┫╰╮\n╰╯╰━┻┻╯╰╯  ╰━━━┻━━┻━┻╯╰┻━━┻━╯\n##### Created by Stetho #####") + bcolors.ENDC) #This is some neat text art on bootup. ooo greeeen
spam = "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv" #This is just a random variable to be used later in the "spam" command.
debug_jid = "8675309debug_y8f@talk.kik.com" #This is where activity info is sent to. Has to be a JID, not a GJID.

print(bcolors.OKGREEN + "\nLet's get started!" + bcolors.ENDC)

setup_preset = False
use_creds = False
credentials = {}
def get_preset():
    global setup_preset, use_creds
    ask_preset = input(bcolors.OKGREEN + ("Would you like to setup automatic startup?\n[1] Yes, I would like to set it up.\n[2] No, I would like to startup manually.\n[3] I would like to use credentials.txt\n> ") + bcolors.ENDC)
    if str(ask_preset) == "1":
        print(bcolors.OKGREEN + ("Great! I'll setup automatic startup for you.\nJust input your details like normal and I'll do the rest!") + bcolors.ENDC)
        setup_preset = True
    elif str(ask_preset) == "2":
        ominous_dots(bcolors.OKGREEN + ("Okay, continuing without automatic startup") + bcolors.ENDC)
    elif str(ask_preset) == "3":
        use_creds = True
        ominous_dots(bcolors.OKGREEN + ("Okay, using credentials.txt") + bcolors.ENDC)
    else:
        print(bcolors.FAIL + "Invalid input! Please only use the number \"1\" or \"2\" (without quotations)\nExiting..." + bcolors.ENDC)
        exit()

if use_preset == False:
    get_preset()

if use_preset == True:
    ask_preset = input(bcolors.OKGREEN + ("\nI see you have startup.py configured.\nWould you like to use automatic startup?\n[1] Yes, I want to use automatic startup.\n[2] No, I want to startup manually.\n[3] No, I want to change automatic startup settings.\n> ") + bcolors.ENDC)
    if str(ask_preset) == "1":
        ominous_dots(bcolors.OKGREEN + ("\nOkay! Using automatic startup") + bcolors.ENDC)
        print("\n")
    elif str(ask_preset) == "2":
        ominous_dots(bcolors.OKGREEN + ("Okay, continuing without automatic startup") + bcolors.ENDC)
        use_preset = False
    elif str(ask_preset) == "3":
        ask_change = input(bcolors.OKGREEN + ("Okay! Let's change automatic startup.\n[1] Change credentials\n[2] Reset to default settings\n") + bcolors.ENDC)
        if str(ask_change) == "1":
            print(bcolors.OKGREEN + ("Great! I'll setup automatic startup for you.\nJust input your details like normal and I'll do the rest!") + bcolors.ENDC)
            setup_preset = True
        elif str(ask_change) == "2":
            clear = open("startup.py", "w+")
            clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = False\n\npreset_username = \"\"\n\npreset_password = \"\"\n\npreset_num_of_bots = 0")
            clear.close()
            input(bcolors.OKGREEN + "Okay, I've reset your settings to the default. Press enter to continue with manual startup." + bcolors.ENDC)
            use_preset = False
        else:
            print(bcolors.FAIL + "Invalid input! Please only use the number \"1\" or \"2\" (without quotations)\nExiting..." + bcolors.ENDC)
            exit()
    else:
        print(bcolors.FAIL + "Invalid input! Please only use the number \"1\", \"2\" or \"3\" (without quotations)\nExiting..." + bcolors.ENDC)
        exit()


def get_prefix(): #This function asks for the bot prefix.
    username_thing = input(bcolors.OKGREEN + ("\n\nWhat is the prefix of your bots usernames?: ") + bcolors.ENDC) #This asks for the bot username prefix in the terminal.
    return username_thing

if use_preset == True:
    username_thing = preset_username
elif use_creds == True:
    with open("credentials.txt", "r") as a_file:
        for line in a_file:
            stripped_line = line.strip()
            cred = stripped_line.split(":")
            credentials[cred[0]] = cred[1]
    a_file.close()
else:
    username_thing = get_prefix() #This triggers the function that aske for the bot prefix
    if len(username_thing) == 0: #This checks for blank prefixes, and retries get_prefix if there are any.
        print(bcolors.FAIL + ("Uh-oh, it looks like you didn't provide any input! Let's try that again.") + bcolors.ENDC)
        username_thing = get_prefix()
    if " " in username_thing: #This checks for spaces in the prefix, and retries get_prefix if there are any.
        print(bcolors.FAIL + ("Uh-oh! There is a space in the username prefix you provided. Let's try that again.") + bcolors.ENDC)
        username_thing = get_prefix()
    print(bcolors.OKGREEN + ("\nOkay, I will be signing into your botnet as \"" + username_thing + "1\", \"" + username_thing + "2\", and so on.\nIf this is incorrect, please restart this session.") + bcolors.ENDC) #This explains how the bots will sign in.

def get_bot_quantity(): #This function asks the user how many bots they wanna use.
    try:
        thing = int(input(bcolors.OKGREEN + ("\nHow many bots do you have?: ") + bcolors.ENDC))
    except ValueError: #This is triggered when the input is not a number.
        print(bcolors.FAIL + ("That's not a number, lol. Lets try that again.") + bcolors.ENDC)
        thing = "NULL" #Just put a random string here to catch ValueError, could have put whatever.
    return thing

if use_preset == True:
    thing = preset_num_of_bots
elif use_creds == True:
    thing = len(credentials)
else:
    thing = get_bot_quantity() #This triggers the above function to ask the user how many bots they wanna use,
    if thing == "NULL": #This retries get_bot_quantity when the input is not a number.
        thing = get_bot_quantity()
    else: #Else statement used because im mixing str/int in 'thing'
        if thing <= 0: #This retries get_bot_quantity when the input is equal to or lower than 0.
            print(bcolors.FAIL + ("You must use a number greater than or equal to 1. Let's try that again.") + bcolors.ENDC)
            thing = get_bot_quantity()

if use_preset == True:
    given_pass = preset_password
    bootup_message = "I am logging in with the preset options: \nUsername prefix - " + str(preset_username) + "\nPassword - " + str(preset_password) + "\nNumber of bots - " + str(preset_num_of_bots)
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
elif use_creds == True:
    bootup_message = "I am logging in with the credentials.txt"
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
else:
    given_pass = input(bcolors.OKGREEN + ("\n" + str(thing) + " bots, got it! What is the password for your bots?: ") + bcolors.ENDC) #This asks for the bot's password, it doesn't need error handling.

if setup_preset == True:
    clear = open("startup.py", "w+")
    clear.write("\'\'\'\nThis is where you add details to speed up the bootup process.\n\'\'\'\nuse_preset = True\n\npreset_username = \"" + str(username_thing) + "\"\n\npreset_password = \"" + str(given_pass) + "\"\n\npreset_num_of_bots = " + str(thing))
    clear.close()
    bootup_message = "I've added the following presets to setup.py: \n\nUsername prefix - " + str(username_thing) + "\nPassword - " + str(given_pass) + "\nNumber of bots - " + str(thing) + "\n"
    print(bcolors.OKGREEN + bootup_message + bcolors.ENDC)
    time.sleep(1)
    input(bcolors.OKGREEN + "Press enter to begin logging in: " + bcolors.ENDC)

time.sleep(1)
print(bcolors.FAIL + emoji.emojize(":warning: RED messages are important and require your attention, keep an eye out for them!") + bcolors.ENDC) #This is an example red text, ooooo
time.sleep(3)
print(bcolors.OKGREEN + emoji.emojize("I am now attempting to login to the botnet.") + bcolors.ENDC)

def login(give_a_username, give_a_password, thing): #This is a function for logging in, it asks for user/pass and # of bots. Its a function so that it can be called on to retry later if there are any closed connections.
    stetho_string = give_a_username #These arent really relevant but I didnt feel like changing variable names when I added retry on connection error, sooo....
    given_pass = give_a_password
    username = sys.argv[1] if len(sys.argv) > 1 else stetho_string #This is where the username goes
    password = sys.argv[2] if len(sys.argv) > 2 else given_pass #This is where the password goes

    def main(): #This function is used to execute the login process only if the file was run directly, and not imported.
        SpamBotnet()

    class SpamBotnet(KikClientCallback):
        def __init__(self): #Constructor for the SpamBotnet class above
            self.client = KikClient(self, username, password) #This is where the previously stored user/pass goes to login

        global result
        result = None #This makes the login scripts wait until the login succeeds or fails before trying again

        def on_login_ended(self, response: LoginResponse): #This is triggered when the bot is done logging in
            ominous_dots(bcolors.OKGREEN + ("Logging in as @" + str(username)) + bcolors.ENDC) #This lets you know your bot logged in in the terminal. It says the first/last name and username.

        def on_authenticated(self): #This is triggered when the bot is authenticated (yayyyy no closed connection)
            print(bcolors.OKGREEN + (" Successfully logged in!"))
            global result
            result = True #This lets the login stanzas know that the login was authenticated and it can continue with the next login
            self.client.request_roster()  # This requests the roster, which is later used in on_roster_recieved

        def on_chat_message_received(self, chat_message: chatting.IncomingChatMessage): #This is triggered when a PM is recieved
            JID = chat_message.from_jid  #This grabs the sender's JID because I dont feel like typing that a million times
            mssg = emoji.demojize(chat_message.body.lower()) #This grabs the message, encodes emojis, and makes it lowercase.
            if mssg == "ping": #command to check if bot is online
                self.client.send_chat_message(JID, "pong") #Replies "pong". Pretty simple
            elif mssg == "friend": #command to add the bot as a friend
                self.client.add_friend(JID) #This is a friend attribution request
                self.client.send_chat_message(JID, "You can now add me to groups.")
            elif mssg.startswith("gif"):
                gif_query = mssg.replace("gif ", "", 1)
                self.client.send_chat_message(JID, "Searching for a gif with the query \"" + str(gif_query) + "\"...")
                try: #This attempts the gif query once first to check if its valid
                    self.client.send_gif_image(JID, gif_query) #This tries to send a gif with the query
                except:
                    self.client.send_chat_message(JID, "I couldn't find a gif for the query" + gif_query + "\"!")
            elif mssg == "commands": #command for listing the commands.
                self.client.send_chat_message(JID, "To spam a user's PMs, use \"spam [JID or Username] w/ [Message]\", this command works both in groups and PMs.\n\nTo spam a group, say \"friend\" in PMs to add me then add me to the group you wish to spam and say \"groupspam [message]\".\n\n Keep in mind that once you start spam, it will not stop until you restart the bot.")
            elif mssg.startswith("spam"): #Command for spamming a user.
                if mssg == "spam": #Elaborates on how to use spam if the message is just "spam"
                    self.client.send_chat_message(JID, "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                    if " w/ " in mssg: #This checks if "w/" was in the string and continues if so
                        if mssg.startswith("spam gif"):
                            failed = False
                            remove_spam = mssg.replace("spam gif ", "")  #This takes the first part of the message off to isolate the jid/username and query
                            split_string = remove_spam.split(" w/ ", 1)  #This splits the message into the JID/username and message
                            jid_to_spam = split_string[0]  #This isolates the JID we got in split_string
                            '''
                            The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                            '''
                            if "@talk.kik.com" in jid_to_spam: #Temporary patch
                              jid_to_spam = jid_to_spam[:-17] #Temporary patch
                            gif_query = split_string[1] #This isolates the query we got in split_string
                            try: #This attempts the gif query once first to check if its valid
                                self.client.send_gif_image(jid_to_spam, gif_query) #This tries to send a gif with the query
                            except: #This is triggered if it fails
                                failed = True #I could have just used "raise someerror" and except, but I was tired when I wrote this... I'ma just leave it. Don't @ me nobody really reads my code anyways. Except you... Hi nerd.
                            if failed == True: #This is triggered when gif grabbing fails
                                self.client.send_chat_message(JID, "I couldn't find a gif for the query" + gif_query + "\"!") #This lets the user know it failed
                            else: #This is triggered if the gif query does not fail
                                self.client.send_chat_message(JID, "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)") #This lets the user on kik know it is spamming gifs
                                print("I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)") #This displays in the terminal that gif spam was triggered
                                while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv": #This triggers a while loop with the random string we made global earlier
                                    self.client.send_gif_image(jid_to_spam, gif_query) #This sends the gif
                                    time.sleep(0.3)  # This is the wait between each message. Never change it to 0, IP bans suck.
                        else:
                            remove_spam = mssg.replace("spam ", "") #This takes the first part of the message off to isolate the jid/username and message
                            split_string = remove_spam.split(" w/ ", 1) #This splits the message into the JID/username and message
                            jid_to_spam = split_string[0] #This isolates the JID
                            '''
                            The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                            '''
                            if "@talk.kik.com" in jid_to_spam: #Temporary patch
                              jid_to_spam = jid_to_spam[:-17] #Temporary patch
                            if jid_to_spam.startswith("@"): #This reminds the user they dont need an @ if they use one, and removes it for them.
                                self.client.send_chat_message(JID, "Reminder: You do not need to put an \"@\" symbol before the username.") #This reminds the user that they dont
                                jid_to_spam = jid_to_spam.replace("@", "", 1) #This gets rid of the @ in the username
                                time.sleep(0.5) #Waits half a second
                            message_to_spam = split_string[1] #Isolates the message we got in split_string
                            if "groups" in jid_to_spam: #Checks if the JID they gave is actually a GJID and warns them if so.
                                self.client.send_chat_message(JID, "You can't use a GJID for the spam command.")
                            else: #Sends a confirmation of who is being spammed with what
                                self.client.send_chat_message(JID, "I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(message_to_spam) + "\"!")
                                print("I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(
                                    message_to_spam) + "\"!")
                                while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                    self.client.send_chat_message(jid_to_spam, emoji.emojize(message_to_spam)) #This is the bot spamming
                                    time.sleep(0.2) #< This is the delay between each message. You should leave it alone but if you need it to be faster/slower you can change it. NEVER set to 0, IP bans suck.
                    else: #This lets the user know when they used the command wrong because "w/" isnt in the string
                        self.client.send_chat_message(JID, "You need to put a \"w/\" with one space on both sides between the JID/username and the spam message.")
                        time.sleep(0.5)
                        self.client.send_chat_message(JID, "To use the spam tool, use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\"\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue is a pretty color!\"")
            elif mssg.startswith("poke"):#Command for sending a single message to a user
                if mssg == "poke":
                    self.client.send_chat_message(JID, "To use the poke tool, please use \"poke [JID or Username] w/ [Message]\".\n\nExample: \"poke bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                    if " w/ " in mssg:
                        remove_poke = mssg.replace("poke ", "") #This takes the first part of the message off to isolate the jid/username and message
                        split_string = remove_poke.split(" w/ ", 1) #This splits the message into the JID/username and message.
                        jid_to_poke = split_string[0] #This isolates the JID.
                        '''
                        The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                        '''
                        if "@talk.kik.com" in jid_to_poke: #Temporary patch
                          jid_to_poke = jid_to_poke[:-17] #Temporary patch
                        if jid_to_poke.startswith("@"): #This reminds the user they dont need an @ if they use one, and removes it for them.
                            self.client.send_chat_message(JID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                            jid_to_poke = jid_to_poke.replace("@", "", 1)
                        message_to_send = split_string[1] #Isolates the message we got in remove_poke
                        if "groups" in jid_to_poke:#Checks if the JID they gave is actually a GJID and warns them if so.
                            self.client.send_chat_message(JID, "You can't use a GJID for the poke command.")
                        else: #Sends a confirmation of who is being sent what
                            self.client.send_chat_message(JID, "I am poking the user \"" + jid_to_poke + "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                            print("I am poking the user \"" + jid_to_poke + "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                            self.client.send_chat_message(jid_to_poke, emoji.emojize(message_to_send))
                    else: #This lets the user know when they used the command wrong because "w/" isn't in the string
                        self.client.send_chat_message(JID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                        time.sleep(0.5)
                        self.client.send_chat_message(JID, "To use the poke tool, use \"spam [JID or Username] w/ [Message]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            elif mssg.startswith("sendfriend"): #This is a command for sending a friend request to a JID
                self.client.send_chat_message(JID, "Tip: You should only use this in groups so that you can trigger all of your bots at once! That's kinda the point of this command...")
                if mssg == "sendfriend":
                    self.client.send_chat_message(JID, "To use the sendfriend tool, please use \"sendfriend [JID or Username]\".\n\nExample: \"sendfriend stethosayshello_3pf@talk.kik.com\"") #This reminds the user that this command is best for groups
                else:
                    remove_sendfriend = mssg.replace("sendfriend ", "", 1) #This removes the beginning of the message to isolate the JID
                    '''
                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                    '''
                    if "@talk.kik.com" in remove_sendfriend: #Temporary patch
                      remove_sendfriend = remove_sendfriend[:-17] #Temporary patch
                    self.client.send_chat_message(JID, "I am sending a friend attribution request and \"I'm adding you as a friend\" message to \"" + remove_sendfriend + " !")
                    self.client.send_chat_message(remove_sendfriend, "I'm adding you as a friend!") #This lets the user know they are being added
                    self.client.add_friend(remove_sendfriend) #This adds the user as a friend
            elif mssg.startswith("leave"): #This command is for eaving groups with a GJID
                remove_leave = mssg.replace("leave ", "", 1) #This removes the first part of the message to isolate the GJID
                if mssg == "leave": #This checks if the message is just "leave" and gives instructions if so
                    self.client.send_chat_message(JID, "To use the leave command, please use \"leave [GJID]\"")
                else:
                    if "groups" in remove_leave: #This checks if the given GJID is in fact a GJID
                        self.client.send_chat_message(JID, "Attempting to leave \"" + remove_leave + "\"!")
                        self.client.leave_group(remove_leave) #This leaves the group
                    else: #This tells the user that they used a JID or otherwise invalid input
                        self.client.send_chat_message(JID, "You must use a valid GJID in the leave command! You used \"" + remove_leave + "\"!")

        def on_group_message_received(self, chat_message: chatting.IncomingGroupChatMessage):
            mssg = emoji.demojize(chat_message.body.lower())
            GJID = chat_message.group_jid
            if mssg.startswith("groupspam"): #This command spams a group with a message.
                if mssg == "groupspam": #This elaborates on how to use groupspam if the user just says "groupspam"
                    self.client.send_chat_message("To use the group spam tool, use \"groupspam [Message]\", or \"groupspam gif [query]\"")
                else: #This is the spam part
                    if mssg.startswith("groupspam gif"): #This checks if it's the gif command and continues if so
                        failed = False #This sets the failed variable we use later
                        gif_query = str(mssg.replace("groupspam gif ", "", 1)) #This isolates the gif query
                        try:
                            self.client.send_chat_message(GJID, "Testing query \"" + str(gif_query) + "\"...") #This lets the user know it is testing the query
                            self.client.send_gif_image(GJID, gif_query) #This attempts to send a gif with the query
                        except: #This is triggered if the attempt fails
                            failed = True
                        if failed == True:
                            self.client.send_chat_message(GJID, "I couldn't find a gif for the query" + gif_query + "\"!") #This lets the user know the attemot failed
                        else:
                            self.client.send_chat_message(GJID, "I will spam gifs with the query \"" + gif_query + "\"!\nTHIS IS YOUR 5 SECOND WARNING TO LEAVE THE GROUP.\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)") #This confirms the request
                            time.sleep(5)
                            print("I am spamming gifs with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)") #This confirms the request in the terminal
                            while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv": #This is a random variable to trigger the while loop
                                self.client.send_gif_image(GJID, gif_query) #This sends the gof with the query
                                time.sleep(0.3) #This is the wait between each message. Never change it to 0, IP bans suck.
                    else:
                        self.client.send_chat_message(GJID, "THIS IS YOUR 5 SECOND WARNING TO LEAVE THE GROUP.")
                        time.sleep(5)
                        while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv": #This triggers a while loop with a random variable
                            spam_message = mssg.replace("groupspam ", "", 1) #This isolates the message the user wants to send.
                            while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                self.client.send_chat_message(GJID, emoji.emojize(spam_message)) #This sends the given message in a loop
                                time.sleep(0.3) #This is the wait between each message. Never change it to 0, IP bans suck.
            elif mssg == "ping": #command to check if bot is online
                self.client.send_chat_message(GJID, "pong") #Replies "pong". Pretty simple
            elif mssg == "friend": #This command lets the user know the friend command only works in PMs
                self.client.send_chat_message(GJID, "This can only be used in PMs")
            elif mssg.startswith("gif"):
                gif_query = mssg.replace("gif ", "", 1)
                self.client.send_chat_message(GJID, "Searching for a gif with the query \"" + str(gif_query) + "\"...")
                try: #This attempts the gif query once first to check if its valid
                    self.client.send_gif_image(GJID, gif_query) #This tries to send a gif with the query
                except:
                    self.client.send_chat_message(GJID, "I couldn't find a gif for the query" + gif_query + "\"!")
            elif mssg == "commands": #command for listing the commands.
                self.client.send_chat_message(GJID, "To spam a user's PMs, use \"spam [JID or Username] w/ [Message]\", this command works both in groups and PMs.\n\nTo spam a group, say \"friend\" in PMs to add me then add me to the group you wish to spam and say \"groupspam [message]\".\n\n Keep in mind that once you start spam, it will not stop until you restart the bot.")
            elif mssg.startswith("spam"): #Command for spamming a user.
                if mssg == "spam": #Elaborates on how to use spam if the message is just "spam"
                    self.client.send_chat_message(GJID, "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                    if " w/ " in mssg: #This checks if "w/" was in the string and continues if so
                        if mssg == "spam":  # Elaborates on how to use spam if the message is just "spam"
                            self.client.send_chat_message(GJID,
                                                          "To use the spam tool, please use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                        else:
                            if " w/ " in mssg:  # This checks if "w/" was in the string and continues if so
                                if mssg.startswith("spam gif"):
                                    failed = False
                                    remove_spam = mssg.replace("spam gif ",
                                                               "")  # This takes the first part of the message off to isolate the jid/username and query
                                    split_string = remove_spam.split(" w/ ",
                                                                     1)  # This splits the message into the JID/username and message
                                    jid_to_spam = split_string[0]  # This isolates the JID we got in split_string
                                    '''
                                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                                    '''
                                    if "@talk.kik.com" in jid_to_spam: #Temporary patch
                                      jid_to_spam = jid_to_spam[:-17] #Temporary patch
                                    gif_query = split_string[1]  # This isolates the query we got in split_string
                                    try:  # This attempts the gif query once first to check if its valid
                                        self.client.send_gif_image(jid_to_spam,
                                                                   gif_query)  # This tries to send a gif with the query
                                    except:  # This is triggered if it fails
                                        failed = True  # I could have just used "raise someerror" and except, but I was tired when I wrote this... I'ma just leave it. Don't @ me nobody really reads my code anyways. Except you... Hi nerd.
                                    if failed == True:  # This is triggered when gif grabbing fails
                                        self.client.send_chat_message(GJID,
                                                                      "I couldn't find a gif for the query" + gif_query + "\"!")  # This lets the user know it failed
                                    else:  # This is triggered if the gif query does not fail
                                        self.client.send_chat_message(GJID,
                                                                      "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This lets the user on kik know it is spamming gifs
                                        print(
                                            "I am spamming gifs to \"" + jid_to_spam + "\" with the query \"" + gif_query + "\"!\n(Keep in mind that some Kik mods cannot see gifs sent from bots.)")  # This displays in the terminal that gif spam was triggered
                                        while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":  # This triggers a while loop with the random string we made global earlier
                                            self.client.send_gif_image(jid_to_spam, gif_query)  # This sends the gif
                                            time.sleep(
                                                0.3)  # This is the wait between each message. Never change it to 0, IP bans suck.
                                else:
                                    remove_spam = mssg.replace("spam ", "") #This takes the first part of the message off to isolate the jid/username and message
                                    split_string = remove_spam.split(" w/ ", 1) #This splits the message into the JID/username and message
                                    jid_to_spam = split_string[0] #This isolates the JID
                                    '''
                                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                                    '''
                                    if "@talk.kik.com" in jid_to_spam: #Temporary patch
                                      jid_to_spam = jid_to_spam[:-17] #Temporary patch
                                    if jid_to_spam.startswith("@"): #This reminds the user they dont need an @ if they use one, and removes it for them.
                                        self.client.send_chat_message(GJID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                                        jid_to_spam = jid_to_spam.replace("@", "", 1)
                                        time.sleep(0.5) #Waits half a second
                                    message_to_spam = split_string[1] #Isolates the message we got in split_string
                                    if "groups" in jid_to_spam: #Checks if the JID they gave is actually a GJID and warns them if so.
                                        self.client.send_chat_message(GJID, "You can't use a GJID for the spam command.")
                                    else: #Sends a confirmation of who is being spammed with what
                                        self.client.send_chat_message(GJID, "I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(message_to_spam) + "\"!")
                                        print("I am spamming the user \"" + jid_to_spam + "\" with the message \"" + emoji.emojize(
                                            message_to_spam) + "\"!")
                                        while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv":
                                            self.client.send_chat_message(jid_to_spam, emoji.emojize(message_to_spam)) #This is the bot spamming
                                            time.sleep(0.2) #< This is the delay between each message. You should leave it alone but if you need it to be faster/slower you can change it. NEVER set to 0, IP bans suck.
                    else: #This lets the user know when they used the command wrong because "w/" isnt in the string
                        self.client.send_chat_message(GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the spam message.")
                        time.sleep(0.5)
                        self.client.send_chat_message(GJID, "To use the spam tool, use \"spam [JID or Username] w/ [Message]\", or \"spam gif [JID or Username] w/ [query]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ i like dick.\"")
            elif mssg.startswith("poke"):#Command for sending a single message to a user
                if mssg == "poke":
                    self.client.send_chat_message(GJID, "To use the poke tool, please use \"poke [JID or Username] w/ [Message]\".\n\nExample: \"poke bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
                else:
                    if " w/ " in mssg:
                        remove_poke = mssg.replace("poke ", "") #This takes the first part of the message off to isolate the jid/username and message
                        split_string = remove_poke.split(" w/ ", 1) #This splits the message into the JID/username and message.
                        jid_to_poke = split_string[0] #This isolates the JID.
                        '''
                        The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                        '''
                        if "@talk.kik.com" in jid_to_poke: #Temporary patch
                          jid_to_poke = jid_to_poke[:-17] #Temporary patch
                        if jid_to_poke.startswith("@"): #This reminds the user they dont need an @ if they use one, and removes it for them.
                            self.client.send_chat_message(GJID, "Reminder: You do not need to put an \"@\" symbol before the username.")
                            jid_to_poke = jid_to_poke.replace("@", "", 1)
                        message_to_send = split_string[1] #Isolates the message we got in remove_poke
                        if "groups" in jid_to_poke:#Checks if the JID they gave is actually a GJID and warns them if so.
                            self.client.send_chat_message(GJID, "You can't use a GJID for the poke command.")
                        else: #Sends a confirmation of who is being sent what
                            self.client.send_chat_message(GJID, "I am poking the user \"" + jid_to_poke + "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                            print("I am poking the user \"" + jid_to_poke + "\" with the message \"" + emoji.emojize(message_to_send) + "\"!")
                            self.client.send_chat_message(jid_to_poke, emoji.emojize(message_to_send))
                    else: #This lets the user know when they used the command wrong because "w/" isn't in the string
                        self.client.send_chat_message(GJID, "You need to put a \"w/\" with one space on both sides between the JID/username and the message.\n\n(Error: w/ not found in message string.)")
                        time.sleep(0.5)
                        self.client.send_chat_message(GJID, "To use the poke tool, use \"spam [JID or Username] w/ [Message]\".\n\nExample: \"spam bacon_6zl@talk.kik.com w/ Blue's a pretty color.\"")
            elif mssg.startswith("sendfriend"): #This is a command for sending a friend request to a JID
                if mssg == "sendfriend":
                    self.client.send_chat_message(GJID, "To use the sendfriend tool, please use \"sendfriend [JID or Username]\".\n\nExample: \"sendfriend stethosayshello_3pf@talk.kik.com\"") #This reminds the user that this command is best for groups
                else:
                    remove_sendfriend = mssg.replace("sendfriend ", "", 1) #This removes the beginning of the message to isolate the JID
                    '''
                    The below patch resolves the issue of invisible unicode characters not being captured when JIDs are copy-pasted. 
                    '''
                    if "@talk.kik.com" in remove_sendfriend: #Temporary patch
                      remove_sendfriend = remove_sendfriend[:-17] #Temporary patch
                    self.client.send_chat_message(GJID, "I am sending a friend attribution request and \"I'm adding you as a friend\" message to \"" + remove_sendfriend + " !")
                    self.client.send_chat_message(remove_sendfriend, "I'm adding you as a friend!") #This lets the user know they are being added
                    self.client.add_friend(remove_sendfriend) #This adds the user as a friend
            elif mssg.startswith("leave"): #This command is for eaving groups with a GJID
                remove_leave = mssg.replace("leave ", "", 1) #This removes the first part of the message to isolate the GJID
                if mssg == "leave": #This checks if the message is just "leave" and gives instructions if so
                    self.client.send_chat_message(GJID, "To use the leave command, please use \"leave [GJID]\"")
                else:
                    if "groups" in remove_leave: #This checks if the given GJID is in fact a GJID
                        self.client.send_chat_message(GJID, "Attempting to leave \"" + remove_leave + "\"!")
                        self.client.leave_group(remove_leave) #This leaves the group
                    else: #This tells the user that they used a JID or otherwise invalid input
                        self.client.send_chat_message(GJID, "You must use a valid GJID in the leave command! You used \"" + remove_leave + "\"!")

        def on_roster_received(self, response: FetchRosterResponse): #This function is triggered when the roster is recieved.
            #You can add an option to view the rosters here, but it was removed to avoid spam in the terminal. Just unquote it if you want to use it.
            #print("Roster:\n" + '\n'.join([str(member) for member in response.peers]))
            response: chatting.IncomingChatMessage
            self.client.send_chat_message(debug_jid, emoji.emojize(":warning: I'm online!"))

        def on_connection_failed(self, response: ConnectionFailedResponse): #This function is triggered when your kik bot's connection is closed/fails
            global result
            result = False #This lets the login stanzas know that the login failed and it can continue with the next one.
            print(bcolors.OKGREEN + emoji.emojize(" Kik closed the connection!") + bcolors.ENDC) #This lets the user know the connection was closed
            oof = open("loginerror.txt", "a+") #This opens the loginerror.txt file
            if use_creds:
                oof.write(username + "\n")
            else:
                oof.write(username_thing + str(thing) + "\n") #This writes the username of the bot into the loginerror.txt file for the login retry later
            oof.close() #This closes the text file. Always a good practice

        def on_login_error(self, login_error: LoginError): #This function is triggered when there is a login error.
            global result
            result = False #This lets the login stanzas know that the login failed and it can continue with the next one.
            if login_error.is_captcha(): #This is triggered when the error is a captcha. Would have added the captcha wizard, but thats not very useful in a botnet.
                if use_creds:
                    print(bcolors.FAIL + emoji.emojize(":warning: Oh no! There is a captcha on @" + username + ", I can't login! Please sign into it manually on your own device to clear the captcha.") + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + emoji.emojize(":warning: Oh no! There is a captcha on @" + username_thing + str(thing) + ", I can't login! Please sign into it manually on your own device to clear the captcha.") + bcolors.ENDC) #This warns the user of the captcha.
            else: #Any other issues are username/password mismatches, so this is triggered when the error is not a captcha.
                if use_creds:
                    print(bcolors.FAIL + emoji.emojize(":warning: Oh no! Your username or password for @" + username + " is incorrect!") + bcolors.ENDC)
                else:
                    print(bcolors.FAIL + emoji.emojize(":warning: Oh no! Your username or password for @" + username_thing + str(thing) + " is incorrect!") + bcolors.ENDC) #This warns the user the username/password is incorrect.

    if __name__ == '__main__': #This is used to execute the login process only if the file was run directly, and not imported.
        main()

clear = open("loginerror.txt", "w+") #This clears out loginerror.txt
clear.close()
if attempt_number == 0: #This checks if logins have been attempted yet, and starts the first login attempts if not.
    while int(thing) > 0: #This loops through the number of bots
        if use_creds:
            for username in credentials.keys():
                password = credentials[username]
                login(username, password, '')
                while result is None:
                    pass
                thing = int(thing) - 1 #This decreases the bot count by one after the login attempt
        else:
            for i in range(thing):
                stetho_string = username_thing + str(thing) #This gets the username to login as
                login(stetho_string, given_pass, thing) #This attempts the login
                while result is None:
                    pass
                thing = int(thing) - 1 #This decreases the bot count by one after the login attempt
    attempt_number = attempt_number + 1 #This increases the attempt number so that this chunk is not triggered again


def retry_login(password): #This function retries logns when there are closed connections
    errors = open("loginerror.txt", "r") #This opens loginerror.txt to read it
    number_of_errors = 0 #This sets the number of errors to 0 for the next step
    read_errors = errors.read() #This reads loginerror.txt
    errors_list = read_errors.split("\n") #This makes a list out of the contents of loginerror.txt
    for user in errors_list: #This loops through each user in the errors list
        if user: #This counts the number of users in the error list
            number_of_errors += 1
    if " " in errors_list: #This ignores any blank lines, happens sometimes.
        number_of_errors = number_of_errors - 1
    if number_of_errors > 0: #This checks if there are any errors, if so, attempts to log in.
        print(bcolors.OKGREEN + emoji.emojize(":warning: There is " + str(number_of_errors) + " closed connection(s). I'll attempt to sign into the account(s) again!") + bcolors.ENDC) #This lets the user know that the script will retry the login(s)
        ominous_dots(bcolors.OKGREEN + emoji.emojize("Re-attempting login(s)") + bcolors.ENDC)
        print("\n")
        time.sleep(1) #This waits a second so the user can read
        clear = open("loginretry.txt", "w+") #This clears the text from loginretry.txt
        clear.close() #This closes the file, always a good practice.
        oof = open("loginretry.txt", "a+") #This opens loginretry.txt to append to it
        for user in errors_list: #This loops through each user in errors list and adds them to loginretry.txt
            oof.write(user + "\n")
        oof.close() #This closes the file, always a good practice.
        retry = open("loginretry.txt", "r") #This opens loginretry.txt to read it
        read_retry = retry.read() #This reads loginretry.txt
        retry_list = read_retry.split("\n") #This splits loginretry.txt into a list
        clear = open("loginerror.txt", "w+") #Clears the text from loginerror.txt
        clear.close() #This closes the file, always a good practice.
        for name in retry_list: #This loops through the failed logins
            if number_of_errors > 0: #This checks if there are errors remaining before continuing
                if " " in name: #This makes lines with spaces blank
                    checked_name = name.replace(" ", "")
                else:
                    checked_name = name
                if not not checked_name: #This ignores blank lines
                    if use_creds:
                        login(checked_name, credentials[checked_name], '')
                    else:
                        login(checked_name, password, number_of_errors) #This attempts to login
                time.sleep(5) #This waits 5 seconds between each login to avoid closed connections
                number_of_errors = number_of_errors - 1 #This subtracts 1 from the error count
        retry.close() #This closes the file, always a good practice.


errors = open("loginerror.txt", "r") #This opens loginerror.txt to read it
number_of_errors = 0 #This sets the number of errors to 0 to later count the errors
read_errors = errors.read() #This reads loginerror.txt
errors_list = read_errors.split("\n") #This splits the contents of loginerror.txt into a list

for user in errors_list: #Loops through each user in the list we made above
    if user: #This counts the number of errors
        number_of_errors += 1
if " " in errors_list: #This ignores blank lines, happens from time to time.
    number_of_errors = number_of_errors - 1

number_of_attempts = 20 #This specifies the number of times the bot will retry logins when connections are closed. I recommend you leave it alone.
while number_of_attempts > 0: #This checks if it is the first login attempt or not. If not, continues.
    if number_of_errors > 0: #This checks if there are any errors left. If there are errors, it continues.
        retry_login(given_pass) #This attempts login again
    number_of_attempts = number_of_attempts - 1 #This subtracts 1 from the number of attemots so that it only retries a specified number of times.
#keep_alive()
time.sleep(2) #Slight delay so stuff doesnt spam
print(bcolors.OKGREEN + emoji.emojize("\n:black_small_square: \"Spam [JID or Username] w/ [Message]\" - Used to spam a user's PMs.\n:black_small_square: \"Spam Gif [JID or Username] w/ [Query]\" - Used to spam a user's PMs with a gif.\n:black_small_square: \"Poke [JID or username] w/ [Message]\" - Used for forwarding a single message to a user.\n:black_small_square: \"Poke Gif [JID or username] w/ [Query]\" - Used for forwarding a single gif to a user.\n:black_small_square: \"Friend\" - Used to add the bot as a friend so that you can add it to groups.\n:black_small_square: \"SendFriend [JID or Username]\" - Used to send a friend attribution request to a user.\n:black_small_square: \"GroupSpam [Message]\" - Used to spam the group that this command is used in.\n:black_small_square: \"GroupSpam Gif [Query]\" - Used to spam the group that this command is used in with gifs.\n:black_small_square: \"Gif [Query]\" - Used to send a single gif in the group that this command is used in.\n:black_small_square: \"Leave [GJID]\" - Used for making your bot(s) leave groups.\n") + bcolors.ENDC) #This explains the commands to the user
print(bcolors.FAIL + emoji.emojize("\n:warning: You can now use the botnet.\n") + bcolors.ENDC) #This lets the user know the botnet is ready
clear = open("loginretry.txt", "w+") #This clears the Loginretry.txt file
clear.close() #This closes the file, always a good practice.

while spam == "Qm90IG1hZGUgYnkgU3RldGhvU2F5c0hlbGxv": #This keeps the bot idle. (spam is just the variable that happens to be convenient for a while loop)
    in_console_message = input("") #This checks if the user has typed anything into the console
    if in_console_message.lower() == "ping": #If they type ping, it will say pong pack.
        print(bcolors.OKGREEN + emoji.emojize("\npong.\n") + bcolors.ENDC)
    else: #If they do not type ping, it reminds them that commands must be sent to the kik bots.
        print(bcolors.FAIL + emoji.emojize("\n:warning: You can't use commands directly in the console! You need to message your bots on Kik.") + bcolors.ENDC)
