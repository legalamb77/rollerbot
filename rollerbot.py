import praw

#Bot input format: /roller followed by command.
#Accepted commands:
#xdy+z, for integers x,y, and z.
#This roll can be followed by certain commands.
##-dropxy: where x and y are ints. This ignores up to y rolls with a value of x.
##-bestx: where x is an int. Returns only the top x dice out of the dice rolled.
##-exploding: when a die is rolled that gets a max value, an additional die is rolled.
#if /roller is called with badly a poorly formatted command, a small faq statement is printed showing the bot's input format.

with open(hiddenInfo) as f:
    hiddenVars=f.readlines()
hiddenVars=[x.strip() for x in hiddenVars]

rollerbot=praw.Reddit(client_id=hiddenVars[0], client_secret=hiddenVars[1],
                             password=hiddenVars[2], user_agent=hiddenVars[3],
                                                  username=hiddenVars[4])
subreddit=bot,subreddit('bottest')

comments=subreddit.stream.comments()

for comment in comments:
    text=comment.body
    if '/roller' in text:
        print "ayylmao"
