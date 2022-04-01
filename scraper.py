from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.types import InputPeerEmpty
from telethon.tl.types import (
    InputPeerEmpty,
    UserStatusLastWeek,
    UserStatusOnline,
    UserStatusRecently,
)
from telethon.tl import types as t
import os, sys
import configparser
import csv
import time
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import ChannelParticipantsSearch
from time import sleep
import datetime
re = "\033[1;31m"
gr = "\033[1;32m"
cy = "\033[1;36m"


def banner():
    print(
        re + " __    __  .______    _______ .______       __        ______   ____    ____  _______     _______.     ______   ______   .___  ___. ")
    print(
        gr + "|  |  |  | |   _  \  |   ____||   _  \     |  |      /  __  \  \   \  /   / |   ____|   /       |    /      | /  __  \  |   \/   | ")
    print(
        re + "|  |  |  | |  |_)  | |  |__   |  |_)  |    |  |     |  |  |  |  \   \/   /  |  |__     |   (----`   |  ,----'|  |  |  | |  \  /  | ")
    print(
        re + "|  |  |  | |   _  <  |   __|  |      /     |  |     |  |  |  |   \      /   |   __|     \   \       |  |     |  |  |  | |  |\/|  | ")
    print(
        re + "|  `--'  | |  |_)  | |  |____ |  |\  \----.|  `----.|  `--'  |    \    /    |  |____.----)   |    __|  `----.|  `--'  | |  |  |  | ")
    print(
        re + " \______/  |______/  |_______|| _| `._____||_______| \______/      \__/     |_______|_______/    (__)\______| \______/  |__|  |__| ")

    print(cy + "version : 1.01")
    print(cy + "Make sure you Subscribed Uber LoverS")
    print(cy + "https://t.me/ubo520")


cpass = configparser.RawConfigParser()
cpass.read('config.data')

try:
    api_id = cpass['cred']['id']
    api_hash = cpass['cred']['hash']
    phone = cpass['cred']['phone']
    client = TelegramClient(phone, api_id, api_hash)
except KeyError:
    os.system('clear')
    banner()
    print(re + "[!] run python3 setup.py first !!\n")
    sys.exit(1)

client.connect()
if not client.is_user_authorized():
    client.send_code_request(phone)
    os.system('clear')
    banner()
    client.sign_in(phone, input(gr + '[+] Enter the code: ' + re))

os.system('clear')
banner()
chats = []
last_date = None
chunk_size = 200
groups = []

result = client(GetDialogsRequest(
    offset_date=last_date,
    offset_id=0,
    offset_peer=InputPeerEmpty(),
    limit=chunk_size,
    hash=0
))
chats.extend(result.chats)

for chat in chats:
    try:
        if chat.megagroup == True:
            groups.append(chat)
    except:
        continue

print(gr + '[+] Choose a group to scrape members :' + re)
i = 0
for g in groups:
    print(gr + '[' + cy + str(i) + ']' + ' - ' + g.title)
    i += 1

print('')
g_index = input(gr + "[+] Enter a Number : " + re)
target_group = groups[int(g_index)]

print(gr + '[+] Fetching Members...')
time.sleep(1)
all_participants = []
# all_participants = client.get_participants(target_group, aggressive=True)
offset = 0
limit = 100
all_participants = []
while True:
    participants = client(GetParticipantsRequest(
        target_group, ChannelParticipantsSearch(''), offset, limit,
        hash=0
    ))
    if not participants.users:
        break
    all_participants.extend(participants.users)
    offset += len(participants.users)
print(gr + '[+] Saving In file...')
time.sleep(1)
print('Saving In file...')

def online_within(participant, days):
    status = participant.status
    if isinstance(status, t.UserStatusOnline):
        return True

    last_seen = status.was_online if isinstance(status, t.UserStatusOffline) else None

    if last_seen:
        now = datetime.datetime.now(tz=datetime.timezone.utc)
        diff = now - last_seen
        return diff <= datetime.timedelta(days=days)

    if isinstance(status, t.UserStatusRecently) and days >= 1 \
            or isinstance(status, t.UserStatusLastWeek) and days >= 7 \
            or isinstance(status, t.UserStatusLastMonth) and days >= 30:
        return True

    return False


with open("members.csv", "w", encoding='UTF-8') as f:
    writer = csv.writer(f, delimiter=",", lineterminator="\n")
    writer.writerow(['username', 'user id', 'access hash', 'name', 'group', 'group id'])
    for user in all_participants:
        accept = True
        try:
            accept = online_within(user, 30)
        except Exception as e:
            continue
        if accept:
            if user.username:
                username = user.username
            else:
                username = ""
            if user.first_name:
                first_name = user.first_name
            else:
                first_name = ""
            if user.last_name:
                last_name = user.last_name
            else:
                last_name = ""
            name = (first_name + ' ' + last_name).strip()
            writer.writerow(
                [username, user.id, user.access_hash, name, target_group.title, target_group.id])

print('Members scraped successfully.')
