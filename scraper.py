import sys
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

if len(sys.argv)< 2:
    sys.exit()

site=sys.argv[1]
parser=urlparse(site)
if not parser.scheme:
    site= "https://"+site

opt=Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
opt.add_argument("--no-sandbox")

driver=webdriver.Chrome(options=opt)
driver.get(site)
driver.implicitly_wait(5)
page=driver.page_source
driver.quit()

bs=BeautifulSoup(page, "html.parser")

if bs.title is not None:
    print("Title:")
    print(bs.title.text.strip())
else:
    print("Title not found")

if bs.body is not None:
    bdy_txt= bs.body.get_text(separator=" ",strip=True)
    print("Page Body:")
    print(bdy_txt)
else:
    print("Body not found")

all_links=[]
for a in bs.find_all("a"):
    link_val=a.get("href")
    if link_val and link_val not in all_links:
        all_links.append(link_val)

print("\nAll Links:")
for link in all_links:
    print(link)
