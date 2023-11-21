#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from telethon.sync import TelegramClient, events

# import nest_asyncio
# nest_asyncio.apply()

session_name = "botname"
api_id = apiid
api_hash = "apihash"
groupchat_id = gcid

os.chdir(sys.path[0])

client = TelegramClient(session_name, api_id, api_hash)
client.start()
entity = client.get_entity(groupchat_id)
def callback(current, total):
    print('Uploaded', current, 'out of', total,
          'bytes: {:.2%}'.format(current / total))
client.send_file(entity,sys.argv[1],caption=sys.argv[2],progress_callback=callback,part_size_kb=512)
client.disconnect()
