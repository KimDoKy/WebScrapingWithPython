from twitter import *

t = Twitter(aouth=OAuth('Access Token','Access Token Secret','Consumer Key','Consumer Secret'))
statusUpdate = t.statuses.update(status='Twitter Test')
print(statusUpdate)
