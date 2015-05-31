import requests


#use the movie db to generate content (overview and link to a poster)
CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
KEY = '714806343d1619b0feac0f2112834cc0'


#get the configuration once and save it in memory
url = CONFIG_PATTERN.format(key=KEY)
r = requests.get(url)
config = r.json()
#image path is in the format of image_base_url+image_size+poster_path
image_base_url = config['images']['base_url']
image_sizes = config['images']['poster_sizes'] 
"""
    'sizes' should be sorted in ascending order, so
        max_size = sizes[-1]
    should get the largest size as well.        
"""
def size_str_to_int(x):
    return float("inf") if x == 'original' else int(x[1:])
image_max_size = max(image_sizes, key=size_str_to_int)



SEARCH_API_PATTERN = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={name}&year={year}'

#actual method used to find the overview and path for the poster
class ContentSearch():
	def __init__(this, movie_name, movie_year):
		search_api_url = SEARCH_API_PATTERN.format(key=KEY, name=movie_name, year=movie_year)
		print search_api_url #for sense checking
		search_api_response = requests.get(search_api_url).json() #read the json
		this.overview = search_api_response['results'][0]['overview']
		poster_path = search_api_response['results'][0]['poster_path']
		this.poster = image_base_url+image_max_size+poster_path