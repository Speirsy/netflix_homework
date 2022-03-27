class Profile:
    def __init__(self, user_name, password ):

        self.user_name = user_name
        self.password = password
        self.favourites = []

    def favs_length(self):
        return len(self.favourites)

    def add_movie(self, movie_to_add):
        self.favourites.append(movie_to_add)

    def remove_movie(self, movie_to_remove):
        self.favourites.remove(movie_to_remove)

