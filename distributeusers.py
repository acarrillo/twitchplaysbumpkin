import requests
import random
import json

red = '_twitchplayspumpkinbots_1414827017243'
blue = '_twitchplayspumpkinbots_1414830320380'
twitchchannels = [red,blue]

userstats = requests.get("http://tmi.twitch.tv/group/user/twitchplayspumpkinbots/chatters") 
userarray = json.loads(userstats.text)['chatters']['viewers']


def newMember(username):
	headers = {'Authorization': 'OAuth 4mry7bjkhd88akziaj7y3lz8k6cso27'}
	payload = {'oauth_token' : '4mry7bjkhd88akziaj7y3lz8k6cso27', 
		'irc_channel' : random.choice(twitchchannels),
		'username': username}
	r = requests.post("http://chatdepot.twitch.tv/room_memberships", data=payload, headers=headers)

for name in userarray:
	newMember(name)