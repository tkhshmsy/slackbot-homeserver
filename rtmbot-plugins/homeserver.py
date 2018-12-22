from __future__ import print_function
from rtmbot.core import Plugin
import pychromecast
import configparser
import json

## vars
config = configparser.ConfigParser()
config.read('homeserver.ini')
chromecasts = pychromecast.get_chromecasts()
chromecast = next(cc for cc in chromecasts if cc.device.friendly_name == config['chromecast']['friendly_name'])
chromecast.wait()

## funcs
def is_called(message):
    if message['type'] != 'message':
        return False, "invalid type"
    if message['team'] != config['slack']['team']:
        return False, "invalid team"
    if message['channel'] != config['slack']['channel']:
        return False, "invalid channel"
    phrase=""
    if 'text' in message:
        # user input
        phrase = message['text']
    elif 'attachments' in message:
        # bot input
        if 'text' in message['attachments'][0]:
            phrase = message['attachments'][0]['text']
        elif 'pretext' in message['attachments'][0]:
            phrase = message['attachments'][0]['pretext']
        else:
            return False, "invalid attachments"
    else:
        return False, "no text"
    own = '<@' + config['slack']['user'] + '>'
    if own not in phrase:
        return False, "not me"
    return True, phrase.replace(own, '').strip()

def exec_command(command):
    try:
        j = json.loads(command)
    except:
        return False, "invalid format"
    if 'command' not in j:
        return False, "no command"
    if j['command'] == 'play_shortcut':
        return play_shortcut(j['shortcut'])
    return False, "command not found"

def play_shortcut(shortcut):
    if shortcut not in config['shortcut']:
        return False, "shortcut:{} not found".format(shortcut)
    url = config['shortcut'][shortcut]
    cast_shortvideo(url)
    return True, "play_shortcut {}".format(shortcut)

def cast_shortvideo(url):
    mc = chromecast.media_controller
    mc.play_media(url, 'video/mp4')
    mc.block_until_active()

## main
class HomeServerPlugin(Plugin):
    def process_message(self, message):
        flag , msg = is_called(message)
        if not flag:
            # no response
            return
        flag, msg = exec_command(msg)
        self.outputs.append([config['slack']['channel'], msg])
        return
