#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import os
import sys
from telethon.sync import TelegramClient, events

session_name = "botname"
api_id = apiid
api_hash = "apihash"
groupchat_id = gcid

os.chdir(sys.path[0])

client = TelegramClient(session_name, api_id, api_hash)
client.start()
entity = client.get_entity(groupchat_id)
client.delete_messages(entity, sys.argv[1])
client.disconnect()
