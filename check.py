import sys
import os
import json

sys.path.append('C:/Users/alanl/Documents/Python/venvs/music/Lib/site-packages')

import pandas as pd

sheet_df = pd.read_csv('https://docs.google.com/spreadsheets/d/13OPoSocCPJEkbbL6NspkAmCLjPITbGK-25kKujqCJdw/export?gid=0&format=csv', names=['artist', 'song', 'genre'])
json_df = pd.read_json('music.json')

for sheet_row, json_row in zip(sheet_df.itertuples(), json_df.itertuples()):
    if sheet_row.artist != json_row.artist:
        print('artist mismatch')
        print(sheet_row)
        print(json_row)
    if sheet_row.song != json_row.song:
        print('song mismatch')
        print(sheet_row)
        print(json_row)
    if sheet_row.genre != json_row.genre:
        print('genre mismatch')
        print(sheet_row)
        print(json_row)

if len(sheet_df.index) != len(json_df.index):
    print('number of songs do not match')
    print(f'sheet: {len(sheet_df.index)}')
    print(f'json: {len(json_df.index)}')
