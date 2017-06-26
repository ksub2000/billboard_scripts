import codecs, requests, json, os, time, spotipy, spotipy.util, sys

inputfile = 'June26_songidonly.csv'
outfilename = 'June26_spotify_info.json'

token = 'BQDvjK95m8MbpScPfkGblYVhVe5iwsq8schsUx7IwIZK-0N9umAMMt6IBuAt-_vM2zDuTzGB2SOmLsadjVWTmA'

headers = {'Accept': 'application/json',
           'Authorization': 'Bearer ' + token}

with codecs.open(inputfile, 'r', 'utf-8') as f:
    for song_id in f:
        currentsong = requests.get('https://api.spotify.com/v1/tracks/?ids=' + song_id.strip(), headers=headers)
        print(currentsong)
        with open(outfilename, 'a') as outputfile:
            json.dump(currentsong.json(), outputfile)
print 'done'
