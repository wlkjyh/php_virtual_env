import re

def get_realname(name):
    return re.sub(r'[\\/:*?"<>|]', '', name)