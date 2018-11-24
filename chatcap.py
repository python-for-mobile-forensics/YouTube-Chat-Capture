#!/usr/bin/env python
import json
import time
from pprint import pprint
import sys

with open(sys.argv[1]) as data_file:
    data = json.load(data_file)

mylist = data.get('response',[])
mylist = mylist.get('continuationContents',[])
mylist = mylist.get('liveChatContinuation',[])
mylist = mylist.get('actions',[])

for item in mylist:
  rep = item.get('replayChatItemAction', [])
  rep = rep.get('actions', [])
  for item in rep:
    act = item.get('addChatItemAction', [])
    act = act.get('item', [])
    mess = act.get('liveChatTextMessageRenderer', [])
    for values in mess:
      author = mess.get('authorName', [])
      author = author.get('simpleText', [])
      message = mess.get('message', [])
      message = message.get('simpleText', [])
      utcstamp = mess.get('timestampUsec', [])
      chanid = mess.get('authorExternalChannelId', [])
      readtime = time.strftime("%a, %d %b %Y %H:%M:%S %Z", time.localtime(int(utcstamp)/1000000.))
      print(author + '|' + chanid + '|' + str(message) + '|' + readtime)
