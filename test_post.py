import json
import requests

# curl: curl -H "Authorization: OAuth 4mry7bjkhd88akziaj7y3lz8k6cso27" --data "oauth_token=4mry7bjkhd88akziaj7y3lz8k6cso27&irc_channel=_twitchplayspumpkinbots_1414851506853&username=reapthenightmare" http://chatdepot.twitch.tv/room_memberships

#content-type application/x-www-form-urlencoded; charset=UTF-8

url = 'http://chatdepot.twitch.tv/room_memberships'
payload = {'oauth_token':'4mry7bjkhd88akziaj7y3lz8k6cso27',
           'irc_channel':'_twitchplayspumpkinbots_1414851506853',
           'username':'reapthenightmare'}
auth = OAuth1('4mry7bjkhd88akziaj7y3lz8k6cso27')

r =  requests.post(url, data=payload, auth=auth)
