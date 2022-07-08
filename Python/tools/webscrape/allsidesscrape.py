import requests
from bs4 import BeautifulSoup

url = 'https://www.allsides.com/media-bias/media-bias-ratings'

r = requests.get(url)

soup = BeautifulSoup(r.content, "html.parser")

#select_one('body') gets the body element
#select_one('.temp') to get <a class="temp"></a>
#select_one('#temp') to get <a id="temp"></a>
#select_one('.temp a') to get <div class="temp"><a></a></div>
#select_one('.temp.example') to get <a class="temp example"></a>

rows = soup.select('tbody tr')

row = rows[0]
name = row.select_one('.views-field-title')
nametext = row.select_one('.views-field-title').text.strip()
print(name)
print(nametext)

