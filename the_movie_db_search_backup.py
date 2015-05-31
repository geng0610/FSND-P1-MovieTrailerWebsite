import requests
CONFIG_PATTERN = 'http://api.themoviedb.org/3/configuration?api_key={key}'
KEY = '714806343d1619b0feac0f2112834cc0'

url = CONFIG_PATTERN.format(key=KEY)
r = requests.get(url)
config = r.json()
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

'''
IMG_PATTERN = 'http://api.themoviedb.org/3/search/movie?api_key=714806343d1619b0feac0f2112834cc0&query=iron man&year=2008' 
r = requests.get(IMG_PATTERN)#.format(key=KEY,imdbid='tt0095016'))
api_response = r.json()['results'][0]['poster_path']
print api_response
print base_url+max_size+api_response
'''

SEARCH_API_PATTERN = 'http://api.themoviedb.org/3/search/movie?api_key={key}&query={name}&year={year}'
class ContentSearch():
	def __init__(this, movie_name, movie_year):
		search_api_url = SEARCH_API_PATTERN.format(key=KEY, name=movie_name, year=movie_year)
		print search_api_url
		search_api_response = requests.get(search_api_url).json()
		this.overview = search_api_response['results'][0]['overview']
		poster_path = search_api_response['results'][0]['poster_path']
		this.poster = image_base_url+image_max_size+poster_path