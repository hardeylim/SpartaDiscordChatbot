# coding=utf-8
# This is a sample Python script.

import random
# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import time
import datetime

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

textAreaCSS = 'slateTextArea-27tjG0'
caCooldown = 601
caNewcomerLink = 'https://discord.com/channels/912425349260922890/925481145532022844'
caGeneralLink = 'https://discord.com/channels/912425349260922890/912428979452002304'
caTheMarket = 'https://discord.com/channels/912425349260922890/925773152901013504'
caTheBasement = 'https://discord.com/channels/912425349260922890/925820459981877358'
caGamesLink = 'https://discord.com/channels/912425349260922890/925820444286808134'

casinoRoyaleLink = 'https://discord.com/channels/898625839330099210/946070912371937280'
casinoDenLink = 'https://discord.com/channels/898625839330099210/946071567417368586'

dogStories = []
sentenceList = ["What was your worst travel experience?",
                "How important do you think self-improvement is?",
                "What strategies do you use to make big decisions?",
                "Im still contemplating on what level I will reach this week."
                "What level do you guys want to achieve this week?",
                "If given a chance would you turn back time lol ",
                "What did you guys have for breakfast",
                "What did you guys have for dinner",
                "What did you guys have for lunch",
                "Whats the best thing that happened to you today",
                "Any new years resolutions?",
                "Any weird new years resolutions?",
                "Any weird new years coin resolutions?",
                "What do you think the future of crypto will be",
                "I wonder what the next big wave for crypto will be",
                "Memecoins NFTs what u guys think is next lol",
                "Who has tried intermittent fasting here",
                "Diet does actually work",
                "Did you exercise today anon?? do itt",

                # Greetings
                "Hello there good sir! ",
                "Hola como esta amigo amigo",
                "Hola como esta compadre comadre",
                "Hows everyone doing today, Im doing great",
                "Ola amigos hows it goinnnnn",
                "Wazzup boys",
                "MOn senoir good morning",
                "MOn senoir good evening",
                "Gday mateyyy watcha up to today",
                "Guten tag my frens here in cryptoland",
                "Hola new comers welcome to the healthy chat!"
                "Always keep safe everyone, these are strange times were in",
                "These are strange times were in, always keep safe everyone",
                "Do some exercise everyone",
                "This is a message to remind you to drink water! lots of it",
                "This is a message to remind you to move your ass today!",
                "This is a message to remind you to stretch and rest your eyes for a bit!",
                "Everyone remember to take your vitamins ayt?? ",
                "Eat healthy today friends, Longevity is key",
                "Rest a bit every once in a while, dont spend too much time looking at the screen. looool",
                "Dont skip breakfast guys, first and most important meal",
                "Everybody doing great? Alright take some rest and continue on",
                "Everyone have a great and fulfilling day today.",
                "I hope everyone is doing awesome today.",
                "I hope everyones feeling great today!",
                "New day boyz! We will make this day count!",
                "Remember to turn off DMs in privacy",
                "We vibinnn babyyyyyyy",

                # Reacting to chats
                "Damn bro I feel you.",
                "Yeah I agree man."
                "Hmmmm I agree to what youre saying to some extent",
                "Bruh thats awesome! gjgjgj",
                "Bro thats terrific",
                "Not really sure bro... gotta ask them",
                "Damn bro you almost got it",
                "I dont really know tbh",
                "As far as I can tell thats probably it",
                "Dude its fine, were getting thru this together.",
                "I can somehow sympathize with that brotherrr",
                "Yeah thats the reason why",
                "Honestly I agree with you",
                "I agree that that is what it really needs",
                "Bro thats awesome, good for you!!",
                "You go man! keep at it dont stop!",
                "Bro.... you can do it. Just trust yourself and thats all you need.",
                "Think about it bro, nobody gonna do it for you. You gotta push bruh",
                "only those who will spend hours in the platform will gain what they deserve",
                "Thats actually awesome. no lie",
                "No cap thats actually amazing",

                # Leveling
                "I really wanna grind til level 25 if time permits... damn want it so bad",
                "Im prolly aiming for level 15 or something",
                "Lets grind boys dont give up. This is the motivation you neeeeeed! LFG",
                "Dont stop when youre tire my man, Stop when its done",
                "Leveling is key, its the grind bruhhh",
                "We gonna keep going until we dropppp lezgo babyy",
                "Leveling is they key, patience young padawanszszzs",
                "One way or another Im getting to max level ",
                "The grind may be hard but so am I",
                "Bro lets get it, I hope we all get to max level.",
                "Lets push to get max level guys!!",
                "Im still allocating my time to invest here to level up.",
                "The goal is max level, whe question is when actually looool",
                "Yeah me too bro... I really want to reach that max level bruh",
                "Damn I really want that NFT, bless us the GODDOGS almighty",
                "The Gods will bless me with max level yo, lets freakin go. I believe",
                "Everyone will hopefully make it to WL, trust babyyyy",
                "Lets grind boyz, lets help each other",
                "I hope I have enough levels to grind until the next lottery"
                "I hope I get thru with the next lottery even though my level isnt maxed",
                "Brothers lets help each other, were all reaching the top together.",
                "New day boyz! We will make this day count lets keep grinding til we drop!",
                "WL WL WL iz what me wants, Im gonna get it babyyy manifest lezgo.!",
                "Time is of the essence, speed we must kekkk",
                "Im really excited when I get that WL, I really really want it so bad lol",
                "Lord of the dogs give me strength to reach levelus Maximusss",

                # Crypto Related
                "Which coins are you in guys, personally Im long BTC",
                "If it corrects tomorrow which coins are you guys buying",
                "Im so bullish on the market, NFA ofcourse. lol",
                "I wonder which are the top gainer coins for this week, Imma hunt gems",
                "What crypto are you guys interested aside from NFTs",
                "You guys bullish or bearish on the general crypto markets",
                "Crypto will be so revolutionary the suits cant ignore us loll",
                "Who here is frog nation?",
                "Do you guys think web3 is a fad or its here to stay",
                "Which NFTs are you bullish on aside from this ofcouse",
                "Top coins this season who you got",
                "Not sure what BTC gonna do next week damn kinda scared",
                "Damn eth really looks primed for a breakout, no?"
                "Im kinda believing the expanding cycles theory not sure.",

                # Quotes
                "Why does happiness come easily to some but not others? ",
                "Good quote You cant control what goes on outside, but you CAN control what goes on inside.",
                "Physical fitness is the first requisite of happiness. nice thing to think about.",
                "To keep the body in good health is a duty, otherwise we shall not be able to keep the mind strong and clear. by Buddha. Something to ponder on",
                "Health is wealth frens, treasure it",
                "An apple a day, keeps the doctor away",

                # Life update
                "Imma hit the gym later on today boys, I just need some kinda motivation",
                "Ate pizza yesterday for breakfast daaaamn!",
                "Contemplating on what to eat later.. Damn its always hard to choose.",
                "Im thinking of the splits that I will do for my next gym session",
                "I always do ab workouts after a solid days workout. I dunno I just watched or read it somewhere.",
                "Had a rough day yesterday boys, kinda need rest. No worries no biggie",
                "Life in general has been..... meh I dunno about you guys",
                "Damn keeping up with current events is so boring lol... theyre so repetitive, no? Feels like hedonic treadmill",
                "Im looking forward to events next week, hopefully fruitful",
                "Movies actually help me destress.",
                "I find that games can help in my cognitive.",
                "Been missing out on dates during lockdowns, hopefully when we go back to legit normal.",
                "New normal seems meh...... to me. I prefer old normal, if that makes any sense. lol",
                "We actually living in the future lol",
                "I cant imagine this reality if I was to go back 7 years from now",
                "Contemplating about life is really relaxing somehow",
                "The secret to life is really patience my frens, don't give up."

                ]
rpsChoices = ['rock', 'paper', 'scissors']

workTimeout = 60
rouletteTimeout = 21
diceTimeout = 15
sixtySeconds = 60
fiveMinutes = 300

driver = webdriver.Chrome()

driver.get(casinoRoyaleLink)
time.sleep(20)
field = driver.find_element_by_class_name(textAreaCSS)

loop = 1
counter = 1
# Initial Wait


def type_staggered_letters(command):
    for char in command:
        field.send_keys(char)
        time.sleep(0.3)
    print(datetime.datetime.now().strftime("%H:%M:%S"), 'Typing ', command, ' ')
    field.send_keys(Keys.ENTER)


while True:
    print(datetime.datetime.now().strftime("%H:%M:%S"), '######## Start House of Sparta loop ########')
    for x in range(1, 13):
        if x == 1:
            type_staggered_letters('/work ')
        if x == 1 or x == 4 or x == 7 or x == 10:
            type_staggered_letters('/dice 100')

        time.sleep(fiveMinutes)
        time.sleep(5)
    counter = counter + 1
    loop = loop + 1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print("Hi, {0}".format(name))  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == __main__:
    print_hi(PyCharm)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
