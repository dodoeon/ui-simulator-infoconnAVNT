from bs4 import BeautifulSoup
import requests
from flask import Flask, render_template, request

app = Flask(__name__)

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

@app.route('/', methods=['GET'])
def notice():

    return render_template('index.html')

@app.route('/play', methods=['GET'])
def index(): 
    if request.method == 'GET':
        songName = request.args.get("songName")
        artist = request.args.get("artist")
        data = Parsing(songName +" "+ artist)
        print(request.form)
        
    return render_template('song.html', songName = data[0], artist = data[1] , albumArt = data[2])
    
if __name__ == "__main__":
    app.run()