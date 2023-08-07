from bs4 import BeautifulSoup
import requests

def Parsing(keyword):
    Header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.83 Safari/537.36'
    }
    url = 'https://genie.co.kr/search/searchSong?query='+keyword
    IMGurl = 'https://image.genie.co.kr/'
    selectorX = '#body-content > div.search_song > div.music-list-wrap > div.music-list-wrap > table > tbody > tr:nth-child(1) > '
    try:
        html = BeautifulSoup((requests.get(url, headers=Header)).content, "html.parser", from_encoding="utf-8")
        songName = html.select(selectorX + 'td.info > a.title.ellipsis')[0].text.replace('\t', '').replace('\n', '').replace('  ', '').replace('TITLE', '').strip()
        songArtist = html.select(selectorX + 'td.info > a.artist.ellipsis')[0].text.strip()
        albumArtSrc = IMGurl+html.select(selectorX + 'td:nth-child(3) > a > img')[0].get('src')
        return songName,songArtist,albumArtSrc
    except:
        return 'error'

print(Parsing(input('songname and artist')))