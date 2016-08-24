# Imports all functions from media.py file
import media

# Imports all functions from media.py file
import fresh_tomatoes


# Instantiates objects for class Movie and stores it in a variable
TOY_STORY = media.Movie(
    "Toy Story",
    "A story of a boy and his toys",
    "https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
    "https://www.youtube.com/watch?v=KYz2wyBy3kc")

AVATAR = media.Movie(
    "Avatar",
    "A paraplegic marine dispatched to the moon"
    "Pandora on a unique mission becomes torn between"
    "following his orders and protecting the world he feels is his home",
    "http://tinyurl.com/j8gejt2",
    "https://www.youtube.com/watch?v=5PSNL1qE6VY")

BATMAN = media.Movie(
    "The Dark Knight",
    "When the menace known as the Joker wreaks havoc and chaos"
    "on the people of Gotham, the caped crusader must come to terms"
    "with one of the greatest psychological tests of his ability to"
    "fight injustice.",
    "https://upload.wikimedia.org/wikipedia/en/8/8a/Dark_Knight.jpg",
    "https://www.youtube.com/watch?v=EXeTwQWrcwY")

GUARDIANS = media.Movie(
    "Legend of the Guardians: The Owls of Ga'Hoole",
    "When a young owl is abducted by an evil Owl army,"
    " he must escape with new-found friends and seek the legendary"
    "Guardians to stop the menace.",
    "http://tinyurl.com/hzppjhz",
    "https://www.youtube.com/watch?v=x8RKCmkOyB4")

SCHOOL = media.Movie(
    "School of Rock",
    "After being kicked out of a rock band,"
    " Dewey Finn becomes a substitute teacher of a strict"
    " elementary private school,"
    " only to try and turn it into a rock band.",
    "https://upload.wikimedia.org/wikipedia/en/1/11/School_of_Rock_Poster.jpg",
    "https://www.youtube.com/watch?v=XCwy6lW5Ixc")

ROCKY = media.Movie(
    "Rocky",
    "Rocky Balboa, a small-time boxer,"
    " gets a supremely rare chance to fight the heavy-weight champion,"
    " Apollo Creed, in a bout in which he strives to go the distance"
    "for his self-respect.",
    "http://tinyurl.com/jly4b7c",
    "https://www.youtube.com/watch?v=7RYpJAUMo2M")

SHAWSHANK = media.Movie(
    "The Shawshank Redemption",
    "Two imprisoned men bond over a number of years,"
    " finding solace and eventual redemption through acts of common decency.",
    "http://tinyurl.com/zy6nv5v",
    "https://www.youtube.com/watch?v=6hB3S9bIaco")

# All variables are in an Array
movies = [TOY_STORY, AVATAR, BATMAN, GUARDIANS, SCHOOL, ROCKY, SHAWSHANK]

# Function open_movies_page is called from fresh_tomatoes and variable
# movies is passed as an argument
fresh_tomatoes.open_movies_page(movies)

# Prints documentation from class Movie
print media.Movie.__doc__

# Prints the name of the class
print media.Movie.__name__

# Prints the name of the module
print media.Movie.__module__
