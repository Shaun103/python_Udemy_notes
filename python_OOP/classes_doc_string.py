
class Song:
    """Class to represent a song

    Attributes:
        title (str): The title of the Song
        artist (Artist): An artist object representing the songs crerator
        duration (int): The duration of the song in seconds. May be zero
    """
    def __init__(self, title: str="title", artist: str ="artist", duration: int=0) -> None:
        # # 1st method to add doc strings
        # """Song init method
        #     Args:
        #         title (str): Initialises the 'title' attribute
        #         artist (Artist): At Artist object representing the song's creator
        #         duration (Optional[int]: Initial value for the 'duration' attribute.
        #             will default to zero if not specified.
        # """ 
        self.title = title
        self.artist = artist
        self.duration = duration

class Album:
    """Class to represent an Album, using it's track list
    
    Attributes:
        name (str): The name of the album
        year (int): The year the album was released.
        artist: (Artist): The artist responsible for the album.
            If not specified, the artist will default to an artist with the name
            "various artist
        tracks (List[Song]): A list of the songs on the album
        
        Methods:
            addSong: Used to ad a new son to the album's track list
    """
    def __init__(self, name, year, artist: str=None):
        self.name = name
        self.year = year
        if artist is None:
            #
            self.artist = Artist("Various Artists")
        else:
            self.artist = artist
        self.tracks = []

    def add_song(self, song, position=None):
        """Adds a song to the track list
        
        Args:
            song (Song): A song to add.
            position (Optional[int]): if specified, the song will be added to that position
                in the track list - inserting it between other songs if necessary. 
                Otherwise, the song will be add to the end of the list
        """
        if position is None:
            self.tracks.append(song)
        else:
            self.trackk.insert(position, song)
        
class Artist:
    """basic class to store artist details.
    
    Attributes:
        name (str): The name of the artist.
        albums (List/Album): A list of the albums by this artist.
            The list includes only those albums in this collection, it is
            not an exhaustive list of the artist's published albums
            
    
    MethodsL
        add_albums: use to add a new album to the artist's album list
    """
    def __init__(self, name: str="name") -> None:
        self.name = name
        self.albums = []
    
    def add_album(self, album):
        """Add a new album to the list.
        
        Args: 
            album (Album): Album object to the list 
                If the album is already present, it will not be added again (although this is yet to be implemented).
        """
        self.albums.append(album)



def main():
    print()

    # help(Song.__init__)
    # print(Song.__doc__)
    print(Song.__init__.__doc__)

    # 2nd method to add documentation
    Song.__init__.__doc__ = """Song init method
            Args:
                title (str): Initialises the 'title' attribute
                artist (Artist): At Artist object representing the song's creator
                duration (Optional[int]: Initial value for the 'duration' attribute.
                    will default to zero if not specified.
        """ 

    help(Song)
#_______________________________________________________________________________________

    help(Album)



if __name__ == "__main__":
    main()
    