import random
import time
from lxml.html import fromstring
import nltk
import requests
import login
nltk.download('punkt')


tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
HEADERS = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5)'
                      ' AppleWebKit/537.36 (KHTML, like Gecko) Cafari/537.36'
    }


def kurtlar_vadisi():
    r = requests.get('https://www.ensonhaber.com/galeri/kurtlar-vadisinden-unutulmayan-sozler', headers=HEADERS)
    tree = fromstring(r.content)
    paras = tree.xpath('//div[@class="item"]//div[@class="item-header"]/p')
    paras_text = [para.text_content() for para in paras if para.text_content()]
    para = random.choice(paras_text)
    para_tokenized = tokenizer.tokenize(para)
    for _ in paras_text:
        text = random.choice(para_tokenized)
        return text


def main():
    print('---Kurtlar Vadisi Bot Başlatılıyor---\n')
    login.twitterLogin()
    while True:
        kurtlar_vadisi()
        kvp = "{}".format(kurtlar_vadisi())
        login.sendTweet(kvp)
        time.sleep(10)


if __name__ == "__main__":
    main()
