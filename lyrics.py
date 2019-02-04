#lyrics.py

from secrets import *
import lyricsgenius

print("hello there")


genius = lyricsgenius.Genius(genius_key)
song = genius.search_song("Humble", "Kendrick Lamar")
print(song.lyrics)
