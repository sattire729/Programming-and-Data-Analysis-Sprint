# 8-7 Album: Write a function called make_album() that builds a dictionary describing a music album. The function should take in an aritst name and an album title, and it should return a dictionary containing these two pieces of information. Use the function to make three dictionaries representing different albums. Print each return value to show that the dictionaries are storing the information correctly.
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. If the calling line includes a value for the number of songs, add that value to the album's dictionary. Make at least one new function call that includes the number of songs on an album.

def make_album(artist_name, album_title, album_length=None):
    dictionary = {'Artist Name' : artist_name, 'Album Title': album_title}
    if album_length:
        dictionary['Album_length'] = album_length
    return dictionary

album_1 = make_album('Furina', 'La Vaguelette')
album_2 = make_album('Pradyumna', 'Emo Hyperpop')
album_3 = make_album('Wey', 'Bullshit')
album_4 = make_album('Taiga', 'Orange', 7)

print(album_1)
print(album_2)
print(album_3)
print(album_4)