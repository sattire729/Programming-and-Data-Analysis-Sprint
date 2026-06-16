# 8-8 User Albums: Start with your program from Exercise 8-7. Write a while loop that allows users to enter an album's artist and title. Once you have that information, call make_album() with the user's input and print the dictionary that's created. Be sure to include a quit value in the while loop.

def make_album(artist_name, album_title):
    dictionary = {'Artist Name' : artist_name, 'Album Title': album_title}
    return dictionary

while True:
    print("\nPlease enter the album's artist and title:")
    print("Enter 'q' anytime to Exit the Program")
    artist = input("Please Enter the Artist's name: ")
    if artist == 'q':
        break

    title = input("Please Enter the Album Title: ")
    if title == 'q':
        break

    album_info = make_album(artist, title)
    print(album_info)


