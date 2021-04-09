from bs4 import BeautifulSoup as Soup
from urllib.request import urlopen as uReq  # Web client
search_keyword = input()  # The keyword to search in YouTube
base_url = "https://www.youtube.com/results?search_query="
full_url = base_url + search_keyword.replace(" ", "+")
# print(full_url)
yClient = uReq(full_url)  # I will call it my YouTube client
raw_html_data = Soup(yClient.read(), "html.parser")
yClient.close()

print(raw_html_data)
raw_video_list = raw_html_data.findAll("div")
print(raw_video_list[0])
#for x in raw_video_list:
    # print(raw_video_list)