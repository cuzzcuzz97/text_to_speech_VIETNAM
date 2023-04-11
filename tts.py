from selenium import webdriver
import time
import requests
import threading
from removeaccentVN import remove_accents

def download_audio_banmai(text):
    options = webdriver.ChromeOptions()
    options.add_argument("headless")
    web = webdriver.Chrome(options=options)
    web.get('https://fpt.ai/tts')
    last = web.find_element('xpath','//*[@id="tts-text"]')
    last.send_keys(text)
    time.sleep(1)
    Submit = web.find_element('xpath','//*[@id="tts-speak"]')
    Submit.click()
    time.sleep(len(text)*0.1)
    output = web.find_element('xpath','//*[@id="tts-audio"]')
    URL = output.get_attribute('src')
    return URL
    # response = requests.get(URL)
    # file_name = remove_accents(text)
    # filename = f"{'-'.join(file_name.split())}.mp3"
    # open(f'output/{filename}', "wb").write(response.content)
    # web.close()

with open('input.txt','r') as f:
    texts = f.readlines()

res = []
titles = []
for text in texts:
    t = download_audio_banmai(text.replace('\n',''))
    if t.endswith('juicy.mp3'):
        ...
    else:
        titles.append(remove_accents(text))
        res.append(t)

with open('output.txt', 'w') as file:
    for i,x in enumerate(res):
        file.writelines(titles[i] + ':' + x + '\n')
# threads = []

# for text in res:
#     t = threading.Thread(target=download_audio_banmai, args=(text,))
#     t.start()
#     threads.append(t)

# for thread in threads:
#     thread.join()

print('download successful')
