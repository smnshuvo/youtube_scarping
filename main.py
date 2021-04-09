# from bs4 import BeautifulSoup as Soup
# from urllib.request import urlopen as uReq  # Web client
# search_keyword = input()  # The keyword to search in YouTube
# base_url = "https://www.youtube.com/results?search_query="
# full_url = base_url + search_keyword.replace(" ", "+")
# # print(full_url)
# yClient = uReq(full_url)  # I will call it my YouTube client
# raw_html_data = Soup(yClient.read(), "html.parser")
# yClient.close()
#
#
#
# raw_video_list = raw_html_data.findAll("yt-formatted-string")
# print(raw_video_list[0])
# #for x in raw_video_list:
#     # print(raw_video_list)

I gave up scrapping YouTube videos using
Beautiful soup. BS is not the right tool for
YouTube scrapping as YouTube does a lot of
processing in js