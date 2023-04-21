# from https://youtu.be/cta1yCb3vA8
from requests_html import HTMLSession

s = HTMLSession()

query = 'Philadelphia'
url = f'https://www.google.com/search?q=weather+{query}'

r = s.get(url, headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48'})
#print(r.html.find('title',first=True).text)
temp = r.html.find('span#wob_tm',first=True).text
unit = r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text # search for class with div
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text
high = r.html.find('div.gNCp2e', first=True).find('span.wob_t', first=True).text
low = r.html.find('div.wNE31c', first=True).find('span.wob_t')[2].text

print(f"Current weather in {query}: {desc} {temp}{unit}")
print(f"High: {high} \t Low: {low}")



