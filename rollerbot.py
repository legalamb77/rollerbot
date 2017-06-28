import praw
import random

#Bot input format: /roller followed by command.
#Accepted commands:
#xdy+z, for integers x,y, and z.
##Currently, to prevent pointlessly giant rolls, x is capped at two digits, and y and z are capped at 4
#This roll can be followed by certain commands.
##-dropxy: where x and y are ints. This ignores up to y rolls with a value of x.
##-bestx: where x is an int. Returns only the top x dice out of the dice rolled.
##-exploding: when a die is rolled that gets a max value, an additional die is rolled.
#if /roller is called with badly a poorly formatted command, a small faq statement is printed showing the bot's input format.

faq="ayylmao"

def rollDie(sidesDice):
    return random.randint(1,sidesDice)

def rollDice(numDice,sidesDice,mod,modVal):
    #returns the value of the rolled dice
    sum=0
    while(numDice>0):
        sum+=rollDie(sidesDice)
        numDice-=1
    if mod=="-":
        sum-=modVal
    elif mod=="+":
        sum+=modVal
    elif mod=="*":
        sum*=modVal
    elif mod=="/":
        sum/=modVal
    return sum

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
        expression='/roller\s*(\d\d?)d(\d{1,4})((\+|\-|\*|/)(\d{1,4}))?'
        match=re.match(expression,text)
        if match:
            numberOfDice=int(match.group(1))
            sidesOfDice=int(match.group(2))
            modifier=None
            modifierValue=0
            if match.group(3):
                modifier=match.group(4)
                modifierValue=int(match.group(5))
            value=rollDice(numberOfDice,sidesOfDice,modifier,modifierValue)
            comment.reply(value)
        else:
            #Reply with faq
            comment.reply(faq)
