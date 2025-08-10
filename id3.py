import json
import os
import sys

sys.path.append('C:/Users/alanl/Documents/Python/venvs/music/Lib/site-packages')

import pandas as pd
import eyed3

edge_cases = {
    'yes, and': 'yes, and?',
    "Who's That Chick": "Who's That Chick?",
    'Mama-Show Love': 'Mama/Show Love',
    'Am I Okay': 'Am I Okay?',
    'AMPM': 'AM:PM',
    'bad idea right': 'bad idea right?',
    '...Ready For It': '...Ready For It?',
    "Is It Over Now (Taylor's Version)": "Is It Over Now? (Taylor's Version)",
    '1035': '10:35',
    'Alan Walker ft. AuRa, Tomine Harket': 'Alan Walker ft. Au/Ra, Tomine Harket',
    'Why Is She Still Here': 'Why Is She Still Here?'
}

json_df = pd.read_json('music.json')

dir_list = os.listdir("C:/Users/alanl/Music")

for item in dir_list:
    if '.mp3' not in item:
        continue

    artist = item.split(' - ')[0]
    title = item.split(' - ')[1].split('.mp3')[0]
    if title in edge_cases:
        title = edge_cases[title]
    if artist in edge_cases:
        artist = edge_cases[artist]
    genre = json_df[(json_df['song'] == title) & (json_df['artist'] == artist)]['genre'].iloc[0]

    path = f"C:/Users/alanl/Music/{item}"
    file = eyed3.load(path)
    file.tag.artist = artist
    file.tag.title = title
    file.tag.genre = genre
    file.tag.save()

sheet_df = pd.read_csv('https://docs.google.com/spreadsheets/d/13OPoSocCPJEkbbL6NspkAmCLjPITbGK-25kKujqCJdw/export?gid=0&format=csv', names=['artist', 'song', 'genre'])

for item in dir_list:
    if '.mp3' not in item:
        continue

    path = f"C:/Users/alanl/Music/{item}"
    file = eyed3.load(path)
    artist = file.tag.artist
    title = file.tag.title
    genre = file.tag.genre

    entry = sheet_df[(sheet_df['song'] == title) & (sheet_df['artist'] == artist) & (sheet_df['genre'] == genre)]
    if entry.empty:
        print('WARNING')
        print(artist, title, genre)
        print('is not in the Google Sheet')
        break
