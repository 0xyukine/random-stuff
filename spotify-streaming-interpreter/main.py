import os
import json

artists = {}
songs = {}

for json_file in os.listdir():
    if "Streaming_History_Audio" in json_file:
        print(json_file)
        with open(json_file) as f:
            f = json.load(f)
            for item in f:
                artist_key = 'master_metadata_album_artist_name'
                song_key = 'master_metadata_track_name'

                if item[artist_key] in artists.keys():
                    artists[item[artist_key]]['count'] += 1
                else:
                    artists.update({item[artist_key]:{'count':1}})

                if item[song_key] in songs.keys():
                    songs[item[song_key]]['count'] += 1
                else:
                    songs.update({item[song_key]:{'count':1,'artist':item[artist_key]}})

with open('artists.json', 'w') as f:
    json.dump(artists, f, indent=4)

with open('songs.json', 'w') as f:
    json.dump(songs, f, indent=4)

                
