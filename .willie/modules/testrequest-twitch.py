import requests
import random

red = '_twitchplayspumpkinbots_1414827017243'
blue = '_twitchplayspumpkinbots_1414830320380'
twitchchannels = [red,blue]
newmember = 

def newMember(username):


payload = {'oauth_token' : '4mry7bjkhd88akziaj7y3lz8k6cso27', 
'irc_channel' : random.choice(twitchchannels)
'username': newmember}

r = requests.post("http://chatdepot.twitch.tv/room_memberships", params=payload)

