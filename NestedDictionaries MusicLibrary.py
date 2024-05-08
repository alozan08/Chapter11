def add_artist(music, artist):
    if artist not in music.keys():
        music[artist] = {}
    else:
        print("Artist Already Exists")


def add_album(music, artist, album_name, year, platinum):
    if artist in music:
        if album_name not in music[artist]:
            music[artist][album_name] = {
                'songs': [],
                'year': year,
                'platinum': platinum
            }
            print(f'{album_name} added to {artist}')
        else:
            print(f'{album_name} Already Exists')

def add_song(music, artist, album_name, song_name):
    if artist in music:
        if album_name in music[artist]:
            if song_name not in music[artist][album_name]['songs']:
                music[artist][album_name]['songs'].append(song_name)
                print(f'{song_name} added to {artist}')
            else:
                print(f'{song_name} Already Exists')
        else:
            print(f'{album_name} does not exist in {artist}')
    else:
        print(f'{artist} does not exist')

music = {
    'Pink Floyd': {
        'The Dark Side of the Moon': {
            'songs': [ 'Speak to Me', 'Breathe', 'On the Run', 'Money'],
            'year': 1973,
            'platinum': True
        },
        'The Wall': {
            'songs': [ 'Another Brick in the Wall', 'Mother', 'Hey you'],
            'year': 1979,
            'platinum': True
        }
    },
    'Justin Bieber': {
        'My World':{
            'songs': ['One Time', 'Bigger', 'Love Me'],
            'year': 2010,
            'platinum': True
        }
    }
}
# First, add a command that adds an artist name to the music dictionary.
# Then add commands for adding albums and songs. Take care to check that
# an artist exists in the dictionary before adding an album, and that an
# album exists before adding a song.



while True:
    command = input("Enter a command (add-artist, add-album, add-song, quit): ")
    command = command.lower()

    if command == "add-artist":
        artist_name = input("Enter artist name: ")
        add_artist(music, artist_name)

    elif command == "add-album":
        artist_name = input("Enter artist name: ")
        album_name = input("Enter album name: ")
        year = int(input("Enter album year: "))
        platinum = input("Did it go platinum? (True/False)")
        add_album(music, artist_name, album_name, year, platinum)

    elif command == "add-song":
        artist_name = input("Enter artist name: ")
        album_name = input("Enter album name: ")
        song_name = input("Enter song name: ")
        add_song(music, artist_name, album_name, song_name)

    elif command == "quit":
        print("Exiting...")
        break

    else:
        print("Unknown command. Please try again.")

