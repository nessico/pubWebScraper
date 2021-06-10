import discord
import urllib3
import requests
from bs4 import BeautifulSoup


CLIENT_ID = 'REDACTED' # REDACTED
CLIENT_SEC = 'REDACTED' # REDACTED
TOKEN = 'REDACTED' # REDACTED
 

client = discord.Client()


def splitInput(mes):
    # getting url from user
    fURL = str(mes)
    fURL = fURL.split(".c ")[1]
    return fURL


def openWebPage(URL):
    # opening page and inserting id_token
    headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:66.0) Gecko/20100101 Firefox/66.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate", "DNT": "1", "Connection": "close", "Upgrade-Insecure-Requests": "1"}
    cookies = dict(id_token='Redacted')  # REDACTED
    r = requests.get(URL, headers=headers, cookies=cookies)

    # parsing html text to find the answer
    soup = BeautifulSoup(r.text, 'html.parser')
    parsed = soup.find("div", class_="REDACTED") # REDACTED

    # formatting parse into text and images
    parsedtext = parsed.get_text()

    images = []
    for img in parsed.findAll('img'):
        images.append(img.get('src'))

    global parsedfinal
    parsedfinal = "text: " + parsedtext + "\n" + "images:" + str(images)
    return parsedfinal


@client.event
async def on_message(message):
    if(message.content.startswith('.c')):
        URL = splitInput(message.content)
        Answer = openWebPage(URL)

        # separating into separate messages if it passes character limit
        n = 1999
        chunks = [Answer[i:i+n] for i in range(0, len(Answer), n)]
        for x in chunks:
            await message.channel.send(str(x))


# send a web cookie where it creates a id_token valued REDACTED
# and inserts it with the link. then parse html or take screenshot. inspect element -> application -> cookies -> id_token

async def on_ready(self):
    print('Logged on as: {0}!', format(self.user))


client.run(TOKEN)
