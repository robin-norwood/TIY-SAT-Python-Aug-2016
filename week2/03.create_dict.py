# coding: utf-8

# Data looks like this:
classic_songs = [["1973", "Don't stop believing"], ["1971", "All along the watchtower"], ["1973", "Do-wop"]]

# We want a dictionary that counts songs per year:
songs_per_year = { "1973": 2, "1971": 1 }

# start with empty dict:
spy = {}

# Loop over songs
for song in classic_songs:
    if song[0] in spy: # if this year is in dict, increment counter
        spy[song[0]] += 1
    else: # if it isn't, start at 1 song found for this year
        spy[song[0]] = 1
        

# Next, find the largest number of songs

most_songs = 0 # What's the most # of songs?
most_songs_year = None # What year was it?
        
for (yr, count) in spy.items(): # go through each (year, count) in dict
    if count > most_songs: # if this count is the most so far...
        most_songs = count  # remember the count and year
        most_songs_year = yr
        
most_songs
most_songs_year
