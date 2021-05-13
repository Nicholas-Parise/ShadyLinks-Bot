import praw
import re
import os
import time
import random
reddit = praw.Reddit(client_id='NFETfLjwQ4WIbA',
                     client_secret='AvSMBJK3yEttlKEgk3JLp6bh7Rp3VA',
                     user_agent='shadyLinks by u/ForArms',
                     username='shadyLinks',
                     password='P8p(/qm7RO-q.Gu')


Phrase = [
    "I like midget porn as much as the next guy but....",
    "Ah fellow foot fetishist, got any more?",
    "Belle delphine nude?!?!?! Sweet!",
    "subpar porn she moans like my mom",
    "great vid I lost No Nut November to this video",
    "bruh my mom was in the room, why did you link hardcore porn?",
    "Im Foaming At The Dick from this video",
    "This video is Mouth-watering",
    "The video title calls her a milf but she's only like 25. Not funny didn't cum!",
    "I have that same ikea bed, although mine is a little cleaner....",
    "she can really fit a lot of ping pong balls up there",
    "Bruh she's like 60 WHO WATCHES GRANDMAN PORN!",
    "Seriously? After 20 minutes of getting to choke this gorgeous girl with his cock, two little poots of cum is all he could manage? Pathetic.",
    "This pornstar has very fake boobs",
    "she has an AMAZING PUSSY",
    "Best porn of my entire life but don't know if I jizzed for the guy or for the girl",
    "My first time was a lot like this. Except there was more crying on my part. And I only lasted about 10 pumps. And she looked like David Ortiz.",
    "She's so amazing at deepthroating, I bet she could swallow a John Cena figurine whole",
    "\"First time anal\" who actually belives this stuff",
    "\"Stepsister fucks\" why does every porn have to be step sister?",
    "OMG I know her! she obviously got a lot of work done she was like an A cup in high school... at least she got nice fake tits ",
    "why did she get such awful tattoos? At least her pussy is nice",
    "She has nice tits, but A Man Has Fallen Into The River in LEGO City",
    "I'd suck a fart out of her ass so hard her forehead would collapse",
    "That chick is so hot i would consider sucking her dads dick",
    "well for anyone wondering it's gay porn",
    "well for anyone wondering it's lesbien porn",
    "well for anyone wondering it's hentai",
    "for anyone wondering it's Mia khalifa in this video",
    "for anyone wondering it's Lana Rhoades in this video",
    "for anyone wondering it's Riley Reid in this video",
    "for anyone wondering it's Abella danger in this video",
    "for anyone wondering it's Brandi love in this video",
    "for anyone wondering it's Johnny sins in this video",
    "If her boobs were any further apart they'd be on her back",
    "I'd fuck her in the ass so hard my initials would be in her shit",
    "This porn is FANTASTIC! She really boobs",
    "they had me until he shaved his ass",
    "Who the fuck links porn in this sub",
    "ahh that was a nice rub/tug. I think I'll leave a comment to display how satisfied I am",
    "let's have a conversation with the other people who are enjoying this anal fisting video",
    "why is she wearing a diaper while getting fucked?",
    "why is he wearing a diaper while getting fucked?",
    "wow she peed all over that expensive camera, what a bitch",
    "bruh explosive diarrhea while getting fucked? DISGUSTING",
    "Her boobs are bigger than my future",
    "thats not a clit, thats a dick, you cant fool me!!!!!!!",
    "Japanese fantasy rape porn? Just no my dude",
    "The only thing hairier than her asshole is her lip",
    "That guy is living like Larry!",
    "This is not real DP. It says DP in the title, but real DP is two dicks in one hole. While this clip indeed has two dicks in it, they are clearly going in two different holes.",
    "If she his mom why doesn't he call her mom?",
    "I'm not gay but I would fuck him",
    "Why was he covered in Chocolate Syrup?",
    "she's so hot she could make a dead man cum",
    "This is the first video that shows up when you search anne frank",
    "She queefs at 19:23",
    "damn that was some rough oral she was like gluk gluk glukkk....hahahahaha",
    "I used be a heterosexual like you, then I took a dick in the butt.",
    "(IN PUBLIC, ALMOST CAUGHT!) what a cliche over used title",
    "Why are the guys moans loudler than the chicks?",
    "That is one dirty casting couch",
    "who Cums on feet? you apparently",
    "I wish I could suck cock like her, he cums in under a minute, what a lucky guy ",
    "Elastic girl rule 34? well it's not my place to judge...",
    "This room smells like enemas and sadness"
]


FakePhrase = [
"bruh why did you send a rick roll? We just want the sauce",
"This is not the sauce",
"I understand the joke of sending fake sauce, but come on",
"I am very dissapopinted in this sauce, it tasted very sour and had the consistancy of chunky vomit 2/10 would not recomend this recipe",
"Wow really mature guys rick rolling in 2021",
"Imagine rick rolling in a nsfw sub",
"What a misleading link",
"This porn is FANTASTIC! The pornstar just needs to work on communication, aim, dick placement, cum flicks, g spot awareness, flashes, positioning, spray control and getting hard",
"very disappointing video, not as good as I though it would be"
#pornhub.com
]


#comment.author
IgnoreAuthor = [
"save_video",
"shadyLinks",
"Evthe420",
"unyoda-bot",
"LoneWolf242009",
"Zephrnos",
"JugoDePescado",
"NekoGarou",
"madmaximus",
"Madmax-imus",
"sixtyfivewolves",
"Hot_Carry2617",
"Wixhael",
"chillbro360",
"AIex-Shaw",
"TheWither2010",
"CobBasey",
"JayMagpie",
"GreatAwesome_Bombs",
"quirapretty",
"killerboy3143",
"therealsaucebot",
"tiffanysporn",
"_J_64",
"familyfriendlyjosh32",
"sixtyfivewolves",
"KassMonday",
"bloodban7",
"OwO-tism"
]

#comment.subreddit.display_name
IgnoreSub = [
"test",
"MadeMeSmile",
"SMG4",
"PewdiepieSubmissions",
"r4rmontreal",
"teenagers",
"tumblr",
"niceguys",
"BABYMETAL",
"flashlight",
"OrthodoxChristianity",
"VirginiaTech",
"PornhubComments"
]

def Test(PHLimiter):
    if (PHLimiter > 3):
        print("yes")


def Wait():
    if(true):
        print("a")


print("Start")

subreddit = reddit.subreddit('all')

#subreddit = reddit.subreddit('u_shadyLinks')

#subreddit.submit('Test post, please ignore', 'Self post text here')

if not os.path.isfile("posts_replied_to.txt"):
    posts_replied_to = []
else:
    with open("posts_replied_to.txt", "r") as f:
        posts_replied_to = f.read()
        posts_replied_to = posts_replied_to.split("\n")
        #print(posts_replied_to)
        posts_replied_to = list(filter(None, posts_replied_to))

later = 1618520163
difference = 0
# I dont want it to always respond to porn so I will add a limiter to stop rampant porn comments
PHLimiter = 2
Test(PHLimiter)


while True:  # {
    print("ran")
    for comment in subreddit.stream.comments(): #{
        if comment.id not in posts_replied_to:#{
            #print((comment.submission.locked))
            #Rick Rolls and not rick astley
            if (PHLimiter < 4) and (re.search(r"dQw4w9WgXcQ\)", comment.body)) and not (re.search(r"((R|r)ick|(A|a)stley)", comment.body)) and (comment.author not in IgnoreAuthor) and (comment.subreddit.display_name not in IgnoreSub) and (comment.submission.locked == False) and (comment.author != comment.submission.author): #{
                
                print(str(comment.author)+" "+str(comment.submission.author))

                PHLimiter += 1
                print("Found post")
                RandInt = random.randint(0, 64)
                now = time.time()
                difference = int(now-later)
                later = time.time()
                print("It took: "+ str(difference)+" seconds to find post")
                if difference < 660:  # {
                    print("waiting for ratelimit: " +str(660-difference)+" seconds remaining")
                    time.sleep(660-difference)
                # }
                try:  # {
                    comment.reply(f'''{Phrase[RandInt]}''')
                    print('reply successful to:' + str(comment.author)+ " in the subreddit: "+str(comment.subreddit.display_name))
                    posts_replied_to.append(comment.id)
                    with open("posts_replied_to.txt", "w") as f:  # {
                        for post_id in posts_replied_to:  # {
                            f.write(post_id + "\n")
                        # }
                    # }
                    print("Searching...")
                # }
                except Exception as E:  # {
                    print(E)
                    break
                    continue
                # }
            #}

            #Real Links
            if (PHLimiter > 3) and (re.search(r"(\(https://www.|\(www.|\()pornhub.com", comment.body)) and (comment.author not in IgnoreAuthor) and (comment.subreddit.display_name not in IgnoreSub) and (comment.submission.locked == False) and (comment.author != comment.submission.author): #{
                PHLimiter = 0
                print("Found porn post")
                RandInt = random.randint(0, 8)
                now = time.time()
                difference = int(now-later)
                later = time.time()
                print("It took: "+ str(difference)+" seconds to find post")
                print(difference)
                if difference < 660:  # {
                    print("waiting for ratelimit: " +str(660-difference)+" seconds remaining")
                    time.sleep(660-difference)
                # }
                try:  # {
                    comment.reply(f'''{FakePhrase[RandInt]}''')
                    print('reply successful to:' + str(comment.author)+ " in the subreddit: "+str(comment.subreddit.display_name))
                    posts_replied_to.append(comment.id)
                    with open("posts_replied_to.txt", "w") as f:  # {
                        for post_id in posts_replied_to:  # {
                            f.write(post_id + "\n")
                        # }
                    # }
                    print("Searching...")
                # }
                except Exception as E:  # {
                    print(E)
                    break
                    continue
                # }

            #}






        #}
    #}
# }

     


# search for a rick roll link
    # use database of rick roll links like from PornHub or youtube
# if it is a rick roll link
# comment under it with wacky phrases that have nothing to do with it

# search for a shady link
    # use data base of shady links ie: discord links, shortened links etc
#  comment something like: this has been detected as a shady link, I sudgest you use caution
#

# Hello this is an automated message I am a bot, if I posted something I should not have please DM me and my developer will delete this comment.
