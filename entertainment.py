import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg", "https://www.youtube.com/watch?v=vwyZH85NQC4")
#print(toy_story.title)

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://upload.wikimedia.org/wikipedia/id/b/b0/Avatar-Teaser-Poster.jpg", "https://www.youtube.com/watch?v=-9ceBgWV8io")
#avatar.show_trailer()

thupakki = media.Movie("Thuppaki", "The story revolves around an Indian army intelligence officer from a Mumbai-based Tamil family", "http://upload.wikimedia.org/wikipedia/en/b/b0/First_look_Thuppakki.jpg", "https://www.youtube.com/watch?v=aW_j4pNvG98")
#print(thupakki.storyline)
#thupakki.show_trailer()

movies = [toy_story,avatar,thupakki]

#fresh_tomatoes.open_movies_page(movies)
print(media.Movie.__doc__)
print(media.Movie.__name__)