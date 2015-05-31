import webbrowser
import youtube_search #use youtube to populate the trailer
import the_movie_db_search #use 'the movie db' to populate overview and poster

class Movie():
# takes a movie title and a date
	def __init__(self, movie_title, movie_date):
		self.title = movie_title
		self.date = movie_date
		self.year = movie_date[-4:]
		content_search_result = the_movie_db_search.ContentSearch(self.title, self.year)
		self.storyline = unicode(content_search_result.overview).encode('utf8')
		self.poster_image_url = content_search_result.poster
		self.trailer_youtube_url = youtube_search.trailer_search(self.title)

	def show_trailer (self):
		webbrowser.open(self.trailer_youtube_url)