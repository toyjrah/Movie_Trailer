import webbrowser


class Movie():
    ''' This class provides a way to store movie related documentation '''
    valid_ratings = ["G", "PG", "PG-13", "R"]

    def __init__(
            self,
            movie_title,
            movie_storyline,
            poster_image,
            trailer_youtube):
    ''' Attributes of an object for the class Movie'''
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        ''' This function will open the movie trailer on clicking the movie tile on HTML page '''
        webbrowser.open(self.trailer_youtube_url)
