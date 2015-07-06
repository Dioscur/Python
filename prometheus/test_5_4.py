import sys
import math

def file_search(folder, filename):
    path = ''
    if folder == filename:
        return (folder[0]+'/')
    elif filename in folder:
        path = folder[0] + '/' + filename
        return path
    else:
        for i in folder:
            if isinstance(i,list):
                res = file_search (i, filename)
                if isinstance (res, str): 
                    path = folder[0] + '/' + res
                    return path
    if path == '': 
        return False


a = [ '/home', ['user1'], ['user2', ['my pictures'], ['desktop', 'not this', 'and not this', ['new folder', 'hereiam.py' ] ] ], 'work.ovpn', 'prometheus.7z', ['user3', ['temp'], ], 'hey.py']
b = 'hereiam.py'

print file_search (a,b)
